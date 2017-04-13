# -*- coding: utf-8 -*-
import scrapy
import json
import logging

from tutorial.settings import XUEQIU_COOKIES
from scrapy.http import FormRequest

# set up logging to file
logging.basicConfig(
	filename='logging.txt',
	filemode = 'wb',
	format='%(asctime)s [%(name)s] %(levelname)s: %(message)s',
	level=logging.DEBUG
)
# set up logging to console
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
# set a format which is simpler for console use
formatter = logging.Formatter('%(asctime)s [%(name)s] %(levelname)s: %(message)s')
console.setFormatter(formatter)
# add the handler to the root logger
logging.getLogger('').addHandler(console)

#查看当前的ip
class XueqiuSpider(scrapy.Spider):
	name = 'xueqiu' 
	# allowed_domains = ["xueqiu.com"]
	# start_urls = [
	# 	'https://xueqiu.com/'
	# ]

	def __init__(self):
		self.cookies = XUEQIU_COOKIES
		self.headers = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
		}

	def start_requests(self):
		# for i in range(5, 0, -1):
		# 	request = FormRequest('https://xueqiu.com/stock/forchart/stocklist.json?symbol=SH000001&period=1d',
		# 		headers={
		# 			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
		# 		},
		# 		cookies=self.cookies,
		# 		dont_filter=True,
		# 		callback=self.parseShStock,
		# 		errback=self.errback_shStock)

		# 	request.meta['i'] = str(i)
		# 	yield request

		for i in range(5, 0, -1):

			shRequest = FormRequest("https://xueqiu.com/v4/stock/quote.json?code=SH000001&_={0}".format(i),
				dont_filter=True,
				headers=self.headers,
				cookies=self.cookies,
				callback=self.parseShStock)
			shRequest.meta['i'] = str(i)
			yield shRequest

			szRequest = FormRequest("https://xueqiu.com/v4/stock/quotec.json?code=SZ399006&_={0}".format(i),
				dont_filter=True,
				headers=self.headers,
				callback=self.parseSzStock)
			szRequest.meta['i'] = str(i)
			yield szRequest

			hkRequest = FormRequest("https://xueqiu.com/v4/stock/quote.json?code=HKHSI&_={0}".format(i),
				dont_filter=True,
				headers=self.headers,
				callback=self.parseHkStock)
			hkRequest.meta['i'] = str(i)
			yield hkRequest

	#解析上证指数
	def parseShStock(self, response):
		logging.info('SH STOCK, i: ' + response.meta['i'] + ', response: ' + response.body)

	def errback_shStock(self, failure):
		logging.error(failure.value.response.body)

	#解析创业板指
	def parseSzStock(self, response):
		logging.info('SZ STOCK, i: ' + response.meta['i'] + ', response: ' + response.body)

	#解析恒生指数
	def parseHkStock(self, response):
		logging.info('HK STOCK, i: ' + response.meta['i'] + ', response: ' + response.body)