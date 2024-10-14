import numpy as np
import pandas as pd
import math
import random
from numpy import sqrt
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score


# print(math.log2(0))
seed = 381514
rng = np.random.default_rng(seed=seed)

for i in range(5):
    print(rng.choice(20, size=20, replace=False))

with open("testtt.model", "w", encoding="utf-8") as file:
    file.write(
        str([{"fdhalf": ["fdhlasf", 3]}, {"fdhalf": [{"fduahlguh": [0, 1]}, 0]}])
    )


# shihtl> COMMENT before hand in <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
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

    best_ig = -1e9
    best_threshold = 0
    best_feature = ""

    def process(feature, percent, lock):
        nonlocal best_ig, best_threshold, best_feature

        data_size = data.shape[0]
        this_data = data.sort_values(feature)

        split_idx = min(
            data_size - 2, math.floor(data_size * percent * percentile_each)
        )
        # print(split_idx)

        if this_data.iloc[split_idx][feature] == this_data.iloc[split_idx + 1][feature]:
            return 0, 0, 0

        this_threshold = (
            this_data.iloc[split_idx][feature] + this_data.iloc[split_idx + 1][feature]
        ) / 2
        this_mask = data[feature] <= this_threshold
        this_ig = information_gain(data, this_mask)

        # shihtl> find max ig
        # shihtl> sync need a lock
        with lock:
            if this_ig > best_ig:
                best_ig, best_threshold, best_feature = (
                    this_ig,
                    this_threshold,
                    feature,
                )

    from multiprocessing import Lock, Pool
    from itertools import product

    lock = Lock()
    pool = Pool(4)

    input_product = product(data.columns[:-1], range(percentile_count), [lock])
    pool.map(process, input_product)

    best_ig = round(best_ig, 4)

    return best_ig, best_threshold, best_feature

    # shihtl> COMMENT before hand in >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # check the condition of current depth and the remaining number of samples
    if depth < max_depth and data.shape[0] > min_samples_split:
        # call find_best_split_advance() to find the best combination
        ig, threshold, feature = find_best_split_advance(data)

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
                    left, max_depth, min_samples_split, depth
                )
                right_subtree = build_tree_advance(
                    right, max_depth, min_samples_split, depth
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

    # check the condition of current depth and the remaining number of samples
    if depth < max_depth and data.shape[0] > min_samples_split:
        # call find_best_split_advance() to find the best combination
        ig, threshold, feature = find_best_split_advance(data)

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
                    left, max_depth, min_samples_split, depth
                )
                right_subtree = build_tree_advance(
                    right, max_depth, min_samples_split, depth
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
