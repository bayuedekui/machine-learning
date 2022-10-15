import pandas as pd
import numpy as np
import copy
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


def tvocs_rf_regression():
    df = pd.read_excel('tvocs_data.xlsx', sheet_name=1)
    print(df.head())

    head_name = df.columns
    for hn in head_name:
        if hn != 'time':
            df[hn].fillna(df[hn].mean(), inplace=True)
    print(df.shape[0])
    # 去除没有日期的
    df.dropna(axis=0, how='any', inplace=True)
    print(df.shape[0])

    x_train, y_train = df.iloc[:, 1:-1].values, df.iloc[:, -1].values

    rfg = RandomForestRegressor(n_estimators=200, oob_score=True, random_state=0)
    rfg.fit(x_train, y_train)

    # 打印特征重要性，并从高到底排列
    feature_imp = rfg.feature_importances_
    indices = np.argsort(feature_imp)[::-1]
    feature_name = df.columns[1:]
    for i in indices:
        print("%s:%f" % (feature_name[i], feature_imp[i]))

    # 画出回归预测图
    plt.figure(figsize=(20, 16))
    plt.scatter(df.iloc[:, 0], y_train, color='red')
    plt.plot(df.iloc[:, 0], rfg.predict(x_train), color='blue')
    plt.show()


if __name__ == '__main__':
    tvocs_rf_regression()
