# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import redis
import json
import time
from datetime import datetime


class IndexspiderPipeline(object):
    def process_item(self, item, spider):
        indexId = 0
        if spider.name == 'greed':
            indexId = 1
        elif spider.name == 'longshort':
            indexId = 2
        else:
            print("Bad Index")
            return item

        value = item['value']
        date = int(time.mktime(datetime.now().date().timetuple()))
        index = {'indexId': indexId, 'value': float(value), 'date': date, 'isSaved': False}
        r = redis.Redis(host='localhost', port=6379, password='password', decode_responses=True)
        r.set('a:i:' + str(indexId) + ':' + str(date), json.dumps(index), ex=86400 * 30)
        return item
