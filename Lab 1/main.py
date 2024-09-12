import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
import math
import random

training_dataroot = "lab1_basic_training.csv"  # Training data file file named as 'lab1_basic_training.csv'
testing_dataroot = (
    "lab1_basic_testing.csv"  # Testing data file named as 'lab1_basic_testing.csv'
)
output_dataroot = "lab1_basic.csv"  # Output file will be named as 'lab1_basic.csv'

training_datalist = []  # Training datalist, saved as numpy array
testing_datalist = []  # Testing datalist, saved as numpy array

output_datalist = []  # Your prediction, should be a list with 100 elements


# Read input csv to datalist
with open(training_dataroot, newline="") as csvfile:
    training_datalist = pd.read_csv(training_dataroot).to_numpy()

with open(testing_dataroot, newline="") as csvfile:
    testing_datalist = pd.read_csv(testing_dataroot).to_numpy()


def SplitData(data, split_ratio):
    training_data = []
    validation_data = []

    data_size = len(data)
    training_data = data[: math.floor(data_size * split_ratio)]
    validation_data = data[math.floor(data_size * split_ratio) :]

    return training_data, validation_data


def PreprocessData(data):
    preprocessedData = data

    data_removed_nan = np.array(
        [i for i in preprocessedData if not np.isnan(i[0]) and not np.isnan(i[1])]
    )

    (x_mean, y_mean) = np.mean(data_removed_nan, axis=0).tolist()
    print(f"{(x_mean, y_mean)=}")

    x_q25, x_q50, x_q75 = np.percentile(data_removed_nan[:, 0], [25, 50, 75]).tolist()
    y_q25, y_q50, y_q75 = np.percentile(data_removed_nan[:, 1], [25, 50, 75]).tolist()
    print(f"{(x_q25, x_q75)=}, {(y_q25, y_q75)=}")

    x_iqr = x_q75 - x_q25
    y_iqr = y_q75 - y_q25
    print(f"{x_iqr=}, {y_iqr=}")

    x_ac_range = (x_q25 - 1.5 * x_iqr, x_q75 + 1.5 * x_iqr)
    y_ac_range = (y_q25 - 1.5 * y_iqr, y_q75 + 1.5 * y_iqr)
    print(f"{x_ac_range=}, {y_ac_range=}")

    res = []
    for i in preprocessedData:
        # nan value
        if (
            np.isnan(i[0])
            or np.isnan(i[1])
            or not x_ac_range[0] <= i[0] <= x_ac_range[1]
            or not y_ac_range[0] <= i[1] <= y_ac_range[1]
        ):
            continue

        res.append(i)

    res = np.array(res)

    # plt.scatter(res[:, 0], res[:, 1])
    # plt.show()
    # print(len(res))
    # print(len(data))

    return res


def mape(y, y_pred):
    res = np.mean(np.absolute(np.subtract(y, y_pred) / y))
    return res


def MakePrediction(w, test_dataset):
    prediction = []

    for data in test_dataset:
        prediction.append(w[0] + w[1] * data + w[2] * data * data)

    return np.array(prediction)


def Regression(dataset, mape_record):
    X = dataset[:, :1]
    y = dataset[:, 1]

    degree = 2  # For example, quadratic regression

    # Add polynomial features to X
    X_poly = np.ones((X.shape[0], 1))  # Add intercept term (column of ones)
    for d in range(1, degree + 1):
        X_poly = np.hstack((X_poly, X**d))  # Add x^d terms to feature matrix

    # Initialize coefficients (weights) to zero
    # Number of features (including intercept and polynomial terms)
    num_dimensions = X_poly.shape[1]
    w = np.zeros(num_dimensions)  # shihtl> 這個 w 就是我們要解的東西

    num_iteration = 70_0000
    base_rate = 5e-8

    # Gradient Descent
    m = len(y)  # Number of data points
    for iteration in range(2, 2 + num_iteration):
        learning_rate = base_rate * (1 / math.log1p(iteration))
        y_hat = X_poly @ w
        d = y - y_hat

        g = -2 * (np.transpose(d) @ X_poly) / m

        w = w - learning_rate * g

        if iteration % 5000 == 0:
            mse = np.sum((y - y_hat) ** 2) / len(y)
            valid_pred = MakePrediction(w, valid_data[:, 0])
            mape_ = mape(valid_data[:, 1], valid_pred)
            print(f"Iteration {iteration}, MSE: {mse}, mape: {mape_}")

    return w


training_datalist = PreprocessData(training_datalist)
training_data, valid_data = SplitData(training_datalist, 0.85)

mape_record = []
w = Regression(training_data, mape_record)
plt.plot(mape_record)
plt.show()

valid_pred = MakePrediction(w, valid_data[:, 0])
print(mape(valid_data[:, 1], valid_pred))
output_datalist = MakePrediction(w, testing_datalist[:, 0])

input()

with open(output_dataroot, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Id", "gripForce"])
    for i in range(len(output_datalist)):
        writer.writerow([i, output_datalist[i]])
