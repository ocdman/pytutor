# -*- coding: utf-8 -*-
import scrapy
import json
import time
import traceback

from tutorial.items import *
from tutorial.settings import COOKIES
from scrapy.http import FormRequest

class XingshulinSpider(scrapy.Spider):
	name = "xingshulin"
	allowed_domains = ["xingshulin.com"]
	global filename
	filename = 'testVo.json'
	global failurefile
	failurefile = 'failure.txt'
	global exceptionfile
	exceptionfile = 'exception.txt'
	global misseditemfile
	misseditemfile = 'misseditem.txt'
	# start_urls = [
	# 	"http://www.xingshulin.com/searchTest.html"
	# ]

	def __init__(self):
		self.cookies = COOKIES
		#清空文件，如果没有文件则创建
		# f = open(filename, 'wb')
		# f.close()
		ff = open(failurefile, 'wb')
		ff.close()
		ef = open(exceptionfile, 'wb')
		ef.close()
		mf = open(misseditemfile, 'wb')
		mf.close()

	def start_requests(self):
		#检验
		#改动范围,用来测试
		#for i in range(2, 0, -1):
		# for i in range(4800, 0, -1):
		# 	yield FormRequest("http://epocket.xingshulin.com/test/getTestDetail/{0}".format(i),
		# 		cookies=self.cookies,
		# 		callback=self.parseTest)

		#指南
		for i in range(21000, 0, -1):
			yield FormRequest("https://epocket.xingshulin.com/guide/getGuideDetail/{0}".format(i),
				cookies=self.cookies,
				callback=self.parseGuide)

		# for i in range(4712, 0, -2):
		# 	yield FormRequest("http://www.xingshulin.com/TestAction.do?processID=get&id={0}".format(i),
		# 				formdata={'processID': 'get', 'id': '{0}'.format(i)},
		# 				callback=self.parse)

		# for i in range(1, 31):
		# 	yield FormRequest("http://www.xingshulin.com/QueryAction.do?processID=getResult&pageno={0}&catalog=%E6%A3%80%E9%AA%8C&timeRange=&classTags=&insurancetype=&periodical=&queryStr=*".format(i),
		# 				formdata={'processID': 'getResult', 'pageno': '{0}'.format(i), 'catalog': '%E6%A3%80%E9%AA%8C', 'timeRange': '', 'classTags': '', 'insurancetype': '', 'periodical': '', 'queryStr': '*'},
		# 				callback=self.parse)

	#解析检验
	def parseTest(self, response):
		if response.status == 200:
			details = json.loads(response.body)
			testItem = XingshulinTestItem()
			try:
				if details['obj'].has_key('testVo') == True:
					items = details['obj']['testVo']
					if 'id' in items:
						testItem['id'] = items['id']
						testItem['cname'] = "'" + items['cname'].encode('utf-8').replace("'","''") + "'" if 'cname' in items else 'NULL'
						testItem['ename'] = "'" + items['ename'].encode('utf-8').replace("'","''") + "'" if 'ename' in items else 'NULL'
						testItem['testName'] = "'" + items['testName'].encode('utf-8').replace("'","''") + "'"  if 'testName' in items else 'NULL'
						testItem['testDescription'] =  "'" + items['testDescription'].encode('utf-8').replace("'","''") + "'"  if 'testDescription' in items else 'NULL'
						testItem['sampleType'] = "'" + items['sampleType'].encode('utf-8').replace("'","''") + "'" if 'sampleType' in items else 'NULL'
						testItem['normalValue'] = "'" + items['normalValue'].encode('utf-8').replace("'","''") + "'" if 'normalValue' in items else 'NULL'
						testItem['normalValueDescription'] = "'" + items['normalValueDescription'].encode('utf-8').replace("'","''") + "'" if 'normalValueDescription' in items else 'NULL'
						testItem['summary'] = "'" + items['summary'].encode('utf-8').replace("'","''") + "'" if 'summary' in items else 'NULL'
						testItem['testWhys'] = "'" + items['testWhys'].encode('utf-8').replace("'","''") + "'" if 'testWhys' in items else 'NULL'
						testItem['testWhen'] = "'" + items['testWhen'].encode('utf-8').replace("'","''") + "'" if 'testWhen' in items else 'NULL'
						testItem['testPrinciple'] = "'" + items['testPrinciple'].encode('utf-8').replace("'","''") + "'" if 'testPrinciple' in items else 'NULL'
						testItem['resultEffectReason'] = "'" + items['resultEffectReason'].encode('utf-8').replace("'","''") + "'" if 'resultEffectReason' in items else 'NULL'
						testItem['diseaseRelated'] = "'" + items['diseaseRelated'].encode('utf-8').replace("'","''") + "'" if 'diseaseRelated' in items else 'NULL'
						testItem['relationTest'] = "'" + items['relationTest'].encode('utf-8').replace("'","''") + "'" if 'relationTest' in items else 'NULL'
						testItem['relationQuestion'] = "'" + items['relationQuestion'].encode('utf-8').replace("'","''") + "'" if 'relationQuestion' in items else 'NULL'
						testItem['suffererPrepare'] = "'" + items['suffererPrepare'].encode('utf-8').replace("'","''") + "'" if 'suffererPrepare' in items else 'NULL'
						testItem['swatchGather'] = "'" + items['swatchGather'].encode('utf-8').replace("'","''") + "'" if 'swatchGather' in items else 'NULL'
						#这段可以省略了
						# for key in items:
						# 	if key not in testItem:
						# 		#写入遗漏的字段
						# 		with open(misseditemfile, 'a+') as mf:
						# 			mf.write(time.strftime('%Y-%m-%d %H:%m:%S',time.localtime(time.time())) + ', 遗漏字段: ' + str(key) + '\n')
						# 		mf.close()
						return testItem
			except Exception, ex:
				#写入异常捕获
				with open(exceptionfile, 'a+') as ef:
					ef.write(time.strftime('%Y-%m-%d %H:%m:%S',time.localtime(time.time())) + ', 异常捕获: ' + str(ex) + '\n')
		elif response.status == 404:
			#写入未爬取的url
			with open(failurefile, 'a+') as ff:
				ff.write(time.strftime('%Y-%m-%d %H:%m:%S',time.localtime(time.time())) + ', 未爬取的url: ' + str(response.url) + '\n')

	#解析指南
	def parseGuide(self, response):
		if response.status == 200:
			details = json.loads(response.body)
			guideItem = XingshulinGuideItem()
			try:
				if details['obj'].has_key('guideVo') == True:
					items = details['obj']['guideVo']
					if 'id' in items:
						guideItem['id'] = items['id']
						guideItem['guideName'] = "'" + items['guideName'].encode('utf-8').replace("'","''") + "'" if 'guideName' in items else 'NULL'
						guideItem['year'] = "'" + items['year'].encode('utf-8').replace("'","''") + "'" if 'year' in items else 'NULL'
						guideItem['organization'] = "'" + items['organization'].encode('utf-8').replace("'","''") + "'" if 'organization' in items else 'NULL'
						guideItem['summary'] = "'" + items['summary'].encode('utf-8').replace("'","''") + "'" if 'summary' in items else 'NULL'
						guideItem['publishedDate'] = "'" + items['publishedDate'].encode('utf-8').replace("'","''") + "'" if 'publishedDate' in items else 'NULL'
						guideItem['pdfLink'] = "'" + items['pdfLink'].encode('utf-8').replace("'","''") + "'" if 'pdfLink' in items else 'NULL'
						guideItem['epubLink'] = "'" + items['epubLink'].encode('utf-8').replace("'","''") + "'" if 'epubLink' in items else 'NULL'
						guideItem['journal'] = "'" + items['journal'].encode('utf-8').replace("'","''") + "'" if 'journal' in items else 'NULL'
						guideItem['author'] = "'" + items['author'].encode('utf-8').replace("'","''") + "'" if 'author' in items else 'NULL'
						guideItem['volume'] = "'" + items['volume'].encode('utf-8').replace("'","''") + "'" if 'volume' in items else 'NULL'
						guideItem['issue'] = "'" + items['issue'].encode('utf-8').replace("'","''") + "'" if 'issue' in items else 'NULL'
						guideItem['downloadCount'] = 0
						# for key in items:
						# 	if key not in guideItem:
						# 		with open(misseditemfile, 'a+') as mf:
						# 			mf.write(time.strftime('%Y-%m-%d %H:%m:%S',time.localtime(time.time())) + ', 遗漏字段: ' + str(key) + ', Id:' + str(items['id']) + '\n')
						# 		mf.close()
						return guideItem
			except Exception, ex:
				with open(exceptionfile, 'a+') as ef:
					ef.write(time.strftime('%Y-%m-%d %H:%m:%S',time.localtime(time.time())) + ', 异常捕获: ' + str(ex) + '\n')
		elif response.status == 404:
			with open(failurefile, 'a+') as ff:
				ff.write(time.strftime('%Y-%m-%d %H:%m:%S',time.localtime(time.time())) + ', 未爬取的url: ' + str(response.url) + '\n')
