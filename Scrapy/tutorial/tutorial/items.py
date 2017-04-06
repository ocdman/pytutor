# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class XingshulinTestItem(scrapy.Item):
	id = scrapy.Field()
	#中文名
	cname = scrapy.Field()
	#英文名	
	ename = scrapy.Field()	
	#实验名
	testName = scrapy.Field()
	#临床意义
	testDescription = scrapy.Field()
	#样本类型
	sampleType = scrapy.Field()
	#参考范围
	normalValue = scrapy.Field()
	#常规描述
	normalValueDescription = scrapy.Field()
	#简介
	summary = scrapy.Field()
	#检查目的
	testWhys = scrapy.Field()
	#检查时机
	testWhen = scrapy.Field()
	#检验原理
	testPrinciple = scrapy.Field()
	#影响因素
	resultEffectReason = scrapy.Field()
	#相关疾病
	diseaseRelated = scrapy.Field()
	#相关实验
	relationTest = scrapy.Field()
	#相关问题
	relationQuestion = scrapy.Field()
	#患者准备
	suffererPrepare = scrapy.Field()
	#样本收集
	swatchGather = scrapy.Field()

class DmozItem(scrapy.Item):
	title = scrapy.Field()
	link = scrapy.Field()
	desc = scrapy.Field()

class XingshulinGuideItem(scrapy.Item):
	id = scrapy.Field()
	#指南名
	guideName = scrapy.Field()
	#发表年
	year = scrapy.Field()
	#组织
	organization = scrapy.Field()
	#简介
	summary = scrapy.Field()
	#发表日期
	publishedDate = scrapy.Field()
	#pdf链接
	pdfLink = scrapy.Field()
	#epub链接
	epubLink = scrapy.Field()
	#杂志
	journal = scrapy.Field()
	#作者
	author = scrapy.Field()
	#量
	volume = scrapy.Field()
	#期号
	issue = scrapy.Field()
	#下载次数
	downloadCount = scrapy.Field()

class WanfangExaminationItem(scrapy.Item):
	ID = scrapy.Field()
	RecordType = scrapy.Field()
	CName = scrapy.Field()
	EName = scrapy.Field()
	NameInfo = scrapy.Field()
	Summarize = scrapy.Field()
	Indication = scrapy.Field()
	Reference = scrapy.Field()
	Clinical = scrapy.Field()
	Samples = scrapy.Field()
	Precautions = scrapy.Field()
	Category = scrapy.Field()
	Initial = scrapy.Field()
	ArticleCount = scrapy.Field()
	CategoryShort = scrapy.Field()
	CategoryRoot = scrapy.Field()
	Author = scrapy.Field()
	Checker = scrapy.Field()
		

