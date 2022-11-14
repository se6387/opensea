import codecs
import os
import scrapy

from openseadetail.items import OpenSeaDetailItem

class OpenSeaCollectionSpider(scrapy.Spider):
    flag = True
    name = 'openseanftspider'
    urlToScrape = 'opensea.io'
    allowed_domains = [
        urlToScrape
    ]

    with open('openseacollection.txt', 'rt') as f:
        collection_name = f.readline()
    
    # start_urls = [
    #     'https://' + urlToScrape + '/' + collection_name
    # ]
    start_urls = [
        'https://' + urlToScrape
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
            f.write('Last Updated : ' + openSeaDetailItem['lastUpdated'] + '\r\n')
            f.write('Creator Earnings : ' + openSeaDetailItem['creatorEarnings'] + '\r\n\n\n')

    def parseurls(self, response):
        openSeaDetailItem = OpenSeaDetailItem()
        item = response.css('div.sc-29427738-0')

        yield {
            'LP': item.css('div.sc-29427738-0').css('div.sc-29427738-0::text').extract()
        }

        if item.css('div.sc-29427738-0').css('div.sc-29427738-0::text').extract()[8] == 'Last Updated':
            global flag
            flag = True
            yield {
                'Contract Address': item.css('span.sc-29427738-0').css('a.sc-1f719d57-0::attr(href)').extract()[0],
                'Token ID': item.css('span.sc-29427738-0').css('a.sc-1f719d57-0::text').extract()[1],
                'Token Standard': item.css('span.sc-29427738-0::text').extract()[0],
                'Chain': item.css('span.sc-29427738-0::text').extract()[1],
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
                'Chain': item.css('span.sc-29427738-0::text').extract()[1],
                'Creator Earnings': item.css('span.sc-29427738-0::text').extract()[2]
            }
            openSeaDetailItem['contractAddress'] = item.css('span.sc-29427738-0').css('a.sc-1f719d57-0::attr(href)').extract()[0]
            openSeaDetailItem['tokenID'] = item.css('span.sc-29427738-0').css('a.sc-1f719d57-0::text').extract()[1]
            openSeaDetailItem['tokenStandard'] = item.css('span.sc-29427738-0::text').extract()[0]
            openSeaDetailItem['chain'] = item.css('span.sc-29427738-0::text').extract()[1]
            openSeaDetailItem['creatorEarnings'] = item.css('span.sc-29427738-0::text').extract()[2]

            self.writeToFile(openSeaDetailItem)
    def parseEthereum(self, response):
        openSeaDetailItem = OpenSeaDetailItem()
        item = response.css('div.sc-29427738-0')

        yield {
                'Contract Address': item.css('span.sc-29427738-0').css('a.sc-1f719d57-0::attr(href)').extract()[0],
                'Token ID': item.css('span.sc-29427738-0').css('a.sc-1f719d57-0::text').extract()[1],
                'Token Standard': item.css('span.sc-29427738-0::text').extract()[0],
                'Chain': item.css('span.sc-29427738-0::text').extract()[1],
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

    def parseCollections(self, response):
        for link in response.css('article.sc-82fdd4b8-6').css('a.sc-1f719d57-0::attr(href)'):
            yield response.follow(link.get(), callback = self.parseEthereum)

    def parse(self, response):
        counter = 0
        yield {
            'scraped links': len(response.css('main.sc-29427738-0').css('div.sc-29427738-0').css('a.sc-1f719d57-0::attr(href)'))
        }

        for link in response.css('main.sc-29427738-0').css('div.sc-29427738-0').css('a.sc-1f719d57-0::attr(href)'):
            # yield response.follow(link.get(), callback = self.parseCollections)
            yield {
                'link': link.get()
            }
            
            # counter += 1

            # if counter == 100:
            #     break
