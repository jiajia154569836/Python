from scrapy.item import Item, Field


class JianshuItem(Item):
       user = Field()
       time = Field()
       title = Field()
       view = Field()
       comment = Field()
       like = Field()
       gain = Field()