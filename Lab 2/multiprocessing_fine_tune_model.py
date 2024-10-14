import numpy as np
import pandas as pd
import math
import random
from numpy import sqrt
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
import time
from multiprocessing import Manager, Pool
from itertools import product

input_data = pd.read_csv("lab2_basic_input.csv")

max_depth = 2
depth = 0
min_samples_split = 2
n_features = input_data.shape[1] - 1


def entropy(data):
    """
    This function measures the amount of uncertainty in a probability distribution
    args:
    * data(type: DataFrame): the data you're calculating for the entropy
    return:
    * entropy_value(type: float): the data's entropy
    """
    p = 0  # to count the number of cases that survived
    n = 0  # to count the number of cases that passed away

    # Hint 1: what is the equation for calculating entropy?
    # Hint 2: consider the case when p == 0 or n == 0, what should entropy be?
    p = data[data["hospital_death"] == 1].count()["hospital_death"]
    n = data[data["hospital_death"] == 0].count()["hospital_death"]

    # shihtl> note that log2(0) = inf
    if p == 0 or n == 0:
        return 0

    p_ratio = p / (p + n)
    n_ratio = n / (p + n)

    entropy_value = -p_ratio * math.log2(p_ratio) - n_ratio * math.log2(n_ratio)
    entropy_value = round(entropy_value, 4)

    return entropy_value


def information_gain(data, mask):
    """
    This function will calculate the information gain
    args:
    * data(type: DataFrame): the data you're calculating for the information gain
    * mask(type: Series): partition information(left/right) of current input data,
      - boolean 1(True) represents split to left subtree
      - boolean 0(False) represents split to right subtree
    return:
    * ig(type: float): the information gain you can obtain by classifying the data with this given mask
    """

    # Hint: you should use mask to split the data into two, then recall what is the equation for calculating information gain
    left = data.where(mask == True)
    right = data.where(mask == False)

    left_count = left.count()["hospital_death"]
    right_count = right.count()["hospital_death"]

    left_ratio = left_count / (left_count + right_count)
    right_ratio = right_count / (left_count + right_count)

    ig = entropy(data) - (left_ratio * entropy(left) + right_ratio * entropy(right))
    ig = round(ig, 4)

    return ig


def make_partition(data, feature, threshold):
    """
    This function will split the data into 2 branches
    args:
    * data(type: DataFrame): the input data
    * feature(type: string): the attribute(column name)
    * threshold(type: float): the threshold for splitting the data
    return:
    * left(type: DataFrame): the divided data that matches(less than or equal to) the assigned feature's threshold
    * right(type: DataFrame): the divided data that doesn't match the assigned feature's threshold
    """

    left = data[data[feature] <= threshold]
    right = data[data[feature] > threshold]

    return left, right


def classify_data(instance, tree):
    """
    This function will predict/classify the input instance
    args:
    * instance: a instance(case) to be predicted
    return:
    * answer: the prediction result (the classification result)
    """
    equation = list(tree.keys())[0]
    if equation.split()[1] == "<=":
        temp_feature = equation.split()[0]
        temp_threshold = equation.split()[2]
        if instance[temp_feature] > float(temp_threshold):
            answer = tree[equation][1]
        else:
            answer = tree[equation][0]
    else:
        if instance[equation.split()[0]] in (equation.split()[2]):
            answer = tree[equation][0]
        else:
            answer = tree[equation][1]

    if not isinstance(answer, dict):
        return answer
    else:
        return classify_data(instance, answer)


def make_prediction(tree, data):
    """
    This function will use your pre-trained decision tree to predict the labels of all instances in data
    args:
    * tree: the decision tree
    * data: the data to predict
    return:
    * y_prediction: the predictions
    """

    # [Note] You can call the function classify_data() to predict the label of each instance
    y_prediction = []
    for _, entry in data.iterrows():
        y_prediction.append(classify_data(entry, tree))

    return y_prediction


def calculate_score(y_true, y_pred):
    """
    This function will calculate the f1-score of the predictions
    args:
    * y_true: the ground truth
    * y_pred: the predictions
    return:
    * score: the f1-score
    """
    score = f1_score(y_true, y_pred)

    return score


advanced_training_data = pd.read_csv("lab2_advanced_training.csv")
advanced_training_data

advanced_testing_data = pd.read_csv("lab2_advanced_testing.csv")
advanced_testing_data

# shihtl> 暫時用 98%
training_data = advanced_training_data[
    : math.ceil(advanced_training_data.shape[0] * 0.98)
]
validation_data = advanced_training_data[
    math.ceil(advanced_training_data.shape[0] * 0.98) :
]

import logging

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[logging.FileHandler("./logs/fine_tune_log.log"), logging.StreamHandler()],
)


# Define the attributes
max_depth = 5
depth = 0
min_samples_split = 200

# total number of trees in a random forest
n_trees = 5

# number of features to train a decision tree
n_features = 8

# the ratio to select the number of instances
sample_size = 0.3
n_samples = int(training_data.shape[0] * sample_size)

# seed
SEED = 48567108467
random.seed(SEED)
rng = np.random.default_rng(seed=SEED)

# ig split attributes
percentile_count = 33
percentile_each = 1 / percentile_count

# for output file name
PARAMS = f"{max_depth}_{min_samples_split}_{n_trees}_{n_features}_{sample_size}_{SEED}_{percentile_count}"
PARAMS_PRINT = f"{max_depth=}, {min_samples_split=}, {n_trees=}, {n_features=}, {sample_size=}, {SEED=}, {percentile_count=}"


best_ig = -1e9
best_threshold = 0
best_feature = ""


def find_best_split_advance(data):
    """
    This function will find the best split combination of data
    args:
    * data(type: DataFrame): the input data
    * impl_part(type: string): 'basic' or 'advanced' to specify which implementation to use
    return
    * best_ig(type: float): the best information gain you obtain
    * best_threshold(type: float): the value that splits data into 2 branches
    * best_feature(type: string): the feature that splits data into 2 branches
    """
    best_ig = -1e9
    best_threshold = 0
    best_feature = ""

    data_size = data.shape[0]
    # print(data_size)
    for this_feature in data.columns[:-1]:
        # shihtl> sort by each feature
        this_data = data.sort_values(this_feature)

        # shihtl> traversal all entries
        for percent in range(percentile_count):
            split_idx = min(
                data_size - 2, math.floor(data_size * percent * percentile_each)
            )
            # print(split_idx)

            # if (
            #     this_data.iloc[split_idx][this_feature]
            #     == this_data.iloc[split_idx + 1][this_feature]
            # ):
            #     continue

            this_threshold = (
                this_data.iloc[split_idx][this_feature]
                + this_data.iloc[split_idx + 1][this_feature]
            ) / 2
            this_mask = data[this_feature] <= this_threshold
            this_ig = information_gain(data, this_mask)

            # print(f"{this_ig}, {this_threshold}, {this_feature}")
            # shihtl> find max ig
            if this_ig > best_ig:
                best_ig, best_threshold, best_feature = (
                    this_ig,
                    this_threshold,
                    this_feature,
                )

        # print(f"Done {this_feature}!")

    best_ig = round(best_ig, 4)

    # best_ig, best_threshold = float(best_ig), float(best_threshold)

    return best_ig, best_threshold, best_feature


def process(args):
    data, feature, percent = args

    # global best_ig, best_threshold, best_feature
    # logger.info(f"Start process {feature}, {percent}")

    data_size = data.shape[0]
    this_data = data.sort_values(feature)

    split_idx = min(data_size - 2, math.floor(data_size * percent * percentile_each))
    # print(split_idx)

    if feature == "gender":
        this_threshold = 0.5
    else:
        while (
            split_idx < data_size - 2
            and this_data.iloc[split_idx][feature]
            == this_data.iloc[split_idx + 1][feature]
        ):
            split_idx += 1

        this_threshold = (
            this_data.iloc[split_idx][feature] + this_data.iloc[split_idx + 1][feature]
        ) / 2

    this_mask = data[feature] <= this_threshold
    this_ig = information_gain(data, this_mask)

    # logger.info(f"Done process {feature}, {percent}")
    return this_ig, this_threshold, feature


def MP_find_best_split_advance(data):
    """
    This function will find the best split combination of data
    args:
    * data(type: DataFrame): the input data
    * impl_part(type: string): 'basic' or 'advanced' to specify which implementation to use
    return
    * best_ig(type: float): the best information gain you obtain
    * best_threshold(type: float): the value that splits data into 2 branches
    * best_feature(type: string): the feature that splits data into 2 branches
    """

    global pool, lock

    best_ig = -1e9
    best_threshold = 0
    best_feature = ""

    input_product = list(product([data], data.columns[:-1], range(percentile_count)))
    with lock:
        res = pool.map(process, input_product)

        for line in res:
            this_ig, this_threshold, feature = line
            if this_ig > best_ig:
                best_ig, best_threshold, best_feature = (
                    this_ig,
                    this_threshold,
                    feature,
                )

    best_ig = round(best_ig, 4)

    return best_ig, best_threshold, best_feature


def build_tree_advance(data, max_depth, min_samples_split, depth, mp):
    """
    This function will build the decision tree
    args:
    * data(type: DataFrame): the data you want to apply to the decision tree
    * max_depth: the maximum depth of a decision tree
    * min_samples_split: the minimum number of instances required to do partition
    * depth: the height of the current decision tree
    return:
    * subtree: the decision tree structure including root, branch, and leaf (with the attributes and thresholds)
    """

    # check the condition of current depth and the remaining number of samples
    if depth < max_depth and data.shape[0] > min_samples_split:
        # call find_best_split_advance() to find the best combination
        ig, threshold, feature = (
            MP_find_best_split_advance(data) if mp else find_best_split_advance(data)
        )

        # logger.debug(f"{ig=}, {threshold=}, {feature=}")

        # check the value of information gain is greater than 0 or not
        if ig > 0:
            # update the depth
            depth += 1

            # call make_partition() to split the data into two parts
            left, right = make_partition(data, feature, threshold)
            # print(left)
            # print(right)

            # If there is no data split to the left tree OR no data split to the right tree
            if left.empty or right.empty:
                # return the label of the majority
                label = int(data["hospital_death"].mode().iloc[0])
                return label
            else:
                question = "{} {} {}".format(feature, "<=", threshold)
                subtree = {question: []}

                # call function build_tree() to recursively build the left subtree and right subtree
                left_subtree = build_tree_advance(
                    left, max_depth, min_samples_split, depth, mp=mp
                )
                right_subtree = build_tree_advance(
                    right, max_depth, min_samples_split, depth, mp=mp
                )

                if left_subtree == right_subtree:
                    subtree = left_subtree
                else:
                    subtree[question].append(left_subtree)
                    subtree[question].append(right_subtree)
        else:
            # return the label of the majority
            label = int(data["hospital_death"].mode().iloc[0])
            return label
    else:
        # return the label of the majority
        label = int(data["hospital_death"].mode().iloc[0])
        return label

    return subtree


def build_forest(data, n_trees, n_features, n_samples, mp):
    """
    This function will build a random forest.
    args:
    * data: all data that can be used to train a random forest
    * n_trees: total number of tree
    * n_features: number of features
    * n_samples: number of instances
    return:
    * forest: a random forest with 'n_trees' of decision tree
    """

    global rng
    data_len = data.shape[0] - 1  # shihtl> label
    feature_list = data.columns[:-1]  # shihtl> label
    forest = []

    # shihtl> COMMENT before hand in <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    logger.info(data.columns)
    # shihtl> COMMENT before hand in >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Create 'n_trees' number of trees and store each into the 'forest' list
    for i in range(n_trees):
        logger.info(f"Start training {i}-th tree using this hyperparemeters.")

        # Select 'n_samples' number of samples and 'n_features' number of features
        # (you can select randomly or use any other techniques)

        selected_datas = rng.choice(data_len, size=n_samples, replace=False)
        selected_features = rng.choice(feature_list, size=n_features, replace=False)
        selected_features = np.append(selected_features, "hospital_death")

        # global_seed += 30  # shihtl> to avoid all tree are identical

        print(f"selected_datas = {selected_datas}")
        print(f"selected_datas = {len(selected_datas)}")
        print(f"selected_features = {selected_features}")
        # logger.info(f"Using features: {selected_features}")

        # Store the rows in 'selected_datas' from 'data' into a new DataFrame
        tree_data = pd.DataFrame(data, index=selected_datas, columns=selected_features)

        # Filter the DataFrame for specific 'selected_features' (columns)
        tree_data = tree_data[selected_features]

        # Then use the new data and 'build_tree' function to build a tree
        tree = build_tree_advance(tree_data, max_depth, min_samples_split, depth, mp=mp)
        logger.info(f"Done {i}-th tree: {tree}")

        # Save your tree
        forest.append(tree)

    return forest


def make_prediction_forest(forest, data):
    """
    This function will use the pre-trained random forest to make the predictions
    args:
    * forest: the random forest
    * data: the data used to predict
    return:
    * y_prediction: the predicted results
    """
    y_prediction = []
    predictions = []

    # Loop through each tree in the forest
    for tree in forest:
        # Call 'make_prediction'
        pred = make_prediction(tree, data)
        predictions.append(pred)

    predictions = pd.DataFrame(predictions)
    y_prediction = predictions.mode().values[0].tolist()

    return y_prediction


# shihtl> 效能測試
# if __name__ == "__main__":

#     lock = Manager().Lock()
#     pool = Pool(4)

#     logger.info("NOT MP start!")
#     start = time.perf_counter()
#     forest_no_mp = build_forest(training_data, n_trees, n_features, n_samples, mp=False)
#     end = time.perf_counter() - start
#     logger.info(f"NOT MP done! cost {end}")  # shihtl> 66.86024629999883 s

#     rng = np.random.default_rng(seed=SEED)

#     logger.info("MP start!")
#     start = time.perf_counter()
#     forest_mp = build_forest(training_data, n_trees, n_features, n_samples, mp=True)
#     end = time.perf_counter() - start
#     logger.info(f"MP done! cost {end}")  # shihtl> 26.650060900021344 s

#     logger.info(forest_no_mp)
#     logger.info(forest_mp)


if __name__ == "__main__":

    lock = Manager().Lock()
    pool = Pool(4)

    # {max_depth=}, {min_samples_split=}, {n_trees=}, {n_features=}, {sample_size=}, {SEED=}, {percentile_count=}
    l_max_depth = [8]
    l_min_samples_split = [500]
    l_n_trees = [17]
    l_n_features = [10]
    l_sample_size = [0.5]
    l_SEED = [48567108467]
    l_percentile_count = [33]

    for args in product(
        l_max_depth,
        l_min_samples_split,
        l_n_trees,
        l_n_features,
        l_sample_size,
        l_SEED,
        l_percentile_count,
    ):
        (
            max_depth,
            min_samples_split,
            n_trees,
            n_features,
            sample_size,
            SEED,
            percentile_count,
        ) = args

        n_samples = int(training_data.shape[0] * sample_size)

        PARAMS = f"{max_depth}_{min_samples_split}_{n_trees}_{n_features}_{sample_size}_{SEED}_{percentile_count}"
        PARAMS_PRINT = f"{max_depth=}, {min_samples_split=}, {n_trees=}, {n_features=}, {sample_size=}, {SEED=}, {percentile_count=}"

        logger.debug(">" * 120)
        logger.info(f"Starting {PARAMS_PRINT}")
        # rng = np.random.default_rng(seed=SEED)

        logger.info("MP start!")
        start = time.perf_counter()
        forest_mp = build_forest(training_data, n_trees, n_features, n_samples, mp=True)
        end = time.perf_counter() - start
        logger.info(f"MP done! cost {end} seconds.")

        logger.info(f"This forest: {forest_mp}")

        validation_data_x = validation_data.drop("hospital_death", axis=1)
        validation_data_y = validation_data[["hospital_death"]]

        pred_validation = make_prediction_forest(forest_mp, validation_data_x)
        logger.info(f"This predict res: {pred_validation}")
        score = calculate_score(validation_data_y, pred_validation)
        logger.info(f"This F1 Score: {score}")

        y_pred_test = make_prediction_forest(forest_mp, advanced_testing_data)

        advanced_path = "lab2_advanced.csv"
        advanced_path = f"./archive/lab2_advanced_{PARAMS}_{round(score, 10)}.csv"

        advanced_df = pd.DataFrame(
            {"Id": range(len(y_pred_test)), "hospital_death": y_pred_test}
        )
        advanced_df.set_index("Id", inplace=True)

        advanced_df.to_csv(advanced_path, header=True, index=True)

        with open(
            f"./archive/lab2_advanced_{PARAMS}_{round(score, 10)}.model",
            "w",
            encoding="utf-8",
        ) as file:
            file.write(str(forest_mp))
