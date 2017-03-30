# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymssql
import json
import threading

from tutorial.items import *

class TutorialPipeline(object):

	def __init__(self):
		self.lock = threading.Lock()
		print "start pymssql connect"
		#数据库配置
		self.conn = pymssql.connect(server='192.168.6.169', user='sa', password='Password01!', database='clinKnowledge1')
		self.cursor = self.conn.cursor()

	def process_item(self, item, spider):
		if isinstance(item, XingshulinTestItem):
			self.lock.acquire()
			self.cursor.execute("insert into laboratories(id, cname, ename, testname, testdescription, sampletype, normalvalue, normalvaluedescription, summary, testwhys, testwhen, testprinciple, resulteffectreason, diseaserelated, relationtest, relationquestion, suffererprepare, swatchgather) values ({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17})".format(item['id'], item['cname'], item['ename'], item['testName'], item['testDescription'], item['sampleType'], item['normalValue'], item['normalValueDescription'], item['summary'], item['testWhys'], item['testWhen'], item['testPrinciple'], item['resultEffectReason'], item['diseaseRelated'], item['relationTest'], item['relationQuestion'], item['suffererPrepare'], item['swatchGather']))
			self.conn.commit()
			self.lock.release()
		elif isinstance(item, XingshulinGuideItem):
			self.lock.acquire()
			self.cursor.execute("insert into guides(id, guideName, year, organization, summary, publishedDate, pdfLink, epubLink, journal, author, volume, issue) values ({0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11})".format(item['id'], item['guideName'], item['year'], item['organization'], item['summary'], item['publishedDate'], item['pdfLink'], item['epubLink'], item['journal'], item['author'], item['volume'], item['issue']))
			self.conn.commit()
			self.lock.release()
        # return item
