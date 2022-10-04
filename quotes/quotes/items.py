# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from email.quoprimime import quote
import scrapy

class QuotesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # define the items that will be extracted
    quote = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()
