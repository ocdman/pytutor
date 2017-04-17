# -*- coding: utf-8 -*-
import os
import scrapy
import json
import logging

from os import path
from tutorial.settings import DXY_COOKIES
from scrapy.http import FormRequest
from bs4 import BeautifulSoup
from tutorial.items import DxyDocumentItem

# set up logging to file
logging.basicConfig(
	filename='logging.txt',
	filemode = 'wb',
	format='%(asctime)s [%(name)s] %(levelname)s: %(message)s',
	level=logging.DEBUG
)

#查看当前的ip
class DxySpider(scrapy.Spider):
	name = 'dxy' 
	allowed_domains = ["dxy.cn"]

	def __init__(self):
		self.cookies = DXY_COOKIES
		self.headers = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
		}

	def start_requests(self):
		# yield FormRequest('http://down.dxy.cn/67245984-46ac-4883-9a1e-dd4927ac4404',
		# 	headers=self.headers,
		# 	cookies=self.cookies,
		# 	dont_filter=True,
		# 	callback=self.parseDownloadFile,
		# 	errback=self.errback_downloadFile)

		# yield FormRequest('http://d.dxy.cn/bbs/purchase/download/4622223/4622223/check?share=undefined',
		# 	headers=self.headers,
		# 	cookies=self.cookies,
		# 	dont_filter=True,
		# 	callback=self.parseDownloadFile,
		# 	errback=self.errback_downloadFile)

		for i in range(9, 0, -1):
			request = FormRequest('http://d.dxy.cn/search?tpg={0}&keyword=%E6%8A%91%E9%83%81%E7%97%87&free=on&ext=4'.format(i),
				headers=self.headers,
				cookies=self.cookies,
				callback=self.parseDocumentSearch)
			request.meta['classification'] = '抑郁症'
			yield request

	'''
	解析下载文档
	'''
	def parseDownloadFile(self, response):
		# name = response.url.split('/')[-1:][0] + '.pdf'
		# cwd = os.getcwd()
		# savePath = cwd + '\\tutorial\\pdfs\\' + name
		# logging.debug('save path: ' + savePath)
		id = response.meta['id']
		contentType = response.headers.get('Content-type')
		if contentType == 'application/octet-stream':
			documentItem = DxyDocumentItem()
			documentItem['id'] = id
			documentItem['byteContent'] = "'" + response.body.encode('base64') + "'"
			return documentItem
		else:
			logging.error('downloading %d fail, download timeout or url is not valid!' % id)

	def errback_downloadFile(self, failure):
		logging.error('response error: ' + response.body)

	'''
	根据DownloadUrl获取实际的pdf下载地址
	该地址由丁香园服务器随机生成一个guid
	并且该地址在几分钟后会过期
	'''
	def getValidDownloadUrl(self, response):
		result = json.loads(response.body)
		if('url' in result and 'username' in result):
			request = FormRequest(result['url'],
				headers=self.headers,
				cookies=self.cookies,
				callback=self.parseDownloadFile)
			request.meta['id'] = response.meta['id']
			yield request

	'''
	解析丁香文档搜索
	http://d.dxy.cn/
	启用Pipeline之后，正常情况下，一次请求返回一个Scrapy Item
	但是，使用yield而不是return，可以实现在一次请求中，返回多个Item
	'''
	def parseDocumentSearch(self, response):
		html = response.body
		soup = BeautifulSoup(html, 'lxml')
		resultItems = soup.find_all('div', attrs={'class':'resultItem'})
		downloadList = []
		classification = response.meta['classification']
		for resultItem in resultItems:
			item = self.dealSoupResultItem(resultItem, classification)
			downloadDict = {}
			downloadDict['id'] = item['id']
			downloadDict['url'] = item['downloadUrl'].replace("'","")
			downloadList.append(downloadDict)
			yield item
		#以下getValidDownloadUrl请求部分须得 yield item 全部同步完成之后才会执行
		for d in downloadList:
			request = FormRequest(d['url'],
				headers=self.headers,
				cookies=self.cookies,
				callback=self.getValidDownloadUrl)
			request.meta['id'] = d['id']
			yield request

	'''
	处理一次Item
	'''
	def dealSoupResultItem(self, resultItem, classification):
		hsubject = resultItem.find('a', attrs={'class':'hsubject'})
		info = resultItem.find('p', attrs={'class': 'info'})

		documentItem = DxyDocumentItem()
		id = hsubject['href'][8:]
		documentItem['id'] = int(id)
		documentItem['name'] = "'" + hsubject.text.encode('utf-8') + "'"
		documentItem['downloadUrl'] = "'" + 'http://d.dxy.cn/bbs/purchase/download/' + id+ '/' + id + '/check?share=undefined' + "'"
		documentItem['uploadTime'] = "'" + resultItem.h3.span.text.encode('utf-8') + "'"
		documentItem['description'] = "'" + resultItem.find('p', attrs={'class':'sum hdescription'}).text.encode('utf-8') + "'"
		documentItem['sourceType'] = "'" + resultItem.find('p', attrs={'class': 'sort'}).text.encode('utf-8') + "'"
		documentItem['user'] = "'" + 'http://d.dxy.cn' + info.a['href'].encode('utf-8') + "'"
		documentItem['size'] = "'" + info.i.text.encode('utf-8') + "'"
		documentItem['classification'] = "'" + classification + "'"
		return documentItem

