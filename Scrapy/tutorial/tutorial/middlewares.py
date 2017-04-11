# -*- coding: utf-8 -*-
import os
import logging
import fetch_free_proxyes

from twisted.web._newclient import ResponseNeverReceived
from twisted.internet.error import TimeoutError, ConnectionRefusedError, ConnectError
from datetime import datetime, timedelta

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

class MyCustomDownloaderMiddleware(object):
	DONT_RETRY_ERRORS = (TimeoutError, ConnectionRefusedError, ResponseNeverReceived, ConnectError, ValueError)

	def __init__(self):
		print 'use http proxy'
		# 初始化代理列表
		self.proxyes = [{'proxy': None, 'valid': True, 'count': 0}]
		# 存放代理列表的文件，每行一个代理，格式为ip:port
		self.proxy_file = 'proxyes.dat'
		# 初始时使用0号代理（即无代理）
		self.proxy_index = 0
		# 保存上次不用代理直接连接的时间点
		self.last_no_proxy_time = datetime.now()
		# 一定分钟数后切换回不用代理，因为用代理影响速度
		self.recover_no_proxy_interval = 20
		# 表示可信的代理的数量（如自己搭建的http代理）
		self.fixed_proxy = len(self.proxyes)
		# 从文件读取初始代理
		if os.path.exists(self.proxy_file):
			with open(self.proxy_file, 'r') as fd:
				lines = fd.readlines()
				for line in lines:
					line = line.strip()
					if not line or self.url_in_proxyes('http://' + line):
						continue
					self.proxyes.append({'proxy': 'http://' + line,
						'valid': True,
						'count': 0})

	'''
	返回一个代理url是否在代理列表中
	'''
	def url_in_proxyes(self, url):
		for p in self.proxyes:
			if url == p['proxy']:
				return True
		return False

	# def invalid_proxy(self, index):
		#可信代理
		# if index < self.fixed_proxy:

	'''
	将request设置使用当前的或下一个有效的代理
	'''
	def set_proxy(self, request):
		proxy = self.proxyes[self.proxy_index]
		logging.info(proxy)
		# if not proxy['valid']:

		# 每次不用代理直接下载时更新self.last_no_proxy_time
		if self.proxy_index == 0:
			self.last_no_proxy_time = datetime.now()

		if proxy['proxy']:
			request.meta['proxy'] = proxy['proxy']
		elif 'proxy' in request.meta.keys():
			del request.meta['proxy']
		request.meta['proxy_index'] = self.proxy_index
		proxy['count'] += 1

	'''
	overwrite process request
	'''
	def process_request(self, request, spider):
		#set the location of the proxy
		# request.meta['proxy'] = "http://YOUR_PROXY_IP:PORT"
		# request.meta['proxy'] = "http://123.57.35.17:80"
		# request.meta['proxy'] = "http://127.0.0.1:8087/"

		if self.proxy_index > 0 and datetime.now() > (self.last_no_proxy_time + timedelta(minutes=self.recover_no_proxy_interval)):
			logging.info('After %d minutes later, recover from using proxy' % self.recover_no_proxy_interval)
			self.last_no_proxy_time = datetime.now()
			self.proxy_index = 0

		request.meta['dont_redirect'] = True # 有些代理会把请求重定向到一个莫名的地址

		if 'change_proxy'in request.meta.keys() and request.meta['change_proxy']:
			logging.info('change proxy request get by spider: %s' % request)
			# self.invalid_proxy(request.meta['proxy_index'])

		logging.info(request.meta.keys())

		self.set_proxy(request)



