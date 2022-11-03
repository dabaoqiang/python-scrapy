import scrapy

from ..items import TxmoviesItem


class TxmsSpider(scrapy.Spider):

    # name = 'txms'
    # allowed_domains = ['v.qq.com']
    # start_urls = ['https://v.qq.com/x/bu/pagesheet/list?append=1&channel=cartoon&iarea=1&listpage=2&offset=0&pagesize=30']
    # offset = 0
    #
    # def parse(self, response):
    #     items = TxmoviesItem()
    #     lists = response.xpath('//div[@class="list_item"]')
    #     for i in lists:
    #         items['name'] = i.xpath('./a/@title').get()
    #         items['description'] = i.xpath('./div/div/@title').get()
    #         # 在本程序中，我们对item封装数据后，就调用yield把控制权给管道，管道拿到处理后return返回，又回到该程序
    #         yield items
    #
    #     if self.offset < 120:
    #         self.offset += 30
    #         url = 'https://v.qq.com/x/bu/pagesheet/list?append=1&channel=cartoon&iarea=1&listpage=2&offset={}&pagesize=30'.format(
    #             str(self.offset))
    #         # 这条程序里利用了一个回调机制，即callback,回调的对象是parse,也就是当前方法，通过不断的回调，程序将陷入循环，
    #         # 如果不给程序加条件，就会陷入死循环，如本程序我把if去掉，那就是死循环了
    #         yield scrapy.Request(url=url, callback=self.parse)

        name = 'txms'
        allowed_domains = ['v.qq.com']
        url = 'https://v.qq.com/x/bu/pagesheet/list?append=1&channel=cartoon&iarea=1&listpage=2&offset={}&pagesize=30'
        offset = 0

        def start_requests(self):
            for i in range(0, 121, 30):
                url = self.url.format(i)
                yield scrapy.Request(
                    url=url,
                    callback=self.parse
                )

        def parse(self, response):
            items = TxmoviesItem()
            lists = response.xpath('//div[@class="list_item"]')
            for i in lists:
                items['name'] = i.xpath('./a/@title').get()
                items['description'] = i.xpath('./div/div/@title').get()

                yield items
