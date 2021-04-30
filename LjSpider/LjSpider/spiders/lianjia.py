# -*- coding:utf-8 -*-

import json
import scrapy
import logging
import re
from bs4 import BeautifulSoup
from LjSpider.settings import table
from LjSpider.items import LjspiderItem


class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    base_url = 'http://hrb.lianjia.com/ershoufang/'

    def start_requests(self):
        district = ['pingfang','daowai','daoli','nangang','xiangfang','shangzhishi','bayanqu',
                    'hulanqu','achengqu','yanshouxian','yilanxian','mulanxian','binxian','tonghexian',
                    'wuchangshi','shuangchengqu','fangzhengxian','zhaodongshi2']
        for region in district:
            region_url = self.base_url + region
            yield scrapy.Request(url=region_url, callback=self.page_navigate)
            # break

    def page_navigate(self, response):
        soup = BeautifulSoup(response.body, "html.parser")
        try:
            pages = soup.find_all("div", class_="house-lst-page-box")[0]
            if pages:
                dict_number = json.loads(pages["page-data"])
                max_number = dict_number['totalPage']
                for num in range(1, max_number + 1):
                    url = response.url + 'pg' + str(num) + '/'
                    yield scrapy.Request(url=url, callback=self.parse)
                    # break
        except:
            logging.info("*******该地区没有二手房信息********")

    def parse(self, response):
        item = LjspiderItem()
        soup = BeautifulSoup(response.body, "html.parser")

        #获取到所有子列表的信息
        house_info_list = soup.find_all(name="li", class_="clear")

        # 通过url辨认所在区域
        url = response.url
        url = url.split('/')
        item['Region'] = table[url[-3]]

        for info in house_info_list:
            item['Id'] = info.a['data-housecode']
            house_info_title = info.find_all(name='div', class_ = 'title')[0]
            house_info_title = house_info_title.get_text()
            item['Title'] = house_info_title
            house_info = info.find_all(name="div", class_="houseInfo")[0]
            house_info = house_info.get_text()
            house_info = house_info.replace(' ', '')
            house_info = house_info.split('|')
            # print(item['Region'])
            # print(house_info)
            try:
                item['Layout'] = house_info[0]
                item['Size'] = house_info[1]
                item['Direction'] = house_info[2]
                item['Renovation'] = house_info[3]
                item['Height'] = house_info[4]
                item['Floor'] = house_info[4]
                item['Construction'] = house_info[5]
                print(item)
            except:
                print("房屋数据保存错误")

            position_info = info.find_all(name='div', class_='positionInfo')[0]
            position_info_a = position_info.find_all("a")
            try:
                item['Garden'] = position_info_a[0].get_text().replace(' ', '')
                item['District'] = position_info_a[1].get_text().replace(' ', '')
            except:
                print("区域数据保存错误")

            price_info = info.find_all("div", class_="totalPrice")[0]
            item['Price'] = price_info.span.get_text()
            unitprice_info = info.find_all("div", class_="unitPrice")[0]
            item['UnitPrice'] = unitprice_info.span.get_text()

            Tag = info.find_all("div", class_ = "tag")[0]
            SubwayTag = Tag.find_all("span", class_ = "subway")
            if  SubwayTag:
                item["Subway"] = "是"
            else:
                item["Subway"] = "否"
            TaxFreeTag = Tag.find_all("span", class_="taxfree")
            if  TaxFreeTag:
                item["Taxfree"] = "是"
            else:
                item["Taxfree"] = "否"
            # print(item["Subway"])
            # break

            yield item