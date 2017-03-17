# encoding=utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from scrapy.spiders import BaseSpider
from scrapy.selector import HtmlXPathSelector
import re
from scrapy.spiders import CrawlSpider,Rule
import scrapy
from sohu.items import SohuItem
from scrapy.linkextractors import LinkExtractor


class DmozSpider(BaseSpider):
    name = "mysohuSpider"
    allow_domains = []
    start_urls = ["http://so.tv.sohu.com/list_p1100_p2_p3_p42016_p5_p6_p7_p8_p9_p101_p11_p12_p13.html"]
    # rules = (
    #     Rule(LinkExtractor(allow=(r'http://so\.tv\.sohu\.com/list_p1100_p2_p3_p42016_p5_p6_p7_p8_p9_\w+_p11_p12_p13.html')), callback='parse_url',
    #          follow=True),
    # )
    #
    #
    pages = set()
    url_set = set()  # 保留url连接

    def parse(self, response):
        # hxs = HtmlXPathSelector(response)
        # if self.start_urls[0] not in self.pages:
        #     yield scrapy.Request(self.start_urls[0], callback=self.parse_url)
        #     self.pages.add(self.start_urls[0])

        hxs = HtmlXPathSelector(response)
        sites = hxs.xpath('//ul[@class="st-list cfix"]/li')
        for site in sites:
            url = "http:" + site.xpath('.//strong/a/@href')[0].extract()
            if url not in self.url_set and re.search(r"tv.sohu.com", url):
                yield scrapy.Request(url, callback=self.parse_item)
                self.url_set.add(url)

        next_page = "http://so.tv.sohu.com" + hxs.xpath('//div[@class="ssPages area"]/a[last()]/@href')[0].extract()
        if next_page not in self.pages:
            self.pages.add(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
            #yield scrapy.Request(next_page, callback=self.parse_url)



    # def parse_url(self, response):
    #     hxs = HtmlXPathSelector(response)
    #     sites = hxs.xpath('//ul[@class="st-list cfix"]/li')
    #     for site in sites:
    #         url = "http:" + site.xpath('.//strong/a/@href')[0].extract()
    #         if url not in self.url_set and re.search(r"tv.sohu.com", url):
    #             yield scrapy.Request(url, callback=self.parse_item)
    #             self.url_set.add(url)

    def parse_item(self, response):
        items = SohuItem()
        hxs = HtmlXPathSelector(response)
        items['name'] = hxs.xpath('//div[@class="crumbs"]/a[last()]/text()').extract()
        items['fav'] = hxs.xpath('//div[@class="vBox vBox-ding"]//i/text()').extract()
        items['step'] = hxs.xpath('//div[@class="vBox vBox-cai"]//i/text()').extract()
        items['playcounts'] = hxs.xpath('//div[@class="vBox vBox-play vBox-play-panel"]//i/text()').extract()
        items['actor'] = hxs.xpath('//div[@class="info info-con"]//a[@data-pb-other="actor"]/text()').extract()
        items['director'] = hxs.xpath('//div[@class="info info-con"]//a[@data-pb-other="director"]/text()').extract()
        items['introduce'] = hxs.xpath('//div[@class="info info-con"]/p[@class="intro"]/text()').extract()
        # items['time']=hxs.xpath('')
        # items['area']=hxs.xpath('')
        # items['type']=hxs.xpath('')
        # items['year']=hxs.xpath('')
        yield items
