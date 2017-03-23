# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymssql
import json

class TutorialPipeline(object):

    def __init__(self):
    	print "start pymssql connect"
    	self.conn = pymssql.connect(server='192.168.5.35', user='sa', password='Password01!', database='clinKnowledge1')
    	self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
    	self.cursor.execute("insert into laboratories(cname, ename, testname, testdescription, sampletype, normalvalue, normalvaluedescription, summary, testwhys, testwhen, testprinciple, resulteffectreason, diseaserelated, relationtest, relationquestion) values ({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14})".format(item['cname'], item['ename'], item['testName'], item['testDescription'], item['sampleType'], item['normalValue'], item['normalValueDescription'], item['summary'], item['testWhys'], item['testWhen'], item['testPrinciple'], item['resultEffectReason'], item['diseaseRelated'], item['relationTest'], item['relationQuestion']))
     	self.conn.commit()
        return item
