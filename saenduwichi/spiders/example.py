# -*- coding: utf-8 -*-
from math import ceil

import scrapy as scrapy

from saenduwichi.items import ProfileItem


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['kprofiles.com']
    start_urls = ['https://kprofiles.com/k-pop-girl-groups/']

    def parse(self, response):
        for url in response.xpath("//div[@class='entry-content herald-entry-content']/p/a/@href").extract()[1:]:
            yield scrapy.Request(url=url, callback=self.parse_profile, dont_filter=True)

    def parse_profile(self, response):
        members = response.xpath("//div[@class='entry-content herald-entry-content']/p[position() > 3 and position () < last() -5]")
        #members_c = len(members)//2
        members_i_list = [members_c for members_c in range(len(members)) if members_c % 2]
        print(members_i_list)
        #for member in response.xpath("//div[@class='entry-content herald-entry-content']/p[position() > 4 and position () < last() -5]"):



        # for birth_name in response.xpath("//span[contains(.,'Birth Name')]|//span[contains(.,'Birth name')]"):
        #     print(response.xpath("//span[contains(.,'Birth Name')]|//span[contains(.,'Birth name')]"))
        #     print(birth_name.xpath('./following-sibling::text()').extract_first())
        #
        #     b_name = birth_name.xpath("./following-sibling::text()").extract_first()
        #     if not b_name:
        #         b_name = birth_name.xpath("./following-sibling::text()").extract_first()extract_first

            # profile = ProfileItem(
            #     birth_name=birth_name.xpath("./following-sibling::text()").extract_first(),
            #     url=response.url
            # )
            #yield profile
