"""
1.获取数据
2.数据基本处理
    2.1 确定特征值,⽬标值
    2.2 缺失值处理
    2.3 数据集划分
3.特征⼯程(字典特征抽取)
4.机器学习(决策树)
5.模型评估
"""

import pandas as pd
import numpy as np
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_graphviz


def predict_alive():
    # 1、获取数据
    titan = pd.read_csv("C:\\Users\\zhengkui\\Desktop\\tested.csv")
    # print(titan.head())

    # 2、确定特征值，目标值
    x = titan[["Pclass", "Age", "Sex"]]
    y = titan[["Survived"]]

    # print(y.head())

    # 3、缺失值处理，这块虽然报警告，但是不影响赋值
    x["Age"].fillna(x["Age"].mean(), inplace=True)
    # print(x.head(20))

    # 4、数据集划分
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=22)

    # 5、特征工程（字典特征抽取），特征中出现类别符号，需要进行one-hot编码处理（DictVectorizer）
    # print(x_train.head())
    # print(y_train.head())

    # 6、机器学习（决策树）
    transfer = DictVectorizer(sparse=False)

    x_train = transfer.fit_transform(x_train.to_dict(orient="records"))
    # print(x_train)
    x_test = transfer.fit_transform(x_test.to_dict(orient="records"))
    # print(x_test.head())

    estimator = DecisionTreeClassifier()
    estimator.fit(x_train, y_train)

    # 7、模型评估
    score = estimator.score(x_test, y_test)
    print(score)

    # 8、测试集进行预测
    res = estimator.predict(x_test)
    print(res)


if __name__ == '__main__':
    predict_alive()
