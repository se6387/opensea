import scrapy

class OpenSeaSpider(scrapy.Spider):
    name = 'openseaspider'
    allowed_domains = [
        'opensea.io'
    ]
    
    with open('starturls.txt', 'rt') as f:
        start_urls = [url.strip() for url in f.readlines()]

    def parse(self, response):
        item = response.css('div.sc-29427738-0')
        yield {
            'contactAddress': item.css('span.sc-29427738-0').css('a.sc-1f719d57-0::text').extract()[0],
            'tokenId': item.css('span.sc-29427738-0').css('a.sc-1f719d57-0::text').extract()[1],
            'tokenStandard': item.css('span.sc-29427738-0::text').extract()[0],
            'blockChain': item.css('span.sc-29427738-0::text').extract()[1],
            'lastUpdated': item.css('span.sc-29427738-0::text').extract()[2],
            'creatorEarnings': item.css('span.sc-29427738-0::text').extract()[3]
        }
