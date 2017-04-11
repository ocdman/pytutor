# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymssql
import json
import threading

from tutorial.items import *
from tutorial.settings import *

class TutorialPipeline(object):

	def __init__(self):
		print "start pymssql connect"
		#数据库配置
		self.conn = pymssql.connect(server=CUST_SERVER, user=CUST_USER, password=CUST_PWD, database=CUST_DB)
		self.cursor = self.conn.cursor()
		#加入锁
		self.lock = threading.Lock()

	def process_item(self, item, spider):
		if isinstance(item, XingshulinTestItem):
			self.lock.acquire()
			self.cursor.execute("insert into laboratories(id, cname, ename, testname, testdescription, sampletype, normalvalue, normalvaluedescription, summary, testwhys, testwhen, testprinciple, resulteffectreason, diseaserelated, relationtest, relationquestion, suffererprepare, swatchgather) values ({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17})".format(item['id'], item['cname'], item['ename'], item['testName'], item['testDescription'], item['sampleType'], item['normalValue'], item['normalValueDescription'], item['summary'], item['testWhys'], item['testWhen'], item['testPrinciple'], item['resultEffectReason'], item['diseaseRelated'], item['relationTest'], item['relationQuestion'], item['suffererPrepare'], item['swatchGather']))
			self.conn.commit()
			self.lock.release()
		elif isinstance(item, XingshulinGuideItem):
			self.lock.acquire()
			self.cursor.execute("insert into guides(id, guideName, year, organization, summary, publishedDate, pdfLink, epubLink, journal, author, volume, issue) values ({0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11})".format(item['id'], item['guideName'], item['year'], item['organization'], item['summary'], item['publishedDate'], item['pdfLink'], item['epubLink'], item['journal'], item['author'], item['volume'], item['issue']))
			self.conn.commit()
			self.lock.release()
		elif isinstance(item, XingshulinChineseMedicineItem):
			self.lock.acquire()
			self.cursor.execute("insert into chinesemedicines(id, name, pinyin, alias, source, harvestPreparation, commercialSpecification, properties, channelsTropism, functions, indications, dosage, cautions, commentary, chemicalCompositions, pharmacologicalEffects, pharmacodynamics, clinicalReports, toxicity, [references]) values({0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11}, {12}, {13}, {14}, {15}, {16}, {17}, {18}, {19})".format(item['id'], item['name'], item['pinyin'], item['alias'], item['source'], item['harvestPreparation'], item['commercialSpecification'], item['properties'], item['channelsTropism'], item['functions'], item['indications'], item['dosage'], item['cautions'], item['commentary'], item['chemicalCompositions'], item['pharmacologicalEffects'], item['pharmacodynamics'], item['clinicalReports'], item['toxicity'], item['references']))
			self.conn.commit()
			self.lock.release()
		elif isinstance(item, XingshulinDrugItem):
			self.lock.acquire()
			self.cursor.execute("insert into drugs(id, commonName, englishCommonName, tradeName, englishTradeName, tradeMark, mainIngredient, [description], indication, specification, dosage, taboo, other, interaction, storage, manufacturer, executiveStandard, period, geriatricUse, pharmacokinetics, pregnantLactatingUse, sideEffect, approvalDate, pediatricUse, overdose, pharmacologicalToxicology, clinicalTrials, warning, modifyDate, fda, lactationDrug, medicineTakingFeeding, athleticDoping, insuranceType, otcType, [type], isBasic, approvalCode, packages, importCode) values({0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11}, {12}, {13}, {14}, {15}, {16}, {17}, {18}, {19}, {20},{21}, {22}, {23}, {24}, {25}, {26}, {27}, {28}, {29}, {30},{31}, {32}, {33}, {34}, {35}, {36}, {37}, {38}, {39})".format(item['id'], item['commonName'], item['englishCommonName'], item['tradeName'], item['englishTradeName'], item['tradeMark'], item['mainIngredient'], item['description'], item['indication'], item['specification'], item['dosage'], item['taboo'], item['other'], item['interaction'], item['storage'], item['manufacturer'], item['executiveStandard'], item['period'], item['geriatricUse'], item['pharmacokinetics'], item['pregnantLactatingUse'], item['sideEffect'], item['approvalDate'], item['pediatricUse'], item['overdose'], item['pharmacologicalToxicology'], item['clinicalTrials'], item['warning'], item['modifyDate'], item['fda'], item['lactationDrug'], item['medicineTakingFeeding'], item['athleticDoping'], item['insuranceType'], item['otcType'], item['type'], item['isBasic'], item['approvalCode'], item['packages'], item['importCode']))
			self.conn.commit()
			self.lock.release()
		elif isinstance(item, WanfangExaminationItem):
			self.lock.acquire()
			self.cursor.execute("insert into wanfangexaminations(id, recordtype, cname, ename, nameinfo, summarize, indication, reference, clinical, samples, precautions, category, initial, articlecount, categoryshort, categoryroot, author, checker) values ({0},{1},{2},{3},{4},{5},{6},{7},{8},{9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17})".format(item['ID'], item['RecordType'], item['CName'], item['EName'], item['NameInfo'], item['Summarize'], item['Indication'], item['Reference'], item['Clinical'], item['Samples'], item['Precautions'], item['Category'], item['Initial'], item['ArticleCount'], item['CategoryShort'], item['CategoryRoot'], item['Author'], item['Checker']))
			self.conn.commit()
			self.lock.release()
        # return item
