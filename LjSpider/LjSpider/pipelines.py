# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import re

class LjspiderPipeline:
    def process_item(self, item, spider):
        size = item['Size']
        unitPrice = item['UnitPrice']
        high = item['Height']
        floor = item['Floor']

        item['Size'] = float(re.findall(r'([1-9][0-9]*|0)(\.[0-9]+)?', size)[0])
        item['UnitPrice'] = float(re.findall(r'[1-9]+\.?[0-9]*', unitPrice)[0])
        item['Height'] = re.findall(r'.*?\(.(\d*).\).*?', high)[0]
        item['Floor'] = re.findall(r'.+(?=[(])', floor)[0]
        return item