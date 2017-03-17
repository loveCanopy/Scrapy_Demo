# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SohuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name=scrapy.Field()
    fav=scrapy.Field()
    step=scrapy.Field()
    playcounts=scrapy.Field()
    actor=scrapy.Field()
    director=scrapy.Field()
    introduce=scrapy.Field()
    # time=scrapy.Field()
    # area=scrapy.Field()
    # type=scrapy.Field()
    # year=scrapy.Field()


