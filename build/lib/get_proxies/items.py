# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GetProxiesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Proxy(scrapy.Item):
    ip=scrapy.Field()
    port=scrapy.Field()
    flag=scrapy.Field()
    type=scrapy.Field()

class Movie(scrapy.Item):
    directors=scrapy.Field()
    rate=scrapy.Field()
    star=scrapy.Field()
    title=scrapy.Field()
    url=scrapy.Field()
    casts=scrapy.Field()
    cover=scrapy.Field()
    id=scrapy.Field()
