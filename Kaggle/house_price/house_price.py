import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def get_data():
    train_df = pd.read_csv('input/train.csv', index_col=0)
    test_df = pd.read_csv('input/test.csv', index_col=0)
    print(train_df.head())
    print(train_df.info())
    print(train_df.shape)

    # 主要关注SalePrice,使用np.log1p函数进行数据的平滑化（对应解值使用expm1函数）
    prices = pd.DataFrame({"price": train_df["SalePrice"], "log(price+1)": np.log1p(train_df["SalePrice"])})
    # matplot中创建直方图函数
    print(prices.hist())
    plt.show()
    y_train = np.log1p(train_df.pop("SalePrice"))
    # 讲剩下的测试集和训练集合并起来
    all_df = pd.concat((train_df, test_df), axis=0)
    print(all_df.shape)

    print(y_train.head())


if __name__ == '__main__':
    get_data()
