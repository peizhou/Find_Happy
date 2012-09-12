#coding:utf-8
import pymongo
class FindhappyPipeline(object):
    def process_item(self, item, spider):
        conn=pymongo.Connection('127.0.0.1',27017)
        db=conn["happy"]
        collection=db["sentences"]
        collection.insert(dict(item))