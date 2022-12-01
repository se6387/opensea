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
    
    start_urls = [
        etherscanLink
    ]

    def deleteFileIfExists(self):
        if os.path.exists('etherscantransaction.txt'):
            os.remove('etherscantransaction.txt')

    def __init__(self):
        self.deleteFileIfExists()

    def writeToFile(self, openSeaDetailItem):
        with codecs.open('etherscantransaction.txt', 'a+', 'utf-8') as f:
            f.write('Transaction Hash : ' + openSeaDetailItem['transactionHash'] + '\r\n')
            f.write('Status : ' + openSeaDetailItem['status'] + '\r\n')
            f.write('Block : ' + openSeaDetailItem['block'] + '\r\n')
            f.write('Timestamp : ' + openSeaDetailItem['timestamp'] + '\r\n')
            f.write('From : ' + openSeaDetailItem['fromF'] + '\r\n')
            f.write('To : ' + openSeaDetailItem['to'] + '\r\n')
            f.write('Value : ' + openSeaDetailItem['value'] + '\r\n')
            f.write('Transaction Fee : ' + openSeaDetailItem['transactionFee'] + '\r\n')
            f.write('Gas Price : ' + openSeaDetailItem['gasPrice'] + '\r\n\n\n')

    def parseEtherScan(self, response):
        openSeaDetailItem = OpenSeaDetailItem()

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

        openSeaDetailItem['transactionHash'] = response.css('div.col-md-9').css('span.mr-1::text').get()
        openSeaDetailItem['status'] = response.css('div.col').css('span.u-label::text').get()
        openSeaDetailItem['block'] = response.css('div.col-md-9').css('a::text').extract()[2]
        openSeaDetailItem['timestamp'] = response.css('div.row').css('div.col-md-9::text').extract()[8]
        openSeaDetailItem['fromF'] = response.css('div.col-md-9').css('a.mr-1::text').extract()[0]
        openSeaDetailItem['to'] = response.css('div.col-md-9').css('a.mr-1::text').extract()[1]
        openSeaDetailItem['value'] = response.css('div.col-md-9').css('span::text').extract()[7] + ' ' + response.css('div.col-md-9').css('span::text').extract()[8]
        openSeaDetailItem['transactionFee'] = response.css('div.col-md-9').css('span::text').extract()[9] + '.' + response.css('div.col-md-9').css('span::text').extract()[10],
        openSeaDetailItem['gasPrice'] = response.css('div.col-md-9').css('span::text').extract()[11] + response.css('div.col-md-9').css('span::text').extract()[12] + response.css('div.col-md-9').css('span::text').extract()[13]

        

    def parse(self, response):
        for link in response.css('td').css('a.hash-tag::attr(href)'):
            if link.get().startswith('/tx'):
                yield {
                    'link': 'https://' + self.urlToScrape + link.get()
                }

                yield response.follow('https://' + self.urlToScrape + link.get(), callback = self.parseEtherScan)
