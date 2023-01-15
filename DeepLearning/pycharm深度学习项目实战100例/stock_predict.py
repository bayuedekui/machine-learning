import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import tushare as ts


def get_data():
    # 调用tushare pro接口获取股票数据
    pro = ts.pro_api("c6b32ba214d901150d6fc0066c63d199f4fe94078202d605a0738134")

    df = pro.daily(ts_code='000001.SZ', start_date='20180701', end_date='20220718')

    print(df.info())


if __name__ == '__main__':
    get_data()



