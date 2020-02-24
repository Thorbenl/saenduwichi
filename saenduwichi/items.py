# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ProfileItem(scrapy.Item):
    # define the fields for your item here like:
    stage_name = scrapy.Field()
    birth_name = scrapy.Field()
    position = scrapy.Field()
    birthday = scrapy.Field()
    height = scrapy.Field()
    weight = scrapy.Field()
    nationality = scrapy.Field()
