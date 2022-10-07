from selenium import webdriver  # 导入模块
import time
import csv  # 存储数据
from lxml import etree  # 数据的解析
import sys
import pymysql


def reptile():
    option = webdriver.ChromeOptions()  # 网址获取
    option.add_argument('headless')  # 设置浏览器静默
    driver = webdriver.Chrome(options=option)
    driver.get('https://data.eastmoney.com/bbsj/yjbb/600519.html')
    time.sleep(2)

    source = driver.page_source  # 获取页面源码
    mytree = etree.HTML(source)  # 数据解析
    print(mytree)

    tbody = mytree.xpath('//*[@id="dataview"]/div[2]/div[2]/table/tbody')  # 定位表格

    pages = mytree.xpath('//*[@id="dataview"]/div[3]/div[1]/a')

    print(pages)

    stock_id = '600519'
    stock_name = '贵州茅台'

    for i in range(len(tbody)):  # 循环表格
        stockDatas = []
        trs = tbody[i].xpath('.//tr')  # 取出所有tr标签
        print(len(trs))
        for tr in trs:
            line = []
            line.append(stock_id)
            line.append(stock_name)
            for td in tr:
                texts = td.xpath(".//text()")  # 取出所有td标签下的文本
                text_arr = []
                for text in texts:
                    text_arr.append(text.strip(""))  # 字符删除尾部空格和换行符
                line.append(','.join(text_arr))
            print(line)
            stockDatas.append(line)  # 整张表格

        # 保存到csv文件
        with open('data.csv', 'a', newline='') as file:  # 将数据写入文件
            csv_file = csv.writer(file)
            for i in stockDatas:
                csv_file.writerow(i)

    time.sleep(2)
    driver.close()


# 抽象抽取方法，每获取一页数据则存入一页的数据

def repile_page(stockId, stockName):
    # 网址获取
    option = webdriver.ChromeOptions()
    # 设置浏览器静默
    option.add_argument('headless')
    driver = webdriver.Chrome(options=option)
    driver.get('https://data.eastmoney.com/bbsj/yjbb/600519.html')
    time.sleep(2)

    source = driver.page_source  # 获取页面源码
    mytree = etree.HTML(source)  # 数据解析

    # 定位表格
    tbody = mytree.xpath('//*[@id="dataview"]/div[2]/div[2]/table/tbody')
    print("tbody长度为：%d" % len(tbody))

    for i in range(len(tbody)):  # 循环表格
        stockDatas = []
        trs = tbody[i].xpath('.//tr')  # 取出所有tr标签
        for tr in trs:
            line = []
            line.append(stockId)
            line.append(stockName)
            for td in tr:
                texts = td.xpath(".//text()")  # 取出所有td标签下的文本
                text_arr = []
                for text in texts:
                    text_arr.append(text.strip(""))  # 字符删除尾部空格和换行符
                line.append(','.join(text_arr))
            stockDatas.append(tuple(line))  # 整张表格
        print(stockDatas)
        insert_sql = 'insert into t_stock_finance(stock_id,stock_name,report_time,earnings,earnings_deducted,total_operating_income,income_yoy_growth,income_qoq_growth,net_profit,profit_yoy_growth,profit_qoq_growth,net_assets,return_on_equity,operating_cash,gross_profit,profit_distribution,dividend_yield,first_report,latest_report) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        save(insert_sql, stockDatas)


# 抓取股票id与名称信息存入数据库
def repitle_stock_info():
    # 网址获取
    option = webdriver.ChromeOptions()
    # 设置浏览器静默
    option.add_argument('headless')
    driver = webdriver.Chrome(options=option)
    driver.get('http://www.shdjt.com/flsort.asp?lb=sh000016')
    # 获取网页源代码
    source = driver.page_source
    pageHtml = etree.HTML(source)

    tbody = pageHtml.xpath('//*[@id="senfe"]/tbody')
    stock_type = pageHtml.xpath('//*[@id="table1"]/tbody/tr[1]/td/b[1]/text()')[1]
    print(stock_type)

    for i in range(len(tbody)):
        stockInfos = []
        trs = tbody[i].xpath('.//tr')
        for k in range(len(trs)):
            if k >= len(trs) - 2:
                break
            line = []
            tds = []
            for j in range(len(trs[k])):
                if j == 1 or j == 2 or j == 3 or j == 6 or j == 7:
                    texts = trs[k][j].xpath('.//text()')
                    tds.append(texts[0])
                elif j > 7:
                    break
            tds.append(stock_type)
            line.append(','.join(tds))
            stockInfos.append(tuple(line))
        print(stockInfos)


# 将数据存入数据库中
def save(sql, contents):
    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='123456',
        database='stock'
    )
    # 建立游标
    try:
        cursor = conn.cursor()
        for i in range(len(contents)):
            cursor.execute(sql, contents[i])
        conn.commit()
    except Exception as e:
        conn.rollback()
        print("sava data failed:", e)

    print('')


if __name__ == '__main__':
    # reptile()
    # repile_page('600519', '贵州茅台')
    repitle_stock_info()
