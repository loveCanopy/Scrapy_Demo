# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=scrapy.Field()
    director=scrapy.Field()
    actor=scrapy.Field()
    type=scrapy.Field()
    area=scrapy.Field()
    publishtime=scrapy.Field()
    time=scrapy.Field()
    rate_num=scrapy.Field()
    rate= scrapy.Field()
    introduce = scrapy.Field()
