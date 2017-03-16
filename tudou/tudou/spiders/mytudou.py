#encoding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from scrapy.spiders import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from tudou.items import TudouItem
import scrapy
import json
class DmozSpider(BaseSpider):
    name="tudouSpider"
    alowed_domains=[]
    start_urls=["http://www.tudou.com/s3portal/service/pianku/data.action?pageSize=3&app=mainsitepc&deviceType=1&tags=&tagType=3&firstTagId=5&areaCode=&initials=&hotSingerId=&pageNo=1&sortDesc=pubTime"]
    def parse(self,response):
        data=response.body
        #print data
        result=json.loads(str(data).decode("unicode-escape"))
        pagesize = 50
        pagenumber=result['total']/pagesize+1
        #print pagenumber
        for i in range(2,pagenumber):
            url = "http://www.tudou.com/s3portal/service/pianku/data.action?pageSize=" + str(
                pagesize) + "&app=mainsitepc&deviceType=1&tags=&tagType=3" \
                            "&firstTagId=5&areaCode=&initials=&hotSingerId=&" \
                            "pageNo=" + str(i) + "&sortDesc=pubTime"
            yield scrapy.Request(url,callback=self.parse_item)

    def parse_item(self,response):
        data = response.body
        result = json.loads(str(data))
        movie_list=result['items']
        for movie in movie_list:
            tudouItem=TudouItem()
            tudouItem['albumId']=movie['albumId']
            tudouItem['title']=movie['title']
            tudouItem['actors'] =movie['actors']
            tudouItem['itemTitle']=movie['itemTitle']
            tudouItem['reputation'] =movie['reputation']
            tudouItem['playUrl']=movie['playUrl']
            tudouItem['playtimes']=movie['playtimes']
            tudouItem['updateInfo']=movie['updateInfo']
            yield tudouItem


