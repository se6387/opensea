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
            openSeaDetailItem['chain'] = item.css('span.sc-29427738-0::text').extract()[1]
            openSeaDetailItem['lastUpdated'] = item.css('span.sc-29427738-0::text').extract()[2]
            openSeaDetailItem['creatorEarnings'] = item.css('span.sc-29427738-0::text').extract()[3]

            self.writeToFile(openSeaDetailItem)
        else:
            flag = False

            yield {
                'Contract Address': item.css('span.sc-29427738-0').css('a.sc-1f719d57-0::text').extract()[0],
                'Token ID': item.css('span.sc-29427738-0').css('a.sc-1f719d57-0::text').extract()[1],
                'Token Standard': item.css('span.sc-29427738-0::text').extract()[0],
                'Block Chain': item.css('span.sc-29427738-0::text').extract()[1],
                'Creator Earnings': item.css('span.sc-29427738-0::text').extract()[2]
            }
            openSeaDetailItem['contractAddress'] = item.css('span.sc-29427738-0').css('a.sc-1f719d57-0::text').extract()[0]
            openSeaDetailItem['tokenID'] = item.css('span.sc-29427738-0').css('a.sc-1f719d57-0::text').extract()[1]
            openSeaDetailItem['tokenStandard'] = item.css('span.sc-29427738-0::text').extract()[0]
            openSeaDetailItem['chain'] = item.css('span.sc-29427738-0::text').extract()[1]
            openSeaDetailItem['creatorEarnings'] = item.css('span.sc-29427738-0::text').extract()[2]

            self.writeToFile(openSeaDetailItem)

    def urlParser(self):
        return 0
