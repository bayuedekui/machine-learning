# coding=utf-8
from __future__ import print_function, absolute_import
from gm.api import *

if __name__ == '__main__':
    # 可以直接提取数据，掘金终端需要打开，接口取数是通过网络请求的方式，效率一般，行情数据可通过subscribe订阅方式
    # 设置token， 查看已有token ID,在用户-秘钥管理里获取
    set_token('68c65e8543228c82bce877e60100190047011f1b')

    # 查询历史行情, 采用定点复权的方式， adjust指定前复权，adjust_end_time指定复权时间点
    # data = history(symbol='SHSE.600000', frequency='1d', start_time='2020-01-01 09:00:00',
    #                end_time='2020-12-31 16:00:00',
    #                fields='open,high,low,close', adjust=ADJUST_PREV, adjust_end_time='2020-12-31', df=True)
    # print(data)

    # 查询个股股票交易行情衍生的财务数据trading_derivative_indicator，主要就是PE
    # stock_data = get_fundamentals(table='trading_derivative_indicator', symbols='SHSE.600000',
    #                               start_date='2023-03-31',
    #                               end_date='2023-03-31',
    #                               fields='NEGOTIABLEMV,PETTM',
    #                               df=True)
    # print(stock_data)

    # 获取指数：中证红利SHSE.000922 对应成分股以及权重
    # point = get_constituents(index='SHSE.000922', fields='symbol, weight', df=True)
    # print(point)

    stocks = get_constituents(index='SHSE.000922', fields='symbol,weight', df=True)
    # print(stocks)
    total_pettm = 0
    for idx, row in stocks.iterrows():
        stock_pettm = get_fundamentals(table='trading_derivative_indicator', symbols=row.symbol,
                                       start_date='2023-03-31',
                                       end_date='2023-03-31',
                                       fields='NEGOTIABLEMV,PETTM',
                                       df=True)
        for s_idx,s_row in stock_pettm.iterrows():
            print("单个股票pe:", s_row.PETTM)
            print("单个股票权重:", row.weight)
            print("单个股票占比:", s_row.PETTM * row.weight)
            total_pettm += s_row.PETTM * row.weight * 0.01




    print("指数pe:{.4f}", total_pettm)
