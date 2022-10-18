import codecs
import os
import scrapy

from openseadetail.items import OpenSeaDetailItem

class OpenSeaSpider(scrapy.Spider):
    name = 'openseaspider'
    allowed_domains = [
        'opensea.io'
    ]
    
    with open('starturls.txt', 'rt') as f:
        start_urls = [url.strip() for url in f.readlines()]

    def writeToFile(self, openSeaDetailItem):
        with codecs.open('openseadetail.txt', 'a+', 'utf-8') as f:
            f.write('Contract Address : ' + openSeaDetailItem['contractAddress'] + '\r\n')
            f.write('Token ID : ' + openSeaDetailItem['tokenID'] + '\r\n')
            f.write('Token Standard : ' + openSeaDetailItem['tokenStandard'] + '\r\n')
            f.write('Blockchain : ' + openSeaDetailItem['blockChain'] + '\r\n')
            f.write('Last Updated : ' + openSeaDetailItem['lastUpdated'] + '\r\n')
            f.write('Creator Earnings : ' + openSeaDetailItem['creatorEarnings'] + '\r\n\n\n')

    def extractData(self, response):
        openSeaDetailItem = OpenSeaDetailItem()
        item = response.css('div.sc-29427738-0')

        openSeaDetailItem['contractAddress'] = item.css('span.sc-29427738-0').css('a.sc-1f719d57-0::text').extract()[0]
        openSeaDetailItem['tokenID'] = item.css('span.sc-29427738-0').css('a.sc-1f719d57-0::text').extract()[1]
        openSeaDetailItem['tokenStandard'] = item.css('span.sc-29427738-0::text').extract()[0]
        openSeaDetailItem['blockChain'] = item.css('span.sc-29427738-0::text').extract()[1]
        openSeaDetailItem['lastUpdated'] = item.css('span.sc-29427738-0::text').extract()[2]
        openSeaDetailItem['creatorEarnings'] = item.css('span.sc-29427738-0::text').extract()[3]

        self.writeToFile(openSeaDetailItem)

    def parse(self, response):
        self.extractData(response)

        item = response.css('div.sc-29427738-0')
        yield {
            'Contract Address': item.css('span.sc-29427738-0').css('a.sc-1f719d57-0::text').extract()[0],
            'Token ID': item.css('span.sc-29427738-0').css('a.sc-1f719d57-0::text').extract()[1],
            'Token Standard': item.css('span.sc-29427738-0::text').extract()[0],
            'Block Chain': item.css('span.sc-29427738-0::text').extract()[1],
            'Last Updated': item.css('span.sc-29427738-0::text').extract()[2],
            'Creator Earnings': item.css('span.sc-29427738-0::text').extract()[3]
        }
