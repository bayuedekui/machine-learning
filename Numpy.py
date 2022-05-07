import numpy as np

if __name__ == '__main__':
    dt4=np.datetime64('2022-05-07 22:10:34')
    print(dt4,type(dt4))

    range=np.arange('2022-05-01','2022-05-11',2,np.datetime64)
    print(range)

    out=[]
    for date,d in zip(range,np.diff(range)):
        #
        out.extend(np.arange(date,date+d))


    # print(np.diff(range))