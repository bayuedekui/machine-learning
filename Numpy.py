import numpy as np


def yestoday_today_tomorrow():
    yestoday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
    today = np.datetime64('today', 'D')
    tomorrow = np.datetime64('today', 'D') + np.timedelta64(1, 'D')
    print(yestoday)
    print(today)
    print(tomorrow)


def creat_default_arr():
    arr = np.full([3, 3], True, dtype=np.bool_)
    print(arr)
    defaultArr = np.zeros(10)
    defaultArr[4] = 1
    print(defaultArr)

    # 创建一个值域范围从10到49的向量
    rangeArr = np.arange(10, 50)
    print(rangeArr)

    # 创建一个 3x3x3的随机数组
    randomArr = np.random.random((3, 3, 3))
    print(randomArr)

    # 创建一个二维数组，其中边界值为1，其余值为0
    zeroArr = np.ones((10, 10))
    zeroArr[1: -1, 1: -1] = 0
    print(zeroArr)

    # 创建长度为10的numpy数组，从5开始，在连续的数字之间的步长为3。
    pointArr = np.arange(5, 5 + 3 * 10, 3)
    print(pointArr)


def index_slice_2():
    colArr = np.arange(9).reshape((3, 3))
    print(colArr)

    # 交换第一列和第三列
    colChgArr = colArr[:, [2, 1, 0]]
    print(colChgArr)
    # 交换第一行和第三行
    rowChgArr = colArr[[2, 1, 0], :]
    print(rowChgArr)

    # 反转数组
    arr = np.arange(16).reshape((4, 4))
    print(arr)
    reverseArr = arr[::-1, ::-1]
    print(reverseArr)


def changeArr():
    # 将arr转换为2行的2维数组。
    arr = np.arange(10)

    arr1 = arr.reshape((2, 5))
    print(arr1)
    arr2 = arr.reshape((2, -1))
    print(arr2)

    print()

    a = np.arange(10).reshape((2, -1))
    b = np.repeat(1, 10).reshape((2, -1))
    print(a)
    print()
    print(b)
    # 垂直叠加两个数组
    c = np.vstack([a, b])
    # 水平叠加两个数组
    d = np.hstack([a, b])
    print(c)
    print()
    print(d)

    # 将 arr的2维数组按列输出。
    arr3 = np.array(
        [[16, 17, 18, 19, 20], [11, 12, 13, 14, 15], [21, 22, 23, 24, 25], [31, 32, 33, 34, 35], [26, 27, 28, 29, 30]])
    arr4 = arr3.flatten(order="F")
    print(arr3)
    print(arr4)

    # 给定两个随机数组A和B，验证它们是否相等。
    arr5 = np.array([1, 2, 3])
    arr6 = np.array([1, 2, 3])
    equal1 = np.allclose(arr5, arr6)
    equal2 = np.array_equal(arr5, arr6)
    print(equal1)
    print(equal2)

    arr6 = np.random.randint(0, 5, 10)
    print(arr6)
    arr7 = np.full(10, True)
    print(arr7)
    # 如何在numpy数组中找到重复值？
    vals, counts = np.unique(arr6, return_index=True)
    print(vals)
    print(counts)
    arr7[counts] = False
    print(arr7)

    # 建立一个随机数在1-10之间的3行2列的数组，并将其转换成2行3列的数组。
    arr8 = np.random.randint(10, size=[3, 2])
    print(arr8)
    arr9 = arr8.reshape([2, 3])
    print(arr9)


if __name__ == '__main__':
    # dt4 = np.datetime64('2022-05-07 22:10:34')
    # print(dt4, type(dt4))
    #
    # range = np.arange('2022-05-01', '2022-05-10', 2, np.datetime64)
    # print(range)
    #
    # out = []
    # for date, d in zip(range, np.diff(range)):
    #     # zip将range和np.diff()组合成一个元组，已长度短的那个为主
    #     out.extend(np.arange(date, date + d))
    #
    # print(out)
    # # 转化为numpy的array
    # nparr = np.array(out)
    # #  补充2022-5-11这个日期
    # seriesRes = np.hstack([nparr, range[-1]])
    # print(seriesRes)
    # yestoday_today_tomorrow()
    # creat_default_arr()
    # index_slice_2()
    changeArr()
