#encoding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from scrapy.spiders import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
import  scrapy
import  json
from youku.items import YoukuItem
class DmozSpider(BaseSpider):
    name="myyoukuSpider"
    allow_domains=[]
    page_link = set()  # 保存下一页的url
    content_link = set()  # 当前页所有的url
    start_urls=["http://list.youku.com/category/show/c_96.html?spm=a2hmv.20009921.nav-second.5~1~3!11~A"]
    def parse(self,response):
        hxs=HtmlXPathSelector(response)
        sites=hxs.xpath('//*/ul[@class="panel"]/li[@class="yk-col4 mr1"]')
        for site in sites:
            movie=YoukuItem()
            movie['name']=site.xpath('.//li[@class="title"]/a/text()').extract()
            movie['actor']=site.xpath('.//li[@class="actor"]/a/text()').extract()
            movie['playcounts']=site.xpath('.//li[3]/text()').extract()
            yield movie

        hxs = HtmlXPathSelector(response)
        next_url = "http:" + hxs.xpath('//ul[@class="yk-pages"]/li[@class="next"]/a/@href')[0].extract()
        yield scrapy.Request(next_url, callback=self.parse)


