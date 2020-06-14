# -*- coding: utf-8 -*-
import scrapy

class DownLoaderSpider(scrapy.Spider):
    name = 'DownLoaderSpider'
    start_urls = ['https://www.jd.com']

    def parse(self, response):
        self.logger.debug(response.text)
        self.logger.debug('状态码: ' + str(response.status))
