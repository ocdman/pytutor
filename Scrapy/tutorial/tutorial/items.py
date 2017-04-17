# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#杏树林-检查 & 检验类
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

#杏树林-指南类
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

#杏树林-中药类
class XingshulinChineseMedicineItem(scrapy.Item):
	id = scrapy.Field()
	#中药名
	name = scrapy.Field()
	#拼音
	pinyin = scrapy.Field()
	#别名
	alias = scrapy.Field()
	#来源
	source = scrapy.Field()
	#采收炮制
	harvestPreparation = scrapy.Field()
	#商品规格
	commercialSpecification = scrapy.Field()
	#性味
	properties = scrapy.Field()
	#归经
	channelsTropism = scrapy.Field()
	#功效
	functions = scrapy.Field()
	#主治
	indications = scrapy.Field()
	#用法用量
	dosage = scrapy.Field()
	#使用注意
	cautions = scrapy.Field()
	#药论
	commentary = scrapy.Field()
	#化学成分
	chemicalCompositions = scrapy.Field()
	#药理作用
	pharmacologicalEffects = scrapy.Field()
	#药效学
	pharmacodynamics = scrapy.Field()
	#临床报道
	clinicalReports = scrapy.Field()
	#不良反应
	toxicity = scrapy.Field()
	#参考文献
	references = scrapy.Field()

#杏树林-西药 & 中成药类
class XingshulinDrugItem(scrapy.Item):
	id = scrapy.Field()
	#药名
	commonName = scrapy.Field()
	#药英文名
	englishCommonName = scrapy.Field()
	#商品名称
	tradeName = scrapy.Field()
	#商品英文名称
	englishTradeName = scrapy.Field()
	#别名
	aliasName = scrapy.Field()
	#商品标记
	tradeMark = scrapy.Field()
	#主要成分
	mainIngredient = scrapy.Field()
	#性状
	description = scrapy.Field()
	#适应症
	indication = scrapy.Field()
	#规格
	specification = scrapy.Field()
	#用法用量
	dosage = scrapy.Field()
	#禁忌
	taboo = scrapy.Field()
	#注意事项
	other = scrapy.Field()
	#药物相互作用
	interaction = scrapy.Field()
	#贮藏
	storage = scrapy.Field()
	#生产厂家
	manufacturer = scrapy.Field()
	#执行标准
	executiveStandard = scrapy.Field()
	#有效期
	period = scrapy.Field()
	#老年用药
	geriatricUse = scrapy.Field()
	#药代动力学
	pharmacokinetics = scrapy.Field()
	#孕妇及哺乳期妇女用药
	pregnantLactatingUse = scrapy.Field()
	#不良反应
	sideEffect = scrapy.Field()
	#批准日期
	approvalDate = scrapy.Field()
	#儿童用药
	pediatricUse = scrapy.Field()
	#药物过量
	overdose = scrapy.Field()
	#药理毒理
	pharmacologicalToxicology = scrapy.Field()
	#临床试验
	clinicalTrials = scrapy.Field()
	#警告
	warning = scrapy.Field()
	#修改时间
	modifyDate = scrapy.Field()

	fda = scrapy.Field()
	lactationDrug = scrapy.Field()
	medicineTakingFeeding = scrapy.Field()

	athleticDoping = scrapy.Field()
	insuranceType = scrapy.Field()
	otcType = scrapy.Field()
	#类型(1为西药,2为中成药)
	type = scrapy.Field()
	isBasic = scrapy.Field()

	#批准文号
	approvalCode = scrapy.Field()
	#包装
	packages = scrapy.Field()
	importCode = scrapy.Field()

#杏树林-方剂类
class XingshulinPrescriptionItem(scrapy.Item):
	id = scrapy.Field()
	#名称
	name = scrapy.Field()
	#别名
	aliasName = scrapy.Field()
	#使用注意
	cautions = scrapy.Field()
	#制方详解
	elucldation = scrapy.Field()
	#功效
	function = scrapy.Field()
	#主治
	indication = scrapy.Field()
	#组成
	ingredient = scrapy.Field()
	#辨证要点
	keySymptom = scrapy.Field()
	#现代运用
	modernApplication = scrapy.Field()
	#现代研究
	modernResearch = scrapy.Field()
	#临证加减
	modification = scrapy.Field()
	#原书记载
	originalRecord = scrapy.Field()
	#各家方论
	selectedRecord = scrapy.Field()
	#方源
	source = scrapy.Field()
	#用法
	usage = scrapy.Field()
	#歌诀
	verse = scrapy.Field()

#万方-检验类
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
		
class DxyDocumentItem(scrapy.Item):
	id = scrapy.Field()
	name = scrapy.Field()
	downloadUrl = scrapy.Field()
	uploadTime = scrapy.Field()
	description = scrapy.Field()
	sourceType = scrapy.Field()
	user = scrapy.Field()
	size = scrapy.Field()
	classification = scrapy.Field()
	byteContent = scrapy.Field()

class DxyDownloadPdfItem(scrapy.Item):
	file_urls = scrapy.Field()
	files = scrapy.Field()