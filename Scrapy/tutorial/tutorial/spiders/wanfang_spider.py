# -*- coding: utf-8 -*-
import scrapy
import logging
import json

from tutorial.items import *
from tutorial.settings import WANFANG_COOKIES
from scrapy.utils.log import configure_logging
from scrapy.http import FormRequest
from scrapy import Selector

#将标准输出流同步到日志文件里
configure_logging(install_root_handler=False)
logging.basicConfig(
	filename='logging.txt',
	filemode = 'wb',
	format='%(asctime)s [%(name)s] %(levelname)s: %(message)s',
	level=logging.WARNING	#level not work
)

class WanfangSpider(scrapy.Spider):
	name = "wanfang"
	# allowed_domains = ["lczl.med.wanfangdata.com.cn"]
	# start_urls = ['http://lczl.med.wanfangdata.com.cn']

	def __init__(self):
		self.cookies = WANFANG_COOKIES

	def start_requests(self):
		#检验
		for i in range(62, 67, 1):
			request = FormRequest("http://lczl.med.wanfangdata.com.cn/Home/SearchTotal",
				cookies=self.cookies,
				formdata={'initial': '0', 'category': 'Examination', 'id': str(i)},
				callback=self.parseTotal)
			request.meta['id'] = str(i)
			yield request

	#步骤一：先根据id号解析条数
	def parseTotal(self, response):
		id = response.meta['id']
		pageSize = response.body
		logging.info('id:' + id + ', pageSize:' + pageSize)
		yield FormRequest("http://lczl.med.wanfangdata.com.cn/Home/SearchResultList",
			cookies=self.cookies,
			formdata={'type':'Examination', 'initial': '0', 'category': 'Examination', 'id': id, 'page': '0', 'pageSize': pageSize},
			callback=self.parseResultList)

	#步骤二：根据id号和条数，解析具体检查项目名称
	def parseResultList(self, response):
		 resultList = response.xpath('//a/text()').extract()

		 for result in resultList:
		 	yield FormRequest("http://lczl.med.wanfangdata.com.cn/Home/JsonSearch/{0}?category=Examination&page=0&c=".format(result.encode('utf-8')),
		 		cookies=self.cookies,
		 		formdata={'category': 'Examination', 'page': '0', 'c': ''},
		 		callback=self.parseJson)

	#步骤三：根据具体检查项目名称，解析JSON格式检查结果
	def parseJson(self, response):
		if response.status == 200:
			logging.info(response.body)
			try:
				result = json.loads(response.body)
				examItem = WanfangExaminationItem()
				if isinstance(result, list) == True:
					for items in result:
						if 'ID' in items:
							examItem['ID'] = "'" + items['ID'] + "'"
							examItem['RecordType'] = "'" + items['__RecordType__'].encode('utf-8').replace("'","''") + "'" if '__RecordType__' in items else 'NULL'
							examItem['Summarize'] =  "'" + items['Summarize'].encode('utf-8').replace("'","''") + "'" if 'Summarize' in items else 'NULL'
							examItem['Indication'] =  "'" + items['Indication'].encode('utf-8').replace("'","''") + "'" if 'Indication' in items else 'NULL'
							examItem['Reference'] =  "'" + items['Reference'].encode('utf-8').replace("'","''") + "'" if 'Reference' in items else 'NULL'
							examItem['Clinical'] =  "'" + items['Clinical'].encode('utf-8').replace("'","''") + "'" if 'Clinical' in items else 'NULL'
							examItem['Samples'] =  "'" + items['Samples'].encode('utf-8').replace("'","''") + "'" if 'Samples' in items else 'NULL'
							examItem['Precautions'] =  "'" + items['Precautions'].encode('utf-8').replace("'","''") + "'" if 'Precautions' in items else 'NULL'
							examItem['Initial'] = "'" + items['Initial'].encode('utf-8').replace("'","''") + "'" if 'Initial' in items else 'NULL'
							examItem['ArticleCount'] = "'" + items['ArticleCount'].encode('utf-8').replace("'","''") + "'" if 'ArticleCount' in items else 'NULL'
							examItem['CategoryShort'] = "'" + items['CategoryShort'].encode('utf-8') .replace("'","''")+ "'" if 'CategoryShort' in items else 'NULL'
							examItem['CategoryRoot'] = "'" + items['CategoryRoot'].encode('utf-8').replace("'","''") + "'" if 'CategoryRoot' in items else 'NULL'
							
							# examItem['Name'] = "'" + '|'.join(x.encode('utf-8').replace("'","''") for x in items['Name']) + "'" if 'Name' in items and isinstance(items['Name'], list) else 'NULL'
							#将Name拆分成中英文
							examItem['CName'] = "'" + items['Name'][0].encode('utf-8').replace("'","''") + "'" if 'Name' in items else 'NULL'
							examItem['EName'] = "'" + items['Name'][1].encode('utf-8').replace("'","''") + "'" if 'Name' in items else 'NULL'
							
							examItem['NameInfo'] = "'" + '|'.join(x.encode('utf-8').replace("'","''") for x in items['NameInfo']) + "'" if 'NameInfo' in items and isinstance(items['NameInfo'], list) else 'NULL'
							examItem['Category'] = "'" + ','.join(x.encode('utf-8').replace("'","''") for x in items['Category']) + "'" if 'Category' in items and isinstance(items['Category'], list) else 'NULL'
							examItem['Author'] = "'" + ','.join(x.encode('utf-8').replace("'","''") for x in items['Author']) + "'" if 'Author' in items and isinstance(items['Author'], list) else 'NULL'
							examItem['Checker'] = "'" + ','.join(x.encode('utf-8').replace("'","''") for x in items['Checker']) + "'" if 'Checker' in items and isinstance(items['Checker'], list) else 'NULL'
							# for key in items:
							# 	if key not in examItem and key != '__RecordType__':
							# 		#写入遗漏的字段
							# 		logging.warning('遗漏字段: ' + str(key) + '\n')
							return examItem
			except Exception, ex:
				#写入异常捕获
				logging.error('异常捕获: ' + str(ex) + '\n')
		elif response.status == 404:
			logging.warning('未爬取的url: ' + str(response.url) + '\n')




