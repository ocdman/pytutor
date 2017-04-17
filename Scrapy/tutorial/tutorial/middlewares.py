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

class HttpProxyMiddleware(object):
	# 遇到这些类型的错误直接当作代理不可用处理掉，不再传给 retrymiddleware
	DONT_RETRY_ERRORS = (TimeoutError, ConnectionRefusedError, ResponseNeverReceived, ConnectError, ValueError)

	def __init__(self):
		print 'use http proxy'
		# 初始化代理列表
		self.proxyes = [{'proxy': None, 'valid': True, 'count': 0}]
		# 存放代理列表的文件，每行一个代理，格式为ip:port
		self.proxy_file = 'proxyes.dat'
		# 初始时使用0号代理（即无代理）
		self.proxy_index = 0
		# 保存上次不用代理直连的时间点
		self.last_no_proxy_time = datetime.now()
		# 一定分钟数后切换回不用代理，因为用代理影响速度
		self.recover_no_proxy_interval = 20
		# 表示可信任的代理的数量（如自己搭建的http代理）+不用代理直连
		self.fixed_proxy = len(self.proxyes)
		# 当有效代理小于这个数时（包括直连），从网上抓取新的代理，可以将这个数设为为了满足每个ip被要求输入验证码后得到足够休息时间所需要的代理数
		# 例如爬虫在十个可用代理之间切换时，每个ip经过数分钟才轮到自己一次，这样就能get一些请求而不用输入验证码了
		# 如果这个数过小，例如两个，爬虫用A ip爬了没几个就被禁，换了一个又爬了次又被禁，这样整个爬虫就会处于一种忙等待的状态，影响效率
		self.extend_proxy_threshold = 10
		# 一个代理如果没用到这个数字就被发现老是超时，则永久移除该代理。
		# 设置为0则不会修改代理文件
		self.dump_count_threshold = 20
		# 上一次抓新代理的时间
		self.last_fetch_proxy_time = datetime.now()
		# 是否在超时的情况下禁用代理
		self.invalid_proxy_flag = True
		# 一个被设为invalid的代理如果已经成功爬取大于这个参数的页面，将不会被invalid
		self.invalid_proxy_threshold = 200
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

	'''
	返回代理列表中有效的代理数量
	'''
	def len_valid_proxy(self):
		count = 0
		for p in self.proxyes:
			if p['valid']:
				count += 1
		return count

	'''
	将所有count >= 指定阈值的代理重置为valid
	'''
	def reset_proxyes(self):
		logging.info('reset proxyes to valid')
		for p in self.proxyes:
			if p['count'] >= self.dump_count_threshold:
				p['valid'] = True

	'''
	保存代理列表中有效的代理到文件
	'''
	def dump_valid_proxy(self):
		if self.dump_count_threshold <= 0:
			return
		logging.info('dump proxyes to file')
		with open(self.proxy_file, 'w') as fd:
			for i in range(self.fixed_proxy, len(self.proxyes)):
				p = self.proxyes[i]
				if p['valid'] or p['count'] >= self.dump_count_threshold:
					logging.info(p['proxy'] + '\n')
					# 只保存有效的代理
					fd.write(p['proxy'][7:] + '\n')

	'''
	从网上抓取新的代理添加到代理列表里
	'''
	def fetch_new_proxyes(self):
		logging.info('extending proxyes using fetch_new_proxyes.py')
		new_proxyes = fetch_free_proxyes.fetch_xici()
		logging.info('new proxyes: %s' % new_proxyes)
		self.last_fetch_proxy_time = datetime.now()

		for np in new_proxyes:
			if self.url_in_proxyes('http://' + np):
				continue
			else:
				self.proxyes.append({'proxy': 'http://' + np,
					'valid': True,
					'count': 0})

		# 如果发现抓不到新的代理了，缩小阈值以避免白费功夫
		if self.len_valid_proxy() < self.extend_proxy_threshold:
			self.extend_proxy_threshold -= 1

	'''
	将index指向的代理设置为invalid
	并调整当前的proxy_index到下一个有效代理的位置
	'''
	def invalid_proxy(self, index):
		# 可信代理永远不会为invalid
		if index < self.fixed_proxy:
			self.inc_proxy_index()
			return

		if self.proxyes[index]['valid']:
			logging.info('invalidate %s' % self.proxyes[index])
			self.proxyes[index]['valid'] = False
			if index == self.proxy_index:
				self.inc_proxy_index()

			if self.proxyes[index]['count'] < self.dump_count_threshold:
				self.dump_valid_proxy()

	'''
	将代理列表的索引移到下一个有效代理的位置
	如果发现代理列表只有fixed_proxy项有效，重置代理列表
	'''
	def inc_proxy_index(self):
		assert self.proxyes[0]['valid']
		while True:
			self.proxy_index = (self.proxy_index + 1) % len(self.proxyes)
			if self.proxyes[self.proxy_index]['valid']:
				break

		# 两轮直连的时间间隔过短，说明出现验证码抖动，扩充代理列表
		if self.proxy_index == 0 and datetime.now() < self.last_no_proxy_time + timedelta(minutes=2):
			logging.info('captcha thrashing')
			self.fetch_new_proxyes()

		# 如果代理列表中有效的代理不足的话，重置为 valid
		if self.len_valid_proxy() <= self.fixed_proxy or self.len_valid_proxy() < self.extend_proxy_threshold:
			self.reset_proxyes()

		# 代理数量仍然不足，抓取新的代理
		if self.len_valid_proxy() <= self.extend_proxy_threshold:
			logging.info('valid proxy < threshold: %d/%d' % (self.len_valid_proxy(), self.extend_proxy_threshold))
			self.fetch_new_proxyes()

		logging.info('now using new proxy: %s, proxy_index is %d' % (self.proxyes[self.proxy_index]['proxy'], self.proxy_index))

	'''
	将request设置使用当前的或下一个有效的代理
	'''
	def set_proxy(self, request):
		proxy = self.proxyes[self.proxy_index]

		if not proxy['valid']:
			self.inc_proxy_index()
			proxy = self.proxyes[self.proxy_index]

		logging.debug(proxy)

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
	讲request设置为使用代理
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

		# spider发现ip被禁,要求更换代理(change_proxy在具体的spider里设置,因为不同网站ip被禁response不同)
		if 'change_proxy'in request.meta.keys() and request.meta['change_proxy']:
			logging.info('change proxy request get by spider: %s' % request)
			self.invalid_proxy(request.meta['proxy_index'])
			request.meta['change_proxy'] = False

		logging.debug(request.meta.keys())

		self.set_proxy(request)

	'''
	检查response.status，根据status是否在允许的状态码中决定是否切换到下一个代理，或者禁用代理
	'''
	def process_response(self, request, response, spider):
		if 'proxy' in request.meta.keys():
			logging.debug('%s %s %s' % (request.meta['proxy'], response.status, request.url))
		else:
			logging.debug('None %s %s' % (response.status, request.url))

		if response.status != 200 \
			and (not hasattr(spider, 'website_possible_httpstatus_list') \
				or response.status not in spider.website_possible_httpstatus_list):
			logging.info('response status not in spider.website_possible_httpstatus_list')
			self.invalid_proxy(request.meta['proxy_index'])
			new_request = request.copy()
			new_request.dont_filter = True
			return new_request
		else:
			return response

	'''
	处理由于使用代理导致的连接异常
	'''
	def process_exception(self, request, exception, spider):
		logging.debug('%s exception: %s', (self.proxyes[request.meta['proxy_index']]['proxy'], exception))
		request_proxy_index = request.meta['proxy_index']

		# 只有当 proxy_index > fixed_proxy - 1 的情况下才进行比较，至少确保本地直连是存在的
		if isinstance(exception, self.DONT_RETRY_ERRORS):
			# WARN: 直连时超时的话换个代理还是重试，这是个策略问题
			if request_proxy_index > self.fixed_proxy - 1 and self.invalid_proxy_flag:
				if self.proxyes[request_proxy_index]['count'] < self.invalid_proxy_threshold:
					logging.info('exception occure when proxy connection, invalid proxy')
					self.invalid_proxy(request_proxy_index)
				elif request_proxy_index == self.proxy_index:	# 虽然超时，但是如果之前一直很好用的话，也不设为invalid
					logging.info('exception occure when proxy connection but proxy_index_count > invalid_proxy_threshold, inc proxy index')
					self.inc_proxy_index()
			else:	# 简单的切换而不禁用
				if request_proxy_index == self.proxy_index:
					logging.info('exception occure when proxy connection, inc proxy index')
					self.inc_proxy_index()
			new_request = request.copy()
			new_request.dont_filter = True
			return new_request

class MyCustomDownloaderMiddleware(object):

	def __init__(self):
		print 'use http proxy'
	
	def process_request(self, request, spider):
		request.meta['proxy'] = "http://127.0.0.1:8087/"

	def process_response(self, request, response, spider):
		logging.info(response.body)
		return response



