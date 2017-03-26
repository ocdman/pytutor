# -*- coding: utf-8 -*-
import scrapy
import json
import time

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
	# start_urls = [
	# 	"http://www.xingshulin.com/searchTest.html"
	# ]

	def __init__(self):
		self.cookies = COOKIES
		#清空文件，如果没有文件则创建
		f = open(filename, 'wb')
		f.close()
		ff = open(failurefile, 'wb')
		ff.close()

	def start_requests(self):
		for i in range(10, 0, -1):
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
		if response.status == 200:
			items = json.loads(response.body)
			if items['obj'].has_key('testVo') == True:
				with open(filename, 'a+') as f:
					ids = '{id: ' + str(items['obj']['testVo']['id']) + '}, '
					f.write(ids + json.dumps(items['obj']['testVo'], ensure_ascii=False).encode('utf-8') + '\n')
					# f.write(json.dumps(items['obj']['testVo']).decode('unicode-escape').encode('utf-8') + '\n')
		else:
			#写入未爬取的url
			with open(failurefile, 'a+') as ff:
				ff.write(response.url + '\n')

		# items = json.loads(response.body)
		# xingshulinItem = XingshulinItem()

		# if 'id' in items:
		# 	xingshulinItem['id'] = items['id']
		# 	xingshulinItem['cname'] = "'" + items['cname'].encode('utf-8') + "'"
		# 	xingshulinItem['ename'] = "'" + items['ename'].encode('utf-8') + "'" if 'ename' in items else 'NULL'
		# 	xingshulinItem['testName'] = "'" + items['testname'].encode('utf-8') + "'"  if 'testname' in items else 'NULL'
		# 	xingshulinItem['testDescription'] =  "'" + items['testdescription'].encode('utf-8') + "'"  if 'testdescription' in items else 'NULL'
		# 	xingshulinItem['sampleType'] = "'" + items['sampletype'].encode('utf-8') + "'" if 'sampletype' in items else 'NULL'
		# 	xingshulinItem['normalValue'] = "'" + items['normalvalue'].encode('utf-8') + "'" if 'normalvalue' in items else 'NULL'
		# 	xingshulinItem['normalValueDescription'] = "'" + items['normalvaluedescription'].encode('utf-8') + "'" if 'normalvaluedescription' in items else 'NULL'
		# 	xingshulinItem['summary'] = "'" + items['summary'].encode('utf-8') + "'" if 'summary' in items else 'NULL'
		# 	xingshulinItem['testWhys'] = "'" + items['testwhys'].encode('utf-8') + "'" if 'testwhys' in items else 'NULL'
		# 	xingshulinItem['testWhen'] = "'" + items['testwhen'].encode('utf-8') + "'" if 'testwhen' in items else 'NULL'
		# 	xingshulinItem['testPrinciple'] = "'" + items['testprinciple'].encode('utf-8') + "'" if 'testprinciple' in items else 'NULL'
		# 	xingshulinItem['resultEffectReason'] = "'" + items['resulteffectreason'].encode('utf-8') + "'" if 'resulteffectreason' in items else 'NULL'
		# 	xingshulinItem['diseaseRelated'] = "'" + items['diseaserelated'].encode('utf-8') + "'" if 'diseaserelated' in items else 'NULL'
		# 	xingshulinItem['relationTest'] = "'" + items['relationtest'].encode('utf-8') + "'" if 'relationtest' in items else 'NULL'
		# 	xingshulinItem['relationQuestion'] = "'" + items['relationquestion'].encode('utf-8') + "'" if 'relationquestion' in items else 'NULL'
		# 	return xingshulinItem

