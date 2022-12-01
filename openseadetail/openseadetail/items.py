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
    chain = scrapy.Field()
    lastUpdated = scrapy.Field()
    creatorEarnings = scrapy.Field()

    transactionHash = scrapy.Field()
    status = scrapy.Field()
    block = scrapy.Field()
    timestamp = scrapy.Field()
    fromF = scrapy.Field()
    to = scrapy.Field()
    value = scrapy.Field()
    transactionFee = scrapy.Field()
    gasPrice = scrapy.Field()
