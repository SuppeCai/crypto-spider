# -*- coding: utf-8 -*-
import scrapy
from indexSpider.items import LongShortIndexItem


class LongShortSpider(scrapy.Spider):
    name = 'longshort'
    allowed_domains = ['blockchainwhispers.com']
    start_urls = ['https://blockchainwhispers.com/bitmex-position-calculator/']

    def parse(self, response):
        item = LongShortIndexItem()
        longItems = response.xpath('//span[contains(@class,"value long")]/small/text()')
        shortItems = response.xpath('//span[contains(@class,"value short")]/small/text()')

        long = longItems[2].get()
        short = shortItems[2].get()

        item['value'] = round(float(long[0:len(long) - 1]) / float(short[0:len(short) - 1]), 2)
        yield item
