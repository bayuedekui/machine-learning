import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split


def plot_iris_data_distribute():
    iris = load_iris()
    iris_df = pd.DataFrame(iris['data'], columns=['Sepal_Lenght', 'Sepal_Width', 'Petal_Length', 'Petal_Width'])
    iris_df['Species'] = iris.target
    print(iris_df)
    plot_iris(iris_df, 'Petal_Length', 'Petal_Width')


# 画图
def plot_iris(iris, col1, col2):
    sns.lmplot(x=col1, y=col2, data=iris, hue='Species', fit_reg=False)
    plt.xlabel(col1)
    plt.ylabel(col2)
    plt.title("鸢尾花种类分类图")
    plt.show()


def preprocessing_minmaxscalar():
    data = pd.read_csv('dataing.txt')
    print(data)
    # 1、实列化一个转化器类,feature_range=(2, 3) 指定范围，默认feature_range=(0, 1),将数据归一化到2-3之间
    transfer = MinMaxScaler(feature_range=(2, 3))

    # 2、调用fit_transform,初始归一化数据
    data = transfer.fit_transform(data[['milage', 'Liters', 'Consumtime']])
    print(data)


def preprocessing_standardscaler():
    data = pd.read_csv('dataing.txt')
    print("原数据：", data)

    transfer = StandardScaler()
    data = transfer.fit_transform(data[['milage', 'Liters', 'Consumtime']])
    print("标准化数据：", data)
    print("均值：", transfer.mean_)
    print("方差：", transfer.var_)


def knnc():
    iris = load_iris()
    # 1、构造训练集和测试集
    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=0)

    # 2、标准化数据
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.fit_transform(x_test)
    print("标准化训练值：", x_train)
    print("标准化测试值：", x_test)

    # 3、机器学习，模型训练
    estimator = KNeighborsClassifier(n_neighbors=9)
    estimator.fit(x_train, y_train)

    # 4、模型评估
    # 4.1 方法1、比对真实值和测试值
    y_predict = estimator.predict(x_test)
    print("预测结果为：", y_predict)
    print("真实结果为：", y_test)

    # 4.2 方法2、直接计算准去率
    print("准确率为：", estimator.score(x_test, y_test))


if __name__ == '__main__':
    # plot_iris_data_distribute()
    knnc()
