import copy
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


def geni_importances():
    df = pd.read_csv('wine.data', header=None)
    df.columns = ['Class label', 'Alcohol', 'Malic acid', 'Ash',
                  'Alcalinity of ash', 'Magnesium', 'Total phenols',
                  'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins',
                  'Color intensity', 'Hue', 'OD280/OD315 of diluted wines', 'Proline']
    x, y = df.iloc[:, 1:].values, df.iloc[:, 0].values
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
    feat_labels = df.columns[1:]
    forest = RandomForestClassifier(n_estimators=10000, random_state=0, n_jobs=-1)
    forest.fit(x_train, y_train)

    importances = forest.feature_importances_
    indices = np.argsort(importances)[::-1]
    for f in range(x_train.shape[1]):
        print("%2d) %-*s %f" % (f + 1, 30, feat_labels[indices[f]], importances[indices[f]]))


def oob_importances():
    df = pd.read_csv('wine.data', header=None)
    df.columns = ['Class label', 'Alcohol', 'Malic acid', 'Ash',
                  'Alcalinity of ash', 'Magnesium', 'Total phenols',
                  'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins',
                  'Color intensity', 'Hue', 'OD280/OD315 of diluted wines', 'Proline']
    x, y = df.iloc[:, 1:].values, df.iloc[:, 0].values

    rf = RandomForestClassifier(n_estimators=200, oob_score=True)
    rf.fit(x, y)
    print("原样数据准确率==》%f" % rf.oob_score_)

    for i in range(len(df.columns) - 1):
        tmp_df = copy.deepcopy(df)
        tmp_df[df.columns[i + 1]] = 1.1
        tmp_x = tmp_df.iloc[:, 1:]
        rf.fit(tmp_x, y)
        print("%s取随机值准确率==》%f" % (df.columns[i + 1], rf.oob_score_))


def use_oob(x_train, y_train, features_name, features_imp, select_num, rf):
    oob_result = []
    fea_result = []
    features_imp = list(features_imp)

    features_test = copy.deepcopy(features_imp)  # 生成一个排序特征，进行筛选
    features_test.sort()
    features_test.reverse()

    train_index = [features_imp.index(j) for j in features_test[:select_num]]
    print(train_index)
    train_feature_name = [features_name[k] for k in train_index]
    train_data = x_train[:, train_index]

    rf.fit(train_data, y_train)
    acc = rf.oob_score_
    print("%s ==> %f" % (train_feature_name, acc))
    oob_result.append(acc)
    fea_result.append(train_index)

    return max(oob_result), oob_result, fea_result[oob_result.index(max(oob_result))]


if __name__ == '__main__':
    oob_importances()
    # features_name = ['Alcohol', 'Malic acid', 'Ash',
    #                  'Alcalinity of ash', 'Magnesium', 'Total phenols',
    #                  'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins',
    #                  'Color intensity', 'Hue', 'OD280/OD315 of diluted wines', 'Proline']
    # print(len(features_name))
