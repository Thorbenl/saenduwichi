# -*- coding: utf-8 -*-
import scrapy as scrapy
from urllib.parse import urlparse

from saenduwichi.items import ProfileItem


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['kprofiles.com']
    start_urls = ['https://kprofiles.com/k-pop-girl-groups/']

    def parse(self, response):
        for url in response.xpath("//div[@class='entry-content herald-entry-content']/p/a/@href").extract()[1:]:
            yield scrapy.Request(url=url, callback=self.parse_profile, dont_filter=True)

    def parse_profile(self, response):
        members = response.xpath(
            "//div[@class='entry-content herald-entry-content']/p[position() > 3 and position () < last() -5]")
        members_c = len(members)
        if members_c % 2 != 0:
            members_c += 1
        m = 4
        indexes = []
        while m <= members_c + 2:
            indexes.append(m)
            m += 2

        # group_name = response.url
        # parsed = urlparse(group_name)
        # pathvar = parsed.path
        # print(pathvar.split('-')[0][1:])

        for index in indexes:
            profile = ProfileItem(
                birth_name=response.xpath(
                    "//div[@class='entry-content herald-entry-content']//p[%s]/span[contains(.,'Birth Name')]/following-sibling::text()|//span[contains(.,'Birth name')]/following-sibling::text()" % index).extract_first(),
                stage_name=response.xpath(
                    "//div[@class='entry-content herald-entry-content']//p[%s]/span[contains(.,'Stage Name')]/following-sibling::text()|//span[contains(.,'Stage name')]/following-sibling::text()" % index).extract_first(),
                position=response.xpath(
                    "//div[@class='entry-content herald-entry-content']//p[%s]/span[contains(.,'Position')]/following-sibling::text()" % index).extract_first(),
                height=response.xpath(
                    "//div[@class='entry-content herald-entry-content']//p[%s]/span[contains(.,'Height')]/following-sibling::text()" % index).extract_first(),
                weight=response.xpath(
                    "//div[@class='entry-content herald-entry-content']//p[%s]/span[contains(.,'Weight')]/following-sibling::text()" % index).extract_first(),
                nationality=response.xpath(
                    "//div[@class='entry-content herald-entry-content']//p[%s]/span[contains(.,'Nationality')]/following-sibling::text()" % index).extract_first(),
            )
            yield profile

