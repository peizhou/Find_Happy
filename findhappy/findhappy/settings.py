# Scrapy settings for findhappy project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'findhappy'
BOT_VERSION = '1.0'
ITEM_PIPELINES = ['findhappy.pipelines.FindhappyPipeline','scrapy.contrib.pipeline.images.ImagesPipeline']
SPIDER_MODULES = ['findhappy.spiders']
NEWSPIDER_MODULE = 'findhappy.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

