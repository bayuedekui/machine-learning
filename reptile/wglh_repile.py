import pandas as pd
from selenium import webdriver  # 导入模块
import time
import csv  # 存储数据
from lxml import etree  # 数据的解析
import sys
import pymysql
from selenium.webdriver.common.by import By


def wglh_repile():
    # 进行webdriver一些初始化与配置
    options = webdriver.ChromeOptions()  # 网址获取
    # options.add_argument('--headless')  # 开启无界面模式
    # options.add_argument("--disable-gpu")  # 禁用gpu
    # options.add_argument('--user-agent=Mozilla/5.0 HAHA')  # 配置对象添加替换User-Agent的命令
    # options.add_argument('--window-size=1366,768')  # 设置浏览器分辨率（窗口大小）
    # options.add_argument('--start-maximized')  # 最大化运行（全屏窗口）,不设置，取元素会报错
    # options.add_argument('--disable-infobars')  # 禁用浏览器正在被自动化程序控制的提示
    # options.add_argument('--incognito')  # 隐身模式（无痕模式）
    # options.add_argument('--disable-javascript')  # 禁用javascript
    # options.add_argument(f"--proxy-server=http://115.239.102.149:4214")  # 使用代理
    # options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
    driver = webdriver.Chrome(options=options)

    # 请求具体网站
    driver.get('https://wglh.com/auth/login/')
    time.sleep(30)
    # driver.find_element(by=By.XPATH, value='//*[@id="btn_send_msg"]').click()
    # driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[2]/div[1]/button').click()

    # 获取页面源码,使用etree进行数据解析
    source = driver.page_source  # 获取页面源码
    my_tree = etree.HTML(source)  # 数据解析
    base_url = "https://wglh.com"

    # 数据解析
    t_body = my_tree.xpath('//*[@id="table1"]/tbody')
    t_header = my_tree.xpath('//*[@id="table1"]/thead')

    for i in range(len(t_header)):
        etf_header = []
        trs = t_header[i].xpath('.//tr')
        for tr in trs:
            line_header = []
            for th in tr:
                texts = th.xpath('.//text()')
                texts_arr = []
                for text in texts:
                    texts_arr.append(text.strip(""))
                line_header.append(",".join(texts_arr))

    line_header.append("ETF URL")
    print(line_header)

    for i in range(len(t_body)):
        etf_data = []
        etf_data.append(tuple(line_header))
        trs = t_body[i].xpath('.//tr')
        for tr in trs:
            line = []
            line_a = []
            for td in tr:
                texts = td.xpath(".//text()")  # 取出所有td标签下的文本
                a_links = td.xpath(".//a/@href")
                text_arr = []
                if len(a_links) != 0:
                    line_a.append(base_url + a_links[0])
                for text in texts:
                    text_arr.append(text.strip(""))  # 字符删除尾部空格和换行符

                line.append(','.join(text_arr))
            line.append(','.join(line_a))
            etf_data.append(tuple(line))
        print(etf_data)

    df = pd.DataFrame(etf_data[1:], columns=etf_data[0])
    df.to_csv("etf_data.csv", index=0, header=True, encoding='utf_8_sig')
    print(df)


if __name__ == '__main__':
    wglh_repile()
