# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TudouItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    albumId=scrapy.Field()
    title=scrapy.Field()
    actors=scrapy.Field()
    itemTitle=scrapy.Field()
    reputation=scrapy.Field()
    playUrl=scrapy.Field()
    playtimes=scrapy.Field()
    updateInfo=scrapy.Field()

