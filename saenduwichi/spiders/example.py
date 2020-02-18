# -*- coding: utf-8 -*-
import scrapy as scrapy

from saenduwichi.items import ProfileItem


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['kprofiles.com']
    start_urls = ['https://kprofiles.com/korean-actresses-profiles/']

    def parse(self, response):
        for profile in response.css('.herald-entry-content p'):
            url = response.urljoin(profile.css('a::attr(href)').extract_first())
            yield scrapy.Request(url=url, callback=self.parse_profile, dont_filter=True)

    def parse_profile(self, response):
        birth_name = response.xpath("//span[contains(.,'Name')]/following-sibling::text()").extract_first()
        profile = ProfileItem(
            birth_name=birth_name
        )
        yield profile


# /following-sibling::text()