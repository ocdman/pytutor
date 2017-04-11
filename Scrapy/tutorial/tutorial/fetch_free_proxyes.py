# -*- coding: utf-8 -*-
import logging
import urllib2

from bs4 import BeautifulSoup

# set up logging to file
logging.basicConfig(
	filename='logging.txt',
	filemode = 'wb',
	format='%(asctime)s [%(name)s] %(levelname)s: %(message)s',
	level=logging.DEBUG	#level not work
)

def get_html(url):
	request = urllib2.Request(url)
	request.add_header("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.99 Safari/537.36")
	html = urllib2.urlopen(request)
	return html.read()

def get_soup(url):
	soup = BeautifulSoup(get_html(url), 'lxml')
	return soup

def fetch_xici():
	'''
	http://www.xicidaili.com/nn/
	'''
	proxyes = []
	try:
		url = 'http://www.xicidaili.com/nn/'
		soup = get_soup(url)
		table = soup.find('table', attrs={'id':'ip_list'})
		trs = table.find_all('tr')
		for i in range(1, len(trs)):
			tr = trs[i]
			tds = tr.find_all('td')
			ip = tds[1].text	#ip
			port = tds[2].text	#端口
			speed = tds[6].div['title'][:-1]	#速度
			latency = tds[7].div['title'][:-1]	#连接时间
			if float(speed) < 3 and float(latency) < 1:
				proxyes.append('%s:%s' % (ip, port))
	except Exception, ex:
		logging.warning('fail to fetch from xici, error: ' + str(ex))
	return proxyes

if __name__ == '__main__':
	# set up logging to console
	console = logging.StreamHandler()
	console.setLevel(logging.DEBUG)
	# set a format which is simpler for console use
	formatter = logging.Formatter('%(asctime)s [%(name)s] %(levelname)s: %(message)s')
	console.setFormatter(formatter)
	# add the handler to the root logger
	logging.getLogger('').addHandler(console)

	proxyes = fetch_xici()
	logging.info(proxyes)