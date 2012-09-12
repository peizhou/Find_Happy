__author__ = 'json'
import sys
from scrapy.cmdline import execute
if __name__=="__main__":
    sys.argv=['scrapy','crawl','caoegg',]
    execute()
