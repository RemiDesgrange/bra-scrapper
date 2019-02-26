from scrapy import Item, Field

class Bra(Item):
    date = Field()
    region = Field()
    level = Field(serializer=int)
    
