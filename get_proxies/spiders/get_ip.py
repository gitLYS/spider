from scrapy.spiders import Spider
from scrapy import Request
from scrapy.selector import Selector
from get_proxies.items import Proxy
import requests
from bs4 import BeautifulSoup
from mysql import connector as cnn


class Get_Ip(Spider):
   name='test'
   start_url='http://httpbin.org/ip'
   def start_requests(self):
        yield Request(self.start_url)

   def parse(self, response):
        print(response.text)
        yield Request('http://api.ipaddress.com/myip?parameters')

