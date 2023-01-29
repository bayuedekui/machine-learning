import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score


def get_data():
    data_train = pd.read_csv('input/train.csv')
    data_test = pd.read_csv('input/test.csv')
    # 查看数据分布情况，空值情况
    print(data_test.info())

    # 分离特征和结果,分别处理测试数据和训练数据
    data_x_train = data_train.iloc[:, 1:-1]
    data_x_test = data_test.iloc[:, 1:]

    y_train = data_train.iloc[:, -1].apply(lambda x: 1 if x == 'yes' else 0)

    # 进行标准化
    x_train = standardized_features(data_x_train)
    x_test = standardized_features(data_x_test)
    print(x_train)
    print(x_test)

    # 分离测试数据和训练数据
    xgb = XGBClassifier()
    xgb.fit(x_train, y_train)
    y_predict = xgb.predict(x_test)
    # print(y_predict)
    # print(len(y_predict))
    y_predict_id = data_test.id.values
    print(y_predict_id)
    # 先构造二维数据，然后转化为dataframe

    arr = np.hstack((y_predict_id.reshape(-1, 1), y_predict.reshape(-1, 1)))
    # for i in range(len(y_predict)):
    # print(y_predict_id[i])
    # print(y_predict[i])
    res = pd.DataFrame(arr, columns=['id', 'subscribe'])
    res['subscribe'] = res.iloc[:, -1].apply(lambda x: 'yes' if x == 1 else 'no')

    res.to_csv(
        'D:\\EEEEEEEEEEEEEEEEEEEEEEEEEEEE\\PythonProjects\\machine-learning\\tianchi\\金融数据分析赛题1：银行客户认购产品预测\\input\submission.csv',
        index=False)

    print(res)


def standardized_features(features):
    # 进行get_dummies是针对object变成uint8,所以在之前就要取非object列出来
    numeric_col = features.columns[features.dtypes != 'object']
    features = pd.get_dummies(features)
    # 取数字行的进行求均值
    numeric_mean = features[numeric_col].mean()
    # 取数字行的进行求方差
    numeric_std = features[numeric_col].std()
    # 减均值除以方差
    features[numeric_col] = (features[numeric_col] - numeric_mean) / numeric_std

    return features


if __name__ == '__main__':
    get_data()
