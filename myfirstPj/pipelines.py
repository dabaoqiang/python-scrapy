# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MyfirstpjPipeline:
    def process_item(self, item, spider):
        return item


class BaiduMysqlPipeline:

    def process_item(self, item, spider):
        return item

class TxmoviesPipeline:

    def process_item(self, item, spider):
        print(item)
        return item