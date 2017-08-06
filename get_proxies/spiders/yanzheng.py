from scrapy.spider import Spider
from scrapy import Request
from scrapy.selector import Selector
class yanzheng(Spider):
    i=0
    name = 'yanzheng'
    headers={
        'header':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }
    def start_requests(self):
        url='https://www.bilibili.com/'
        yield Request(url,headers=self.headers)

    def parse(self, response):
        result=Selector(response)
        title=result.xpath('/html/head/title/text()')
        print(title)
        self.i=self.i+1
        print('di %d ci:' % self.i)

