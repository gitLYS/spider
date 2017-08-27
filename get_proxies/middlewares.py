# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random
from mysql import connector as cnn
from bs4 import BeautifulSoup
from get_proxies.settings import HTTP_PROXY
from get_proxies.get_ip import GetIp
import requests
import os

class GetProxiesSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod

    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(start_requests, spider):

        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)



class TorProxyMiddleWare(object):
    def process_request(self,request,spider):
        request.meta['proxy']=HTTP_PROXY  #使用tor做代理


class XiciProxyMiddleWare(object):
    def process_request(self,request,spider):
       header={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
        }
       file_name='/home/lys/project/get_proxies/get_proxies/代理ip.txt'
       with open(file_name,'r') as f:
           proxies=f.readlines()

       err_time=0
       while True:
           proxy=random.choice(proxies).strip()
           proxy_http={'http':proxy}
           s=requests.get('https://www.lagou.com/',headers=header,proxies=proxy_http)
           print([BeautifulSoup(s.text,'lxml').h1.text])
           print('correct:'+proxy)
           if BeautifulSoup(s.text,'lxml').h1.text.strip()=='拉勾网':
               break
           err_time=err_time+1
           print('error:'+proxy)
           if err_time==3:
               os.remove(file_name)
               GetIp().get_ip()
               continue

       request.meta['proxy']='http://'+proxy





