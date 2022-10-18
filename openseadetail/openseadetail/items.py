import scrapy

class OpenSeaDetailItem(scrapy.Item):
    # define the items that will be extracted

    #contact address & token id
    cati = scrapy.Field()

    # token standard, block chain, last updated, & creator earnings
    tsbcluce = scrapy.Field()
    
    #
    contractAddress = scrapy.Field()
    tokenID = scrapy.Field()
    tokenStandard = scrapy.Field()
    blockChain = scrapy.Field()
    lastUpdated = scrapy.Field()
    creatorEarnings = scrapy.Field()
