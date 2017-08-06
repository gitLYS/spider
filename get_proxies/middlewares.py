# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random
from mysql import connector as cnn
import bs4
from get_proxies.settings import HTTP_PROXY

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
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.
        #
        # Must return only requests (not items).
        # config={
        #     'user':'root',
        #     'password':'lys',
        #     'host':'127.0.0.1',
        #     'port':3306,
        #     'database':'lys'
        #     }
        # proxies=[]
        # conn=cnn.connect(**config)
        # cur=conn.cursor()
        # try:
        #     sql='select ip,port from proxies where type=1 limit 1000'
        #     cur.execute(sql)
        #     result=cur.fetchall()
        #     for item in result:
        #         proxies.append(item[0]+':'+item[1])
        # except:
        #     cur.close()
        #     conn.close()
        # cur.close()
        # conn.close()
        #
        # ip=random.choice(proxies)
        # print(ip)
        # print('-----------------------------------------------------------------------------------\n---------------------\n-------')
        # start_requests.meta['proxy']=ip

        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)



class ProxyMiddleWare(object):
    def process_request(self,request,spider):
        # config={
        #     'user':'root',
        #     'password':'lys',
        #     'host':'127.0.0.1',
        #     'port':3306,
        #     'database':'lys'}
        # proxies=[]
        # conn=cnn.connect(**config)
        # cur=conn.cursor()
        # try:
        #     sql='select ip,port from proxies where flag=1 limit 1000'
        #     cur.execute(sql)
        #     result=cur.fetchall()
        #     for item in result:
        #         proxies.append(item[0]+':'+item[1])
        # except:
        #     cur.close()
        #     conn.close()
        # cur.close()
        # conn.close()
        #
        # ip=random.choice(proxies)
        # print('-----------------------------------------------------------------------------------\n---------------------\n-------')
        request.meta['proxy']=HTTP_PROXY
