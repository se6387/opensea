import codecs
import os
from pyexpat.errors import codes
import scrapy

from openseadetail.items import OpenSeaDetailItem

class OpenSeaCollectionSpider(scrapy.Spider):
    name = 'openseacollectionspider'
    urlToScrape = 'opensea.io'
    allowed_domains = [
        urlToScrape
    ]

    with open('openseacollection.txt', 'rt') as f:
        collection_name = f.readline()
    
    start_urls = [
        'https://' + urlToScrape + '/' + collection_name
    ]

    def deleteFileIfExists(self):
        if os.path.exists('openseacollectiondetail.txt'):
            os.remove('openseacollectiondetail.txt')

    def __init__(self):
        self.deleteFileIfExists()

    def writeToFile(self, openSeaDetailItem):
        with codecs.open('openseacollectiondetail.txt', 'a+', 'utf-8') as f:
            f.write('Contract Address : ' + openSeaDetailItem['contractAddress'] + '\r\n')
            f.write('Token ID : ' + openSeaDetailItem['tokenID'] + '\r\n')
            f.write('Token Standard : ' + openSeaDetailItem['tokenStandard'] + '\r\n')
            f.write('Blockchain : ' + openSeaDetailItem['blockChain'] + '\r\n')
            f.write('Last Updated : ' + openSeaDetailItem['lastUpdated'] + '\r\n')
            f.write('Creator Earnings : ' + openSeaDetailItem['creatorEarnings'] + '\r\n\n\n')

    def parseurls(self, response):
        openSeaDetailItem = OpenSeaDetailItem()
        item = response.css('div.sc-29427738-0')

        yield {
            'Contract Address': item.css('span.sc-29427738-0').css('a.sc-1f719d57-0::text').extract()[0],
            'Token ID': item.css('span.sc-29427738-0').css('a.sc-1f719d57-0::text').extract()[1],
            'Token Standard': item.css('span.sc-29427738-0::text').extract()[0],
            'Block Chain': item.css('span.sc-29427738-0::text').extract()[1],
            'Last Updated': item.css('span.sc-29427738-0::text').extract()[2],
            'Creator Earnings': item.css('span.sc-29427738-0::text').extract()[3]
        }

        openSeaDetailItem['contractAddress'] = item.css('span.sc-29427738-0').css('a.sc-1f719d57-0::text').extract()[0]
        openSeaDetailItem['tokenID'] = item.css('span.sc-29427738-0').css('a.sc-1f719d57-0::text').extract()[1]
        openSeaDetailItem['tokenStandard'] = item.css('span.sc-29427738-0::text').extract()[0]
        openSeaDetailItem['blockChain'] = item.css('span.sc-29427738-0::text').extract()[1]
        openSeaDetailItem['lastUpdated'] = item.css('span.sc-29427738-0::text').extract()[2]
        openSeaDetailItem['creatorEarnings'] = item.css('span.sc-29427738-0::text').extract()[3]

        self.writeToFile(openSeaDetailItem)

    def parse(self, response):
        yield {
            'scraped links': len(response.css('article.sc-d72d0ead-4').css('a.sc-1f719d57-0::attr(href)'))
        }

        for link in response.css('article.sc-d72d0ead-4').css('a.sc-1f719d57-0::attr(href)'):
            yield response.follow(link.get(), callback = self.parseurls)
            