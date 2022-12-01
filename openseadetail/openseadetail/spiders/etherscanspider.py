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

    def parseEtherScan(self, response):
        yield {
            'Transaction Hash': response.css('div.col-md-9').css('span.mr-1::text').get(),
            'Status': response.css('div.col').css('span.u-label::text').get(),
            'Block': response.css('div.col-md-9').css('a::text').extract()[2],
            'Timestamp': response.css('div.row').css('div.col-md-9::text').extract()[8],
            # 'Transaction Action': response.css('div.media-body').css('span.mr-1::text').extract()[0] + ' ' + response.css('div.media-body').css('span.mr-1::text').extract()[1] + ' ' + response.css('div.media-body').css('span.mr-1::text').extract()[2] + ' ' + response.css('div.media-body').css('span.mr-1::text').extract()[3] + ' ' + response.css('div.col-md-9').css('a.mr-1::text').extract()[0] + ' ' + response.css('div.media-body').css('span.text-secondary::text').extract()[1] + ' ' + response.css('div.col-md-9').css('a.mr-1::text').extract()[1],
            'From': response.css('div.col-md-9').css('a.mr-1::text').extract()[0],
            'To': response.css('div.col-md-9').css('a.mr-1::text').extract()[1],
            # 'ERC-721 Tokens Transferred': response.css('div.mr-1').css('span.font-weight-bold::text').extract()[0] + ' ' + response.css('div.col-md-9').css('a.mr-1::text').extract()[0] + ' ' + response.css('div.mr-1').css('span.font-weight-bold::text').extract()[1] + ' ' + response.css('div.col-md-9').css('a.mr-1::text').extract()[1],
            'Value': response.css('div.col-md-9').css('span::text').extract()[7] + ' ' + response.css('div.col-md-9').css('span::text').extract()[8],
            'Transaction Fee': response.css('div.col-md-9').css('span::text').extract()[9] + '.' + response.css('div.col-md-9').css('span::text').extract()[10],
            'Gas Price': response.css('div.col-md-9').css('span::text').extract()[11] + response.css('div.col-md-9').css('span::text').extract()[12] + response.css('div.col-md-9').css('span::text').extract()[13]
        }

    def parse(self, response):
        for link in response.css('td').css('a.hash-tag::attr(href)'):
            if link.get().startswith('/tx'):
                yield {
                    'link': 'https://' + self.urlToScrape + link.get()
                }

                yield response.follow('https://' + self.urlToScrape + link.get(), callback = self.parseEtherScan)
