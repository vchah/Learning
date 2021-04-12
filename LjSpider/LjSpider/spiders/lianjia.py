import scrapy


class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['hrb.lianjia.com']
    start_urls = ['http://hrb.lianjia.com/xiaoqu/']

    def parse(self, response):
        filename = "ershoufang.html"
        open(filename,'wb').write(response.body)
