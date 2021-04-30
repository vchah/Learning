# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LjspiderItem(scrapy.Item):
    # define the fields for your item here like:
    Id = scrapy.Field()
    #区域
    Region = scrapy.Field()
    #小区
    Garden = scrapy.Field()
    #户型
    Layout = scrapy.Field()
    #面积
    Size = scrapy.Field()
    #朝向
    Direction = scrapy.Field()
    #装修
    Renovation = scrapy.Field()
    #楼层高度
    Height = scrapy.Field()
    #楼层
    Floor = scrapy.Field()
    #建筑
    Construction = scrapy.Field()
    #总价
    Price = scrapy.Field()
    #单价
    UnitPrice = scrapy.Field()
    #住宅位置
    District = scrapy.Field()
    #是否靠近地铁
    Subway = scrapy.Field()
    #房本是否满五年
    Taxfree = scrapy.Field()
    #标题
    Title = scrapy.Field()
    