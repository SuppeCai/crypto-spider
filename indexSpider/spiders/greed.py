# -*- coding: utf-8 -*-
import scrapy
from indexSpider.items import GreedIndexItem


class GreedSpider(scrapy.Spider):
    name = 'greed'
    allowed_domains = ['alternative.me']
    start_urls = ['https://alternative.me/crypto/fear-and-greed-index/']

    def parse(self, response):
        item = GreedIndexItem()
        item['value'] = response.css('.fng-circle::text').extract_first()
        yield item
