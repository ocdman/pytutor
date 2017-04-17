# -*- coding: utf-8 -*-

# Scrapy settings for tutorial project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'tutorial'

SPIDER_MODULES = ['tutorial.spiders']
NEWSPIDER_MODULE = 'tutorial.spiders'
DEFAULT_REQUEST_HEADERS = {
	# 'Referer': "http://www.xingshulin.com/searchTest.html"
}
ITEM_PIPELINES = {
   'tutorial.pipelines.TutorialPipeline': 300
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tutorial (+http://www.yourdomain.com)'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS=32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY=1
## DOWNLOAD_TIMEOUT=10
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN=16
#CONCURRENT_REQUESTS_PER_IP=16
# CONCURRENT_REQUESTS_PER_DOMAIN=2

# Disable cookies (enabled by default)
COOKIES_ENABLED=True
COOKIES = {
	'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%221567c6a24f31-01bbcfa02f3c52-36677f02-1024000-1567c6a24f4253%22%7D',
	'X-Security-Id': 'B81F6C2B576EF75C079ABE9ECF445238',
	'X-User-Agent': '"www/1.0.0 (Macintosh, Intel Mac OS X 10_10_4) net/unkown"',
	'Hm_lvt_bf235f0a5667df7b3b27f35da3ad77cf': '1490447454',
	'Hm_lpvt_bf235f0a5667df7b3b27f35da3ad77cf': '1490447454',
	'X-User-Token': '7B383836383932616165383038346264366230663238316435356631636136623562373732392A72305832526C44584F635171574C52475943306F4B524B5A396D7D2C7B42383146364332423537364546373543303739414245394543463434353233387D2C7B747275657D2C7B3130307D2C7B323130313137397D2C7B386433363866383064323262343139636236643136383764333639653366303654547A39504472594F54703D4E564C30794C6A595A56754249407A71417161337D2C7B35333635636566386636353965346361323165663464373766353333316233397D2C7B323031372D30332D32352032313A31313A31327D2C7B312E302E307D2C7B7777777D2C7B7777775F312E302E302D4F53585F31305F31305F347D'
}
WANFANG_COOKIES = {
	'Hm_lpvt_af200f4e2bd61323503aebc2689d62cb': '1491014974',
	'Hm_lvt_af200f4e2bd61323503aebc2689d62cb': '1491014406',
	'WFKS.Auth': '%7b%22Context%22%3a%7b%22AccountIds%22%3a%5b%5d%2c%22Data%22%3a%5b%5d%2c%22SessionId%22%3a%224dc682a1-436f-4e87-9501-90f93dc4c2f0%22%2c%22Sign%22%3a%22hi+authserv%22%7d%2c%22LastUpdate%22%3a%222017-04-01T02%3a39%3a15Z%22%2c%22TicketSign%22%3a%22ucqLvG96FdQJnf%5c%2fLP5eCFA%3d%3d%22%7d',
	'WFMed.Auth': '%7b%22Context%22%3a%7b%22AccountIds%22%3a%5b%22MedPerson.chilihotpot%22%5d%2c%22Data%22%3a%5b%7b%22Key%22%3a%22MedPerson.chilihotpot.DisplayName%22%2c%22Value%22%3a%22%22%7d%5d%2c%22SessionId%22%3a%22485a62c6-c64f-48e6-8c8a-a9685e696af1%22%2c%22Sign%22%3a%22RD6CdZMNAqICZXw41MLynKZoqxeoC7qxMdR6QLZuN2YrgxyZ0fDFU8ZSmR3u1307%22%7d%2c%22LastUpdate%22%3a%222017-04-01T06%3a54%3a45Z%22%2c%22TicketSign%22%3a%222fDjPsfPOzNVSHSamC4X3g%3d%3d%22%7d'
}
XUEQIU_COOKIES = {
	'aliyungf_tc': 'AQAAAKsLZwTbJg0Ap3ZRZSG5MJ23v/Np',
	'xq_a_token': 'ca292f8d934efc28f3fd052b7dcf46f14a20a0d3',
	'xq_a_token.sig': 'OfkwBmKBwnYETfT5NOuElwVwhBY',
	'xq_r_token': 'd1accc7b0cafd743be1b975a863a146e514d9c80',
	'xq_r_token.sig': 'LV5APomGXuF1PJGnH9SmAPdxYHc',
	'u': '771492072769082',
	'Hm_lvt_1db88642e346389874251b5a1eded6e3': '1492061072,1492062559,1492070685,1492071572',
	'Hm_lpvt_1db88642e346389874251b5a1eded6e3': '1492072769'
}
DXY_COOKIES = {
	"DXY_USER_GROUP": "78",
	"JUTE_SESSION_ID": "4ea06fad-c0b0-4587-a402-7e4f6ed1c766"

	# "CMSSESSIONID": "35C2D65832F32B31E111DD565F8834C8-n1",
	# "DRUGSSESSIONID": "3C8D74F425C1AA684186EDEDE962B290-n1",
	# "JUTE_BBS_DATA": "4cd5fb2f746476144425a1445d16878b17dcd03e57097155baca6029379042419df30a23e856b408f42057bdd7d6ff8c454d0311029f5703f4542debc65973b3012ee04393fb8889f0008ea330829f1f"
}
# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED=False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'tutorial.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'tutorial.middlewares.HttpProxyMiddleware': 543,
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
   # 'tutorial.pipelines.SomePipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# NOTE: AutoThrottle will honour the standard settings for concurrency and delay
#AUTOTHROTTLE_ENABLED=True
# The initial download delay
#AUTOTHROTTLE_START_DELAY=5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY=60
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG=False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED=True
#HTTPCACHE_EXPIRATION_SECS=0
#HTTPCACHE_DIR='httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES=[]
#HTTPCACHE_STORAGE='scrapy.extensions.httpcache.FilesystemCacheStorage'

#日志设置
# LOG_FILE = 'logging.txt'
# LOG_LEVEL = 'DEBUG'

#数据库相关
CUST_SERVER = '192.168.118.138'
CUST_USER = 'sa'
CUST_PWD = 'Password01!'
CUST_DB = 'clinKnowledge1'