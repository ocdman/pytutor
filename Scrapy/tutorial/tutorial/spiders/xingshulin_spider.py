# -*- coding: utf-8 -*-
import scrapy
import json
import time
import traceback
import logging

from tutorial.items import *
from tutorial.settings import COOKIES
from scrapy.http import FormRequest
from scrapy.utils.log import configure_logging

#将标准输出流同步到日志文件里
configure_logging(install_root_handler=False)
logging.basicConfig(
	filename='logging.txt',
	filemode = 'wb',
	format='%(asctime)s [%(name)s] %(levelname)s: %(message)s',
	level=logging.WARNING	#level not work
)

class XingshulinSpider(scrapy.Spider):
	name = "xingshulin"
	allowed_domains = ["xingshulin.com"]
	# start_urls = [
	# 	"http://www.xingshulin.com/searchTest.html"
	# ]

	def __init__(self):
		self.cookies = COOKIES

	def start_requests(self):
		#检查 & 检验
		# for i in range(4800, 0, -1):
		# 	yield FormRequest("http://epocket.xingshulin.com/test/getTestDetail/{0}".format(i),
		# 		cookies=self.cookies,
		# 		callback=self.parseTest)

		#指南
		# for i in range(21000, 0, -1):
		# 	yield FormRequest("https://epocket.xingshulin.com/guide/getGuideDetail/{0}".format(i),
		# 		cookies=self.cookies,
		# 		callback=self.parseGuide)

		#中药
		# for i in range(1200, 0, -1):
		# 	yield FormRequest("http://epocket.xingshulin.com/chineseMedicine/getChineseMedicineDetail/{0}/4".format(i),
		# 		cookies=self.cookies,
		# 		callback=self.parseChineseMedicine)

		#西药 & 中成药
		# for i in range(190000, 0, -1):
		# 	yield FormRequest("http://epocket.xingshulin.com/drug/getDrugDetail/{0}/1".format(i),
		# 		cookies=self.cookies,
		# 		callback=self.parseDrug)

		#方剂
		for i in range(1000, 0, -1):
			yield FormRequest("http://epocket.xingshulin.com/prescription/getPrescriptionDetail/{0}/3".format(i),
				cookies=self.cookies,
				callback=self.parsePrescription)


	'''
	解析检查 & 检验
	'''
	def parseTest(self, response):
		if response.status == 200:
			details = json.loads(response.body)
			testItem = XingshulinTestItem()
			try:
				if details['obj'].has_key('testVo') == True:
					items = details['obj']['testVo']
					if 'id' in items:
						testItem['id'] = items['id']
						testItem['cname'] = "'" + items['cname'].encode('utf-8').replace("'","''") + "'" if 'cname' in items else 'NULL'
						testItem['ename'] = "'" + items['ename'].encode('utf-8').replace("'","''") + "'" if 'ename' in items else 'NULL'
						testItem['testName'] = "'" + items['testName'].encode('utf-8').replace("'","''") + "'"  if 'testName' in items else 'NULL'
						testItem['testDescription'] =  "'" + items['testDescription'].encode('utf-8').replace("'","''") + "'"  if 'testDescription' in items else 'NULL'
						testItem['sampleType'] = "'" + items['sampleType'].encode('utf-8').replace("'","''") + "'" if 'sampleType' in items else 'NULL'
						testItem['normalValue'] = "'" + items['normalValue'].encode('utf-8').replace("'","''") + "'" if 'normalValue' in items else 'NULL'
						testItem['normalValueDescription'] = "'" + items['normalValueDescription'].encode('utf-8').replace("'","''") + "'" if 'normalValueDescription' in items else 'NULL'
						testItem['summary'] = "'" + items['summary'].encode('utf-8').replace("'","''") + "'" if 'summary' in items else 'NULL'
						testItem['testWhys'] = "'" + items['testWhys'].encode('utf-8').replace("'","''") + "'" if 'testWhys' in items else 'NULL'
						testItem['testWhen'] = "'" + items['testWhen'].encode('utf-8').replace("'","''") + "'" if 'testWhen' in items else 'NULL'
						testItem['testPrinciple'] = "'" + items['testPrinciple'].encode('utf-8').replace("'","''") + "'" if 'testPrinciple' in items else 'NULL'
						testItem['resultEffectReason'] = "'" + items['resultEffectReason'].encode('utf-8').replace("'","''") + "'" if 'resultEffectReason' in items else 'NULL'
						testItem['diseaseRelated'] = "'" + items['diseaseRelated'].encode('utf-8').replace("'","''") + "'" if 'diseaseRelated' in items else 'NULL'
						testItem['relationTest'] = "'" + items['relationTest'].encode('utf-8').replace("'","''") + "'" if 'relationTest' in items else 'NULL'
						testItem['relationQuestion'] = "'" + items['relationQuestion'].encode('utf-8').replace("'","''") + "'" if 'relationQuestion' in items else 'NULL'
						testItem['suffererPrepare'] = "'" + items['suffererPrepare'].encode('utf-8').replace("'","''") + "'" if 'suffererPrepare' in items else 'NULL'
						testItem['swatchGather'] = "'" + items['swatchGather'].encode('utf-8').replace("'","''") + "'" if 'swatchGather' in items else 'NULL'
						# for key in items:
						# 	if key not in testItem:
						# 		logging.warning('遗漏字段: ' + str(key) + ', Id:' + str(items['id']) + '\n')
						return testItem
			except Exception, ex:
				logging.error('异常捕获: ' + str(ex) + '\n')
		elif response.status == 404:
			logging.warning('未爬取的url: ' + str(response.url) + '\n')

	'''
	解析指南
	'''
	def parseGuide(self, response):
		if response.status == 200:
			details = json.loads(response.body)
			guideItem = XingshulinGuideItem()
			try:
				if details['obj'].has_key('guideVo') == True:
					items = details['obj']['guideVo']
					if 'id' in items:
						guideItem['id'] = items['id']
						guideItem['guideName'] = "'" + items['guideName'].encode('utf-8').replace("'","''") + "'" if 'guideName' in items else 'NULL'
						guideItem['year'] = "'" + items['year'].encode('utf-8').replace("'","''") + "'" if 'year' in items else 'NULL'
						guideItem['organization'] = "'" + items['organization'].encode('utf-8').replace("'","''") + "'" if 'organization' in items else 'NULL'
						guideItem['summary'] = "'" + items['summary'].encode('utf-8').replace("'","''") + "'" if 'summary' in items else 'NULL'
						guideItem['publishedDate'] = "'" + items['publishedDate'].encode('utf-8').replace("'","''") + "'" if 'publishedDate' in items else 'NULL'
						guideItem['pdfLink'] = "'" + items['pdfLink'].encode('utf-8').replace("'","''") + "'" if 'pdfLink' in items else 'NULL'
						guideItem['epubLink'] = "'" + items['epubLink'].encode('utf-8').replace("'","''") + "'" if 'epubLink' in items else 'NULL'
						guideItem['journal'] = "'" + items['journal'].encode('utf-8').replace("'","''") + "'" if 'journal' in items else 'NULL'
						guideItem['author'] = "'" + items['author'].encode('utf-8').replace("'","''") + "'" if 'author' in items else 'NULL'
						guideItem['volume'] = "'" + items['volume'].encode('utf-8').replace("'","''") + "'" if 'volume' in items else 'NULL'
						guideItem['issue'] = "'" + items['issue'].encode('utf-8').replace("'","''") + "'" if 'issue' in items else 'NULL'
						guideItem['downloadCount'] = 0
						# for key in items:
						# 	if key not in guideItem:
						# 		logging.warning('遗漏字段: ' + str(key) + ', Id:' + str(items['id']) + '\n')
						return guideItem
			except Exception, ex:
				logging.error('异常捕获: ' + str(ex) + '\n')
		elif response.status == 404:
			logging.warning('未爬取的url: ' + str(response.url) + '\n')

	'''
	解析中药
	'''
	def parseChineseMedicine(self, response):
		if response.status == 200:
			details = json.loads(response.body)
			chineseMedicineItem = XingshulinChineseMedicineItem()
			try:
				if details['obj'].has_key('chineseMedicineVo') == True:
					items = details['obj']['chineseMedicineVo']
					if 'id' in items:
						chineseMedicineItem['id'] = items['id']
						chineseMedicineItem['name'] = "'" + items['name'].encode('utf-8').replace("'","''") + "'" if 'name' in items else 'NULL'
						chineseMedicineItem['pinyin'] = "'" + items['pinyin'].encode('utf-8').replace("'","''") + "'" if 'pinyin' in items else 'NULL'
						chineseMedicineItem['alias'] = "'" + items['alias'].encode('utf-8').replace("'","''") + "'" if 'alias' in items else 'NULL'
						chineseMedicineItem['source'] = "'" + items['source'].encode('utf-8').replace("'","''") + "'" if 'source' in items else 'NULL'
						chineseMedicineItem['harvestPreparation'] = "'" + items['harvestPreparation'].encode('utf-8').replace("'","''") + "'" if 'harvestPreparation' in items else 'NULL'
						chineseMedicineItem['commercialSpecification'] = "'" + items['commercialSpecification'].encode('utf-8').replace("'","''") + "'" if 'commercialSpecification' in items else 'NULL'
						chineseMedicineItem['properties'] = "'" + items['properties'].encode('utf-8').replace("'","''") + "'" if 'properties' in items else 'NULL'
						chineseMedicineItem['channelsTropism'] = "'" + items['channelsTropism'].encode('utf-8').replace("'","''") + "'" if 'channelsTropism' in items else 'NULL'
						chineseMedicineItem['functions'] = "'" + items['functions'].encode('utf-8').replace("'","''") + "'" if 'functions' in items else 'NULL'
						chineseMedicineItem['indications'] = "'" + items['indications'].encode('utf-8').replace("'","''") + "'" if 'indications' in items else 'NULL'
						chineseMedicineItem['dosage'] = "'" + items['dosage'].encode('utf-8').replace("'","''") + "'" if 'dosage' in items else 'NULL'
						chineseMedicineItem['cautions'] = "'" + items['cautions'].encode('utf-8').replace("'","''") + "'" if 'cautions' in items else 'NULL'
						chineseMedicineItem['commentary'] = "'" + items['commentary'].encode('utf-8').replace("'","''") + "'" if 'commentary' in items else 'NULL'
						chineseMedicineItem['chemicalCompositions'] = "'" + items['chemicalCompositions'].encode('utf-8').replace("'","''") + "'" if 'chemicalCompositions' in items else 'NULL'
						chineseMedicineItem['pharmacologicalEffects'] = "'" + items['pharmacologicalEffects'].encode('utf-8').replace("'","''") + "'" if 'pharmacologicalEffects' in items else 'NULL'
						chineseMedicineItem['pharmacodynamics'] = "'" + items['pharmacodynamics'].encode('utf-8').replace("'","''") + "'" if 'pharmacodynamics' in items else 'NULL'
						chineseMedicineItem['clinicalReports'] = "'" + items['clinicalReports'].encode('utf-8').replace("'","''") + "'" if 'clinicalReports' in items else 'NULL'
						chineseMedicineItem['toxicity'] = "'" + items['toxicity'].encode('utf-8').replace("'","''") + "'" if 'toxicity' in items else 'NULL'
						chineseMedicineItem['references'] = "'" + items['references'].encode('utf-8').replace("'","''") + "'" if 'references' in items else 'NULL'
						# for key in items:
						# 	if key not in chineseMedicineItem:
						# 		logging.warning('遗漏字段: ' + str(key) + ', Id:' + str(items['id']) + '\n')
						return chineseMedicineItem
			except Exception, ex:
				logging.error('异常捕获: ' + str(ex) + '\n')
		elif response.status:
			logging.warning('未爬取的url: ' + str(response.url) + '\n')

	'''
	解析西药&中成药
	'''
	def parseDrug(self, response):
		if response.status == 200:
			logging.info(response.body)
			details = json.loads(response.body)
			drugItem = XingshulinDrugItem()
			try:
				if details['obj'].has_key('drugVo') == True:
					items = details['obj']['drugVo']
					if 'id' in items:
						drugItem['id'] = items['id']
						drugItem['commonName'] = "'" + items['commonName'].encode('utf-8').replace("'","''") + "'" if 'commonName' in items else 'NULL'
						drugItem['englishCommonName'] = "'" + items['englishCommonName'].encode('utf-8').replace("'","''") + "'" if 'englishCommonName' in items else 'NULL'
						drugItem['tradeName'] = "'" + items['tradeName'].encode('utf-8').replace("'","''") + "'" if 'tradeName' in items else 'NULL'
						drugItem['englishTradeName'] = "'" + items['englishTradeName'].encode('utf-8').replace("'","''") + "'" if 'englishTradeName' in items else 'NULL'
						drugItem['aliasName'] = "'" + items['aliasName'].encode('utf-8').replace("'","''") + "'" if 'aliasName' in items else 'NULL'
						drugItem['tradeMark'] = "'" + items['tradeMark'].encode('utf-8').replace("'","''") + "'" if 'tradeMark' in items else 'NULL'
						drugItem['mainIngredient'] = "'" + items['mainIngredient'].encode('utf-8').replace("'","''") + "'" if 'mainIngredient' in items else 'NULL'
						drugItem['description'] = "'" + items['description'].encode('utf-8').replace("'","''") + "'" if 'description' in items else 'NULL'
						drugItem['indication'] = "'" + items['indication'].encode('utf-8').replace("'","''") + "'" if 'indication' in items else 'NULL'
						drugItem['specification'] = "'" + items['specification'].encode('utf-8').replace("'","''") + "'" if 'specification' in items else 'NULL'
						drugItem['dosage'] = "'" + items['dosage'].encode('utf-8').replace("'","''") + "'" if 'dosage' in items else 'NULL'
						drugItem['taboo'] = "'" + items['taboo'].encode('utf-8').replace("'","''") + "'" if 'taboo' in items else 'NULL'
						drugItem['other'] = "'" + items['other'].encode('utf-8').replace("'","''") + "'" if 'other' in items else 'NULL'
						drugItem['interaction'] = "'" + items['interaction'].encode('utf-8').replace("'","''") + "'" if 'interaction' in items else 'NULL'
						drugItem['storage'] = "'" + items['storage'].encode('utf-8').replace("'","''") + "'" if 'storage' in items else 'NULL'
						drugItem['manufacturer'] = "'" + items['manufacturer'].encode('utf-8').replace("'","''") + "'" if 'manufacturer' in items else 'NULL'
						drugItem['executiveStandard'] = "'" + items['executiveStandard'].encode('utf-8').replace("'","''") + "'" if 'executiveStandard' in items else 'NULL'
						drugItem['period'] = "'" + items['period'].encode('utf-8').replace("'","''") + "'" if 'period' in items else 'NULL'
						drugItem['geriatricUse'] = "'" + items['geriatricUse'].encode('utf-8').replace("'","''") + "'" if 'geriatricUse' in items else 'NULL'
						drugItem['pharmacokinetics'] = "'" + items['pharmacokinetics'].encode('utf-8').replace("'","''") + "'" if 'pharmacokinetics' in items else 'NULL'
						drugItem['pregnantLactatingUse'] = "'" + items['pregnantLactatingUse'].encode('utf-8').replace("'","''") + "'" if 'pregnantLactatingUse' in items else 'NULL'
						drugItem['sideEffect'] = "'" + items['sideEffect'].encode('utf-8').replace("'","''") + "'" if 'sideEffect' in items else 'NULL'
						drugItem['approvalDate'] = "'" + items['approvalDate'].encode('utf-8').replace("'","''") + "'" if 'approvalDate' in items else 'NULL'
						drugItem['pediatricUse'] = "'" + items['pediatricUse'].encode('utf-8').replace("'","''") + "'" if 'pediatricUse' in items else 'NULL'
						drugItem['overdose'] = "'" + items['overdose'].encode('utf-8').replace("'","''") + "'" if 'overdose' in items else 'NULL'
						drugItem['pharmacologicalToxicology'] = "'" + items['pharmacologicalToxicology'].encode('utf-8').replace("'","''") + "'" if 'pharmacologicalToxicology' in items else 'NULL'
						drugItem['clinicalTrials'] = "'" + items['clinicalTrials'].encode('utf-8').replace("'","''") + "'" if 'clinicalTrials' in items else 'NULL'
						drugItem['warning'] = "'" + items['warning'].encode('utf-8').replace("'","''") + "'" if 'warning' in items else 'NULL'
						drugItem['modifyDate'] = "'" + items['modifyDate'].encode('utf-8').replace("'","''") + "'" if 'modifyDate' in items else 'NULL'
						drugItem['fda'] = "'" + items['fda'].encode('utf-8').replace("'","''") + "'" if 'fda' in items else 'NULL'
						drugItem['lactationDrug'] = "'" + items['lactationDrug'].encode('utf-8').replace("'","''") + "'" if 'lactationDrug' in items else 'NULL'
						drugItem['medicineTakingFeeding'] = "'" + items['medicineTakingFeeding'].encode('utf-8').replace("'","''") + "'" if 'medicineTakingFeeding' in items else 'NULL'

						drugItem['athleticDoping'] = items['athleticDoping'] if 'athleticDoping' in items else 'NULL'
						drugItem['insuranceType'] = items['insuranceType'] if 'insuranceType' in items else 'NULL'
						drugItem['otcType'] = items['otcType'] if 'otcType' in items else 'NULL'
						drugItem['type'] = items['type'] if 'type' in items else 'NULL'
						drugItem['isBasic'] = items['isBasic'] if 'isBasic' in items else 'NULL'

						#这几个Item值来自于drugSpecificationVoList列表的第一个字典
						drugItem['approvalCode'] = 'NULL'
						drugItem['packages'] = 'NULL'
						drugItem['importCode'] = 'NULL'

						for key in items:
							if key not in drugItem:
								logging.warning('遗漏字段: ' + str(key) + ', Id:' + str(items['id']) + '\n')
						
						#如果drugSpecificationVoList列表有值，则覆写以下几个Item
						if details['obj'].has_key('drugSpecificationVoList') == True:
							listItems = details['obj']['drugSpecificationVoList']
							if isinstance(listItems, list) == True:
								if len(listItems) > 0:
									items = listItems[0]
									if 'drugId' in items:
										drugItem['approvalCode'] = "'" + items['approvalCode'].encode('utf-8').replace("'","''") + "'" if 'approvalCode' in items else 'NULL'
										drugItem['packages'] = "'" + items['packages'].encode('utf-8').replace("'","''") + "'" if 'packages' in items else 'NULL'
										drugItem['importCode'] = "'" + items['importCode'].encode('utf-8').replace("'","''") + "'" if 'importCode' in items else 'NULL'
										if drugItem['specification'] == 'NULL':
											drugItem['specification'] = "'" + items['specification'].encode('utf-8').replace("'","''") + "'" if 'specification' in items else 'NULL'
						
						return drugItem
			except Exception, ex:
				logging.error('异常捕获: ' + str(ex) + '\n')
		elif response.status:
			logging.warning('未爬取的url: ' + str(response.url) + '\n')
	
	'''
	解析方剂
	'''
	def parsePrescription(self, response):
		if response.status == 200:
			logging.info(response.body)
			details = json.loads(response.body)
			prescriptionItem = XingshulinPrescriptionItem()
			try:
				if details['obj'].has_key('prescriptionVo') == True:
					items = details['obj']['prescriptionVo']
					if 'id' in items:
						prescriptionItem['id'] = items['id']
						prescriptionItem['name'] = "'" + items['name'].encode('utf-8').replace("'","''") + "'" if 'name' in items else 'NULL'
						prescriptionItem['aliasName'] = "'" + items['aliasName'].encode('utf-8').replace("'","''") + "'" if 'aliasName' in items else 'NULL'
						prescriptionItem['cautions'] = "'" + items['cautions'].encode('utf-8').replace("'","''") + "'" if 'cautions' in items else 'NULL'
						prescriptionItem['elucldation'] = "'" + items['elucldation'].encode('utf-8').replace("'","''") + "'" if 'elucldation' in items else 'NULL'
						prescriptionItem['function'] = "'" + items['function'].encode('utf-8').replace("'","''") + "'" if 'function' in items else 'NULL'
						prescriptionItem['indication'] = "'" + items['indication'].encode('utf-8').replace("'","''") + "'" if 'indication' in items else 'NULL'
						prescriptionItem['ingredient'] = "'" + items['ingredient'].encode('utf-8').replace("'","''") + "'" if 'ingredient' in items else 'NULL'
						prescriptionItem['keySymptom'] = "'" + items['keySymptom'].encode('utf-8').replace("'","''") + "'" if 'keySymptom' in items else 'NULL'
						prescriptionItem['modernApplication'] = "'" + items['modernApplication'].encode('utf-8').replace("'","''") + "'" if 'modernApplication' in items else 'NULL'
						prescriptionItem['modernResearch'] = "'" + items['modernResearch'].encode('utf-8').replace("'","''") + "'" if 'modernResearch' in items else 'NULL'
						prescriptionItem['modification'] = "'" + items['modification'].encode('utf-8').replace("'","''") + "'" if 'modification' in items else 'NULL'
						prescriptionItem['originalRecord'] = "'" + items['originalRecord'].encode('utf-8').replace("'","''") + "'" if 'originalRecord' in items else 'NULL'
						prescriptionItem['selectedRecord'] = "'" + items['selectedRecord'].encode('utf-8').replace("'","''") + "'" if 'selectedRecord' in items else 'NULL'
						prescriptionItem['source'] = "'" + items['source'].encode('utf-8').replace("'","''") + "'" if 'source' in items else 'NULL'
						prescriptionItem['usage'] = "'" + items['usage'].encode('utf-8').replace("'","''") + "'" if 'usage' in items else 'NULL'
						prescriptionItem['verse'] = "'" + items['verse'].encode('utf-8').replace("'","''") + "'" if 'verse' in items else 'NULL'
						for key in items:
							if key not in prescriptionItem and key != 'prescriptionId':
								logging.warning('遗漏字段: ' + str(key) + ', Id:' + str(items['id']) + '\n')
						return prescriptionItem
			except Exception, ex:
				logging.error('异常捕获: ' + str(ex) + '\n')
		elif response.status:
			logging.warning('未爬取的url: ' + str(response.url) + '\n')