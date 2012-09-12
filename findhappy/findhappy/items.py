#coding:utf-8
from scrapy.item import Item, Field
class data(Item):
    pass
class FindhappyItem(Item):
    oid=Field()#数据本身id
    detail=Field()#数据正文
    good_count=Field()#顶数
    bad_count=Field()#踩数
    comment_count=Field()#评论数
    cat=Field()#数据类型
    source=Field()#数据来源
    fetch_time=Field()#抓取时间时间戳