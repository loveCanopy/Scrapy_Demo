#encoding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from scrapy.spiders import BaseSpider
import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from tudou.douitems import DoubanItem
import json
class DmozSpider(BaseSpider):
    name="doubanSpider"
    alowed_domains=[]
    start_urls=["https://movie.douban.com/j/search_subjects?type=movie&tag=日本&sort=recommend&page_limit=20&page_start=0"]
    def etl(log):
        return log.replace("\\r","").replace("\\n","").replace("\\t","").replace("\\","").replace("\n","").replace(" ","")

    def parse(self,response):
        tag = ['最新', '经典', '可播放', '豆瓣高分', '冷门佳片',
               '华语', '欧美', '韩国', '日本', '动作', '喜剧', '科幻', '恐怖']
        page_limit = 20000
        page_start = 0
        sort = ['recommend', 'time', 'rank']

        url_common = "https://movie.douban.com/j/search_subjects?type=movie&tag="

        for i in sort:
            for j in tag:
                url = url_common + j + "&sort=" + i + "&page_limit=" + str(page_limit) + "&page_start=" + str(page_start)
                print url
                yield scrapy.Request(url, callback=self.parse_item_url)

    def parse_item_url(self,response):
        data=response.body
        result = json.loads(str(data))
        for i in result['subjects']:
            yield scrapy.Request(i['url'],callback=self.parse_item)

    def parse_item(self,response):
        hxs=HtmlXPathSelector(response)
        movie=DoubanItem()
        # 电影名
        movie['title'] = hxs.xpath('//h1/span[@property="v:itemreviewed"]/text()')
        # 导演
        movie['director'] = hxs.xpath('//div[@id=\"info\"]/span[1]/span[2]/a/text()')
        # 主演
        movie['actor'] = hxs.xpath('//a[@rel="v:starring"]/text()')
        # 类型
        movie['type'] = hxs.xpath('//*[@id="info"]//span[@property="v:genre"]/text()')
        # 国家和地区
        movie['area'] = hxs.xpath('//*[@id="info"]/text()')
        # 上映时间
        movie['publishtime'] = hxs.xpath('//span[@property=\"v:initialReleaseDate\"]/text()')
        # 片长
        movie['time'] = hxs.xpath('//*[@id="info"]//span[@property="v:runtime"]/text()')
        # 评分
        movie['rate_num'] = hxs.xpath('//strong[@property="v:average"]/text()')
        # 评价
        movie['rate'] = hxs.xpath('//div[@class="rating_sum"]/a/span/text()')
        # 介绍
        movie['introduce'] = hxs.xpath('//*[@id="link-report"]/span/text()')
        yield movie





