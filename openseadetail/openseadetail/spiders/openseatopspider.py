import codecs
import os
import scrapy

class OpenSeaTopSpider(scrapy.Spider):
    urltoscrape = "https://opensea.io/rankings"
    allowed_domains = [ urltoscrape ]

    def deleteFileIfExists(self):
        if os.path.exists('openseacollectiondetail.txt'):
            os.remove('openseacollectiondetail.txt')

    def __init__(self):
        self.deleteFileIfExists()
