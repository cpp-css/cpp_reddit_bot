# -*- coding: utf-8 -*-
import scrapy


class OrganizationsSpider(scrapy.Spider):
    name = 'organizations'
    allowed_domains = ['https://mybar.cpp.edu/organizations']
    start_urls = ['http://https://mybar.cpp.edu/organizations/']

    def parse(self, response):
        pass
