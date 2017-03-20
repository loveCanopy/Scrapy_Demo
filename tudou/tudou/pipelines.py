# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TudouPipelintem pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb
from scrapy.utils.project import get_project_settings
from datetime import datetime
from hashlib import md5
class MySQLStoreTudouPipeline:
    # pipeline默认调用
    def __init__(self):
        self.settings = get_project_settings()  # 获取settings配置，设置需要的信息
        self.host = self.settings['MYSQL_HOST']
        self.port = self.settings['MYSQL_PORT']
        self.user = self.settings['MYSQL_USER']
        self.passwd = self.settings['MYSQL_PASSWD']
        self.db = self.settings['MYSQL_DBNAME']
        # 连接到mysql，不是连接到具体的数据库
        self.conn = self.connectDatabase()  # 连接数据库

    def connectDatabase(self):
        conn = MySQLdb.connect(host=self.host,
                               port=self.port,
                               user=self.user,
                               passwd=self.passwd,
                               db=self.db,
                               charset='utf8')  # 要指定编码，否则中文可能乱码
        return conn

        # 获取url的md5编码

    def _get_linkmd5id(self, item):
        # url进行md5处理，为避免重复采集设计
        return md5(item['playUrl']).hexdigest()

    def process_item(self, item, spider):
        cur=self.conn.cursor()
        linkmd5id = self._get_linkmd5id(item)
        now = datetime.utcnow().replace(microsecond=0).isoformat(' ')
        sql='''
              insert into tudou_info
                   values(%s, %s, %s, %s, %s, %s,%s, %s, %s, %s)
                   '''
        #print item['albumId']
        data=(linkmd5id, str(item['albumId']), str(item['title']), str(item['actors']), str(item['itemTitle']), str(item['reputation']),
                     str(item['playUrl']),str(item['playtimes']), str(item['updateInfo']), now)
        cur.execute(sql, data)
        self.conn.commit()
        cur.close()


