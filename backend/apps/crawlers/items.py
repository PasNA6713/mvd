from scrapy.item import Item, Field


class PostItem(Item):
    title = Field(default='')
    link = Field(default='')
    posted = Field(default='')
    text = Field(default='')
    org = Field(default='')
    loc = Field(default='')
    per = Field(default='')