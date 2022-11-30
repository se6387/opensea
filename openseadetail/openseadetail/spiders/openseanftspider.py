import codecs
import os
import scrapy

from openseadetail.items import OpenSeaDetailItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class OpenSeaCollectionSpider(CrawlSpider):
    flag = True
    etherCount = 0
    etherscanLink = ''

    name = 'openseanftspider'
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
            f.write('Chain : ' + openSeaDetailItem['chain'] + '\r\n')

            global flag
            if flag:
                f.write('Last Updated : ' + openSeaDetailItem['lastUpdated'] + '\r\n')

            f.write('Creator Earnings : ' + openSeaDetailItem['creatorEarnings'] + '\r\n\n\n')

    def parseCollection(self, response):
        openSeaDetailItem = OpenSeaDetailItem()
        item = response.css('div.sc-29427738-0')

        if item.css('div.sc-29427738-0').css('div.sc-29427738-0::text').extract()[8] == 'Last Updated':
            global flag
            flag = True
            yield {
                'Contract Address': item.css('span.sc-29427738-0').css('a.sc-1f719d57-0::attr(href)').extract()[0],
                'Token ID': item.css('span.sc-29427738-0').css('a.sc-1f719d57-0::text').extract()[1],
                'Token Standard': item.css('span.sc-29427738-0::text').extract()[0],
                'Block Chain': item.css('span.sc-29427738-0::text').extract()[1],
                'Last Updated': item.css('span.sc-29427738-0::text').extract()[2],
                'Creator Earnings': item.css('span.sc-29427738-0::text').extract()[3]
            }

            openSeaDetailItem['contractAddress'] = item.css('span.sc-29427738-0').css('a.sc-1f719d57-0::attr(href)').extract()[0]
            openSeaDetailItem['tokenID'] = item.css('span.sc-29427738-0').css('a.sc-1f719d57-0::text').extract()[1]
            openSeaDetailItem['tokenStandard'] = item.css('span.sc-29427738-0::text').extract()[0]
            openSeaDetailItem['chain'] = item.css('span.sc-29427738-0::text').extract()[1]
            openSeaDetailItem['lastUpdated'] = item.css('span.sc-29427738-0::text').extract()[2]
            openSeaDetailItem['creatorEarnings'] = item.css('span.sc-29427738-0::text').extract()[3]

            self.writeToFile(openSeaDetailItem)
        else:
            flag = False

            yield {
                'Contract Address': item.css('span.sc-29427738-0').css('a.sc-1f719d57-0::attr(href)').extract()[0],
                'Token ID': item.css('span.sc-29427738-0').css('a.sc-1f719d57-0::text').extract()[1],
                'Token Standard': item.css('span.sc-29427738-0::text').extract()[0],
                'Block Chain': item.css('span.sc-29427738-0::text').extract()[1],
                'Creator Earnings': item.css('span.sc-29427738-0::text').extract()[2]
            }
            openSeaDetailItem['contractAddress'] = item.css('span.sc-29427738-0').css('a.sc-1f719d57-0::attr(href)').extract()[0]
            openSeaDetailItem['tokenID'] = item.css('span.sc-29427738-0').css('a.sc-1f719d57-0::text').extract()[1]
            openSeaDetailItem['tokenStandard'] = item.css('span.sc-29427738-0::text').extract()[0]
            openSeaDetailItem['chain'] = item.css('span.sc-29427738-0::text').extract()[1]
            openSeaDetailItem['creatorEarnings'] = item.css('span.sc-29427738-0::text').extract()[2]

            self.writeToFile(openSeaDetailItem)

        # etherscanLink = item.css('span.sc-29427738-0').css('a.sc-1f719d57-0::attr(href)').extract()[0]
        # yield {
        #     'ether scan link': etherscanLink
        # }
        # yield response.follow(etherscanLink, callback = self.parseEtherScan)

    # def parseEtherScan(self, response):
    #     item = response.css('td').css('a.hash-tag::attr(href)')
    #     yield {
    #         'etsl': etherscanLink
    #     }

    def parseEthereum(self, response):
        item = response.css('div.sc-29427738-0')

        global etherscanLink
        etherscanLink = item.css('span.sc-29427738-0').css('a.sc-1f719d57-0::attr(href)').extract()[0]

        yield {
            'ether scan link': etherscanLink
        }

        # yield response.follow(etherscanLink, callback = self.parseEtherScan)

    def parse(self, response):
        global etherCount
        etherCount = 0

        yield {
            'scraped links': len(response.css('article.sc-a4604e96-6').css('a.sc-1f719d57-0::attr(href)'))
        }

        ethereum = response.css('article.sc-a4604e96-6').css('a.sc-1f719d57-0::attr(href)').extract()[0]
        yield response.follow(ethereum, callback = self.parseEthereum)

        for link in response.css('article.sc-a4604e96-6').css('a.sc-1f719d57-0::attr(href)'):
            etherCount += 1
            yield response.follow(link.get(), callback = self.parseCollection)
