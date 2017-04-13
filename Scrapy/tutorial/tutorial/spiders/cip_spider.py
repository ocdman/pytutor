# -*- coding: utf-8 -*-
import scrapy
import re

from scrapy import FormRequest

#查看当前的ip
class CipSpider(scrapy.Spider):
	name = 'cip' 
	allowed_domains = ["cip.cc"]
	# start_urls = [
	# 	'http://www.cip.cc/'
	# ]

	# def parse(self, response):
	# 	print 'ip地址: ' + re.search('\d+\.\d+\.\d+\.\d+', response.body).group(0)

	def start_requests(self):
		yield FormRequest("http://www.cip.cc/",
			callback=self.parseIP)

	def parseIP(self, response):
		print response.body