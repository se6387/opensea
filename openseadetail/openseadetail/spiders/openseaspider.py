import scrapy

class OpenSeaSpider(scrapy.Spider):
    name = 'openseaspider'
    allowed_domains = [
        'opensea.io'
    ]
    start_urls = [
        'https://opensea.io/assets/ethereum/0x394e3d3044fc89fcdd966d3cb35ac0b32b0cda91/5388',
        'https://opensea.io/assets/ethereum/0xaea4fa9451f527d5f36e65f833d88dbb56a0c264/1831'
    ]

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
