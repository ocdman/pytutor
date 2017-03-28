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
    	self.conn = pymssql.connect(server='192.168.6.169', user='sa', password='Password01!', database='clinKnowledge1')
    	self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
    	self.cursor.execute("insert into laboratories(id, cname, ename, testname, testdescription, sampletype, normalvalue, normalvaluedescription, summary, testwhys, testwhen, testprinciple, resulteffectreason, diseaserelated, relationtest, relationquestion, suffererprepare) values ({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16})".format(item['id'], item['cname'], item['ename'], item['testName'], item['testDescription'], item['sampleType'], item['normalValue'], item['normalValueDescription'], item['summary'], item['testWhys'], item['testWhen'], item['testPrinciple'], item['resultEffectReason'], item['diseaseRelated'], item['relationTest'], item['relationQuestion'], item['suffererPrepare']))
     	self.conn.commit()
        # return item
