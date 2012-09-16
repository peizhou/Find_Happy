__author__ = 'zp'
#coding:utf-8
from scrapy.contrib.spiders import CrawlSpider, Rule
from lxml import html
import time
from findhappy.items import FindhappyItem
import urllib2
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
class spider(CrawlSpider):
    name = 'caoegg'
    allowed_domains = ["caoegg.cn"]
    start_urls = ['http://www.caoegg.cn/']
    rules=(
        Rule(SgmlLinkExtractor(allow='page=\d',restrict_xpaths=u'//*[@id="paging"]/a[contains(text(),"后一页")]')),
        Rule(SgmlLinkExtractor(allow='view/\d',),callback='parse_item')
    )
    def parse_item(self, response):
        print response.url
        item = FindhappyItem()#the item
        tem_data = HtmlXPathSelector(response)
        id =tem_data.select('//*[@id="dateleft"]/a/text()').extract()[0][1:]
        detail=tem_data.select('//*[@id="wrap_info"]/div[2]/div[1]/a/span/text()').extract()[0]
        count=tem_data.select('/html/body/div[3]/div/div[2]/div[2]/div[2]/div[2]/span/font/text()').extract()
        good_count=str(count[0]).split('(')[1].split(')')[0]
        bad_count=str(count[1]).split('(')[1].split(')')[0]
        comment=tem_data.select('//*[@id="dateleft"]/text()').extract()[0]
        comment_count=str(comment[comment.find('('):]).split('(')[1].split(')')[0]
        type=''
        try:
            type=tem_data.select('//*[@id="dateright"]/a[1]/text()').extract()[0]
        except :
            type=tem_data.select('//*[@id="dateright"]/a[2]/text()').extract()[0]
        source=response.url
        fetch_time=time.time()
        item["oid"]=int(id)
        item["detail"]=detail
        item["good_count"]=int(good_count)
        item["bad_count"]=int(bad_count)
        item["comment_count"]=int(comment_count)
        item["cat"]=type
        item["source"]=source.decode('utf-8')
        item["fetch_time"]=int(fetch_time)
        return item
