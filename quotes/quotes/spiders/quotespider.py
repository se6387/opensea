import scrapy
import os
import re
import codecs

from quotes.items import QuotesItem

class QuoteSpider(scrapy.Spider):
    # add some fields our spider class needs
    txt = '.txt'
    all = False
    fn = 'quotes.toscrape'
    dn = fn + '.com'
    firstPage = [
        'http://' + dn + '/page/1/'
    ]
    scope = [
        'http://' + dn + '/page/1/',
        'http://' + dn + '/page/2/'
        'http://' + dn + '/page/3/'
        'http://' + dn + '/page/4/'
    ]

    name = 'quotespider'
    allowed_domains = [
        dn
    ]
    start_urls = [
        'http://' + dn
    ]

    def deleteFile(self):
        if os.path.exists(self.fn + self.txt):
            os.remove(self.fn + self.txt)

    def startRequests(self):
        self.deleteFile()
        pages = self.firstPage if self.all else self.scope

        for page in pages:
            yield scrapy.Request(page, self.parse)

    def extractData(self, response):
        quotesItem = QuotesItem()

        for quote in response.css('div.quote'):
            # unicode range of valid caharacters for the text
            quotesItem['quote'] = '"' + re.sub(r'[^\x00-\x7f]', r'', quote.css('span.text::text').extract_first()) + '"'
            quotesItem['author'] = quote.css('small.author::text').extract_first()
            quotesItem['tags'] = ' '.join(str(s) for s in quote.css('div.tags > a.tag::text').extract())

            self.writeTxt(quotesItem)

    def parse(self, response):
        self.extractData(response)

    def writeTxt(self, quotesItem):
        with codecs.open(self.fn + self.txt, 'a+', 'utf-8') as f:
            f.write(quotesItem['quote'] + '\r\n')
            f.write(quotesItem['author'] + '\r\n')
            f.write(quotesItem['tags'] + '\r\n\n')
