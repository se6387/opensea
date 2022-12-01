import codecs
import os
import scrapy

from openseadetail.items import OpenSeaDetailItem

class EtherScanSpider(scrapy.Spider):
    name = 'etherscanspider'
    urlToScrape = 'etherscan.io'
    allowed_domains = [
        urlToScrape
    ]

    with open('openseacollectiondetail.txt', 'rt') as f:
        etherscanLink = f.readline()
        etherscanLink = etherscanLink[19:]
        print(etherscanLink)
    
    start_urls = [
        etherscanLink
    ]

    def deleteFileIfExists(self):
        if os.path.exists('openseaetherscan.txt'):
            os.remove('openseaetherscan.txt')

    def __init__(self):
        self.deleteFileIfExists()

        with open('openseacollectiondetail.txt', 'rt') as f:
            etherscanLink = f.readline()
            etherscanLink = etherscanLink[20]
            print(etherscanLink)

    def parse(self, response):
        for link in response.css('td').css('a.hash-tag::attr(href)'):
            if link.get().startswith('/tx'):
                yield {
                    'link': link.get()
                }
