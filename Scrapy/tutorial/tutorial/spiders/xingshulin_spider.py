# -*- coding: utf-8 -*-
import scrapy
import json
import time
import traceback

from tutorial.items import XingshulinItem
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
		for i in range(10000, 0, -1):
			yield FormRequest("http://epocket.xingshulin.com/test/getTestDetail/{0}".format(i),
				cookies=self.cookies,
				callback=self.parse)

		# for i in range(4712, 0, -2):
		# 	yield FormRequest("http://www.xingshulin.com/TestAction.do?processID=get&id={0}".format(i),
		# 				formdata={'processID': 'get', 'id': '{0}'.format(i)},
		# 				callback=self.parse)

		# for i in range(1, 31):
		# 	yield FormRequest("http://www.xingshulin.com/QueryAction.do?processID=getResult&pageno={0}&catalog=%E6%A3%80%E9%AA%8C&timeRange=&classTags=&insurancetype=&periodical=&queryStr=*".format(i),
		# 				formdata={'processID': 'getResult', 'pageno': '{0}'.format(i), 'catalog': '%E6%A3%80%E9%AA%8C', 'timeRange': '', 'classTags': '', 'insurancetype': '', 'periodical': '', 'queryStr': '*'},
		# 				callback=self.parse)

	def parse(self, response):
		# if response.status == 200:
		# 	items = json.loads(response.body)
		# 	if items['obj'].has_key('testVo') == True:
		# 		with open(filename, 'a+') as f:
		# 			ids = '{id: ' + str(items['obj']['testVo']['id']) + '}, '
		# 			f.write(ids + json.dumps(items['obj']['testVo'], ensure_ascii=False).encode('utf-8') + '\n')
		# 			# f.write(json.dumps(items['obj']['testVo']).decode('unicode-escape').encode('utf-8') + '\n')
		# else if response.status == 404:
		# 	#写入未爬取的url
		# 	with open(failurefile, 'a+') as ff:
		# 		ff.write(response.url + '\n')

		if response.status == 200:
			details = json.loads(response.body)
			xingshulinItem = XingshulinItem()
			try:
				if details['obj'].has_key('testVo') == True:
					items = details['obj']['testVo']
					if 'id' in items:
						xingshulinItem['id'] = items['id']
						xingshulinItem['cname'] = "'" + items['cname'].encode('utf-8') + "'" if 'cname' in items else 'NULL'
						xingshulinItem['ename'] = "'" + items['ename'].encode('utf-8') + "'" if 'ename' in items else 'NULL'
						xingshulinItem['testName'] = "'" + items['testName'].encode('utf-8') + "'"  if 'testName' in items else 'NULL'
						xingshulinItem['testDescription'] =  "'" + items['testDescription'].encode('utf-8') + "'"  if 'testDescription' in items else 'NULL'
						xingshulinItem['sampleType'] = "'" + items['sampleType'].encode('utf-8') + "'" if 'sampleType' in items else 'NULL'
						xingshulinItem['normalValue'] = "'" + items['normalValue'].encode('utf-8') + "'" if 'normalValue' in items else 'NULL'
						xingshulinItem['normalValueDescription'] = "'" + items['normalValueDescription'].encode('utf-8') + "'" if 'normalValueDescription' in items else 'NULL'
						xingshulinItem['summary'] = "'" + items['summary'].encode('utf-8') + "'" if 'summary' in items else 'NULL'
						xingshulinItem['testWhys'] = "'" + items['testWhys'].encode('utf-8') + "'" if 'testWhys' in items else 'NULL'
						xingshulinItem['testWhen'] = "'" + items['testWhen'].encode('utf-8') + "'" if 'testWhen' in items else 'NULL'
						xingshulinItem['testPrinciple'] = "'" + items['testPrinciple'].encode('utf-8') + "'" if 'testPrinciple' in items else 'NULL'
						xingshulinItem['resultEffectReason'] = "'" + items['resultEffectReason'].encode('utf-8') + "'" if 'resultEffectReason' in items else 'NULL'
						xingshulinItem['diseaseRelated'] = "'" + items['diseaseRelated'].encode('utf-8') + "'" if 'diseaseRelated' in items else 'NULL'
						xingshulinItem['relationTest'] = "'" + items['relationTest'].encode('utf-8') + "'" if 'relationTest' in items else 'NULL'
						xingshulinItem['relationQuestion'] = "'" + items['relationQuestion'].encode('utf-8') + "'" if 'relationQuestion' in items else 'NULL'
						xingshulinItem['suffererPrepare'] = "'" + items['suffererPrepare'].encode('utf-8') + "'" if 'suffererPrepare' in items else 'NULL'
						for key in items:
							if key not in xingshulinItem:
								with open(misseditemfile, 'a+') as mf:
									mf.write(time.strftime('%Y-%m-%d %H:%m:%S',time.localtime(time.time())) + ', 遗漏字段: ' + str(key) + '\n')
								mf.close()
						return xingshulinItem
			except Exception, ex:
				with open(exceptionfile, 'a+') as ef:
					ef.write(time.strftime('%Y-%m-%d %H:%m:%S',time.localtime(time.time())) + ', 异常捕获: ' + str(ex) + '\n')
		elif response.status == 404:
			#写入未爬取的url
			with open(failurefile, 'a+') as ff:
				ff.write(time.strftime('%Y-%m-%d %H:%m:%S',time.localtime(time.time())) + ', 未爬取的url: ' + str(response.url) + '\n')

