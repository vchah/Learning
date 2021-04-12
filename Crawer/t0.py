# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import re
import requests
import xlwt
import csv
import time

#保持登录

#1 爬取网页
def getData(url):
    datelist = []
    return datalist

# 爬取指定单个网页
def askURL(url):
    head ={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
        'ContentType': 'text/html; charset=utf-8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
    }
    res = requests.get(url, headers = head).text
    return res

#解析数据
def htmlAnalysis(file,html):
    bs = BeautifulSoup(html,"html.parser")
    soup = bs.find_all(attrs={"data-lj_action_source_type":"链家_PC_二手列表页卡片"})
    fangInfo={}
    for fang in soup:
        print("第", fang.attrs['data-lj_action_click_position'], "条数据：")
        fangInfo["ID"] = fang.attrs['data-lj_action_housedel_id']
        fangInfo["标题"] = fang.contents[1].contents[0].text
        fangInfo["街道"] = fang.contents[1].contents[1].text.split('-')[0]
        fangInfo["商圈"] = fang.contents[1].contents[1].text.split('-')[1]
        fangInfo["户型介绍"] = fang.contents[1].contents[2].text
        fangInfo["关注\发布"] = fang.contents[1].contents[3].text
        fangInfo["标签"] = fang.contents[1].contents[4].text
        fangInfo["总价"] = fang.contents[1].contents[5].text.split('单价')[0]
        fangInfo["单价"] = fang.contents[1].contents[5].text.split('单价')[1]
        csv_writer = csv.DictWriter(file,fieldnames=['ID', '标题', '街道', '商圈', '户型介绍', '关注\发布', '标签', '总价', '单价'])
        csv_writer.writerow(fangInfo)
    return fangInfo

def main():
    # 获取数据
    # testurl = "https://movie.douban.com/top250?start=0"
    # datalist = getData(testurl)
    # askURL(testurl)
    f = open('D:\Code\Python\LianjiaCrawer\Crawer\哈尔滨二手房信息.csv', mode='a', encoding='utf-8-sig', newline='')
    csv_writer = csv.DictWriter(f, fieldnames=['ID', '标题', '街道', '商圈', '户型介绍', '关注\发布', '标签', '总价', '单价'])
    csv_writer.writeheader()

    for pg in range(0,101):
        aimurl = "https://hrb.lianjia.com/ershoufang/pg{}".format(pg)
        time.sleep(5)
        print('===========================正在下载第{}页数据================================'.format(pg))
        response = askURL(aimurl)
        # 解析数据
        info = htmlAnalysis(f,response)

    f.close()
    # 保存数据
    # aim_savpath = ".\\链家.xlsx"
    # test_savpath = ".\\top250.xlsx"
    # saveData(test_savpath)
    


if __name__ == "__main__":
    main()
 