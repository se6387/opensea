import codecs
import os
import re
import scrapy

from openseadetail.items import OpenSeaDetailItem

class OpenSeaDetailSpider(scrapy.Spider):
    # fields the spider needs
    fileExtension = '.txt'
    scrapeAll = False
    fileName = 'openseadetails'
    
    urlToScrape = 'opensea.io'  
    firstPage = [
        'https://' + urlToScrape + '/assets/ethereum/0x394e3d3044fc89fcdd966d3cb35ac0b32b0cda91/5759/'
    ]
    scope = [
        'https://' + urlToScrape + '/assets/ethereum/0x394e3d3044fc89fcdd966d3cb35ac0b32b0cda91/5759/',
        'https://' + urlToScrape + '/assets/ethereum/0x394e3d3044fc89fcdd966d3cb35ac0b32b0cda91/8095/',
        'https://' + urlToScrape + '/assets/ethereum/0x394e3d3044fc89fcdd966d3cb35ac0b32b0cda91/9412/',
        'https://' + urlToScrape + '/assets/ethereum/0x394e3d3044fc89fcdd966d3cb35ac0b32b0cda91/8987/',
        'https://' + urlToScrape + '/assets/ethereum/0x394e3d3044fc89fcdd966d3cb35ac0b32b0cda91/3676/',
        'https://' + urlToScrape + '/assets/ethereum/0x394e3d3044fc89fcdd966d3cb35ac0b32b0cda91/3044/',
        'https://' + urlToScrape + '/assets/ethereum/0x394e3d3044fc89fcdd966d3cb35ac0b32b0cda91/701/',
        'https://' + urlToScrape + '/assets/ethereum/0x394e3d3044fc89fcdd966d3cb35ac0b32b0cda91/9683/',
        'https://' + urlToScrape + '/assets/ethereum/0x394e3d3044fc89fcdd966d3cb35ac0b32b0cda91/2396/',
        'https://' + urlToScrape + '/assets/ethereum/0x394e3d3044fc89fcdd966d3cb35ac0b32b0cda91/1361/'
    ]

    name = 'openseadetailspider'
    allowed_domains = [
        urlToScrape
    ]
    start_urls = [
        'https://' + urlToScrape
    ]
    
    def deleteIfFileExists(self):
        if os.path.exists(self.fileName + self.fileExtension):
            os.remove(self.fileName + self.fileExtension)

    def startRequests(self):
        self.deleteIfFileExists(self)

        # myHeaders = {
        #     'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win 64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        #     #'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1'
        #     #'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
        # }
        # for url in self.start_urls:
        #     yield re(url, headers = myHeaders)
            
        pages = self.firstPage if self.scrapeAll else self.scope
        for page in pages:
            yield scrapy.Request(url = page, callback = self.parse)

    def extractData(self, response):
        openSeaDetailsItem = OpenSeaDetailItem()
        f = open(self.fileName + self.fileExtension, 'x')
        f.write('scrapping started ..')

        # div.sc-29427738-0.dVNeWL  # sc-29427738-0 dVNeWL  assets-item-asset-details > div > div > div
        for details in response.css('div.sc-29427738-0.dVNeWL'):
            openSeaDetailsItem['cati'] = details.css('span.sc-29427738-0.sc-bdnxRM.sc-37c1b040-1.dVNeWL.kdkxCj.klapes > a.sc-1f719d57-0.fKAlPV::text').extract()
            # openSeaDetailsItem['tsbcluce'] = details.css('span.sc-29427738-0.sc-bdnxRM.sc-37c1b040-1.dVNeWL.kdkxCj.klapes::text').extract()
            
            # openSeaDetailsItem['contractAddress'] = re.sub(r'[^\x00-\x7f]', r'', details.css('a.sc-1f719d57-0.fKAlPV::text').extract_first())
            # openSeaDetailsItem['contractAddress'] = details.css('a.sc-1f719d57-0 fKAlPV::text').extract_first()
            # openSeaDetailsItem['tokenId'] = details.css('div.sc-29427738-0 > span.sc-29427738-0::text').extract_first()

            self.writeToFile(openSeaDetailsItem)

    def parse(self, response):
        self.extractData(response)
    
    def writeToFile(self, openSeaDetailsItem):
        with codecs.open(self.fileName + self.fileExtension, 'a+', 'utf-8') as f:
            f.write(openSeaDetailsItem['cati'] + '\r\n')
            f.write(openSeaDetailsItem['tsbcluce'] + '\r\n')
