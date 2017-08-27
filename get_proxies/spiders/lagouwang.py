from scrapy.spiders import Spider
from scrapy.spiders import CrawlSpider
from scrapy import Request
from scrapy.http import FormRequest,HtmlResponse
from get_proxies.spiders.urls import Urls
from get_proxies.spiders.urls import UserAgent
from scrapy.selector import Selector,HtmlXPathSelector
from selenium import webdriver
class LaGouWang(Spider):
    name = 'lagouwang'
    # allowed_domains = ["www.lagou.com"]
    start_url='https://www.lagou.com'

    #all catagory urls
    urls=Urls.lagouwang_urls
    #first,we get all jobs' urls in a category
    item_urls=[]
    cate=0

    header=UserAgent().getUserAgent()
    def start_requests(self):
        #login
        yield Request(self.urls[self.cate],headers=self.header,callback=self.parse)



    def parse(self, response):
        sel=Selector(response)

        #each job urls in one page
        each_jos_urls=sel.xpath('//*[@id="s_position_list"]/ul/li/div/div[1]/div/a/@href').extract()
        for url in each_jos_urls:
            self.item_urls.append(url)


        next_page=sel.xpath('//*[@id="s_position_list"]/div[2]/div/a')[-1].xpath('./@href').extract()
        print(next_page)
        if 'www.lagou.com' in next_page[0]:
            return Request(url=next_page[0],headers=self.header,callback=self.parse)
        else:
            self.cate=self.cate+1
            return Request(url=self.urls[self.cate],headers=self.header,callback=self.parse)

