#!/bin/python2.7
import shelve
import sys
import json
import re
import urllib
import urllib2
import time
from bs4 import BeautifulSoup
db_merge = shelve.open("data/female_merge.shelve")

def checkData(profileAttribute):
	if profileAttribute != None:
		profileAttribute = profileAttribute.string
		if profileAttribute == None:
			return None
		if len(profileAttribute.strip()) == 1:
			profileAttribute = None
		return profileAttribute
	return None

re_username_find = re.compile(" OkCupid \| (.*?) / ([0-9]+) .*? \| (.*)$")
profile_url = "http://www.okcupid.com/profile/%s"
topic_url = "http://textalytics.com/core/topics-1.1"
for user in db_merge.items():
	time.sleep(2)
	username = user[0]
	userdata = user[1]
	try:
		userdata = json.loads(userdata)
	except:
		continue

	try:
		if len(userdata['tweets']) == 0:
			print "Skipping %s, no tweets" % username
			continue
		if userdata.has_key('topicList'):
			print "Skipping %s, already processed description" % username
			continue
		if userdata.has_key('educationString') and userdata.has_key('Description'):
			print len(userdata['Description'])
			if len(userdata['Description']) > 0:
				print "Starting topic mining for %s" % username
				postData = {
					'txt': userdata['Description'],
					'txtf': 'plain',
					'key': '3cdabc92eb210b7b56cfe31d4c5ca249',
					'lang': 'en',
					'src': 'unknown',
					'of': 'json',
					'tt': 'ec',
				}
				time.sleep(1)
				fp = urllib2.urlopen(topic_url, urllib.urlencode(postData))
				topicData = fp.read()
				fp.close()
				topicData = json.loads(topicData)
				topicList = []
				for entity in topicData['entity_list']:
					topicList.append( entity['form'] )
				for concept in topicData['concept_list']:
					topicList.append( concept['form'] )
				userdata['topicList'] = topicList
				db_merge[username] = userdata
				print "stored %s topics for %s" % (len(topicList), username)
				continue
			else:
				print "No description found for %s" % username
				continue

		time.sleep(1)
		url = profile_url % username
		fp = urllib2.urlopen(url)
		profileData = fp.read()
		fp.close()
		profileSoup = BeautifulSoup(profileData)
	except Exception, e:
		print e
		continue

	profileEducationTag = profileSoup.find("dd", attrs={'id': 'ajax_education'})
	profileEthnicitiesTag = profileSoup.find("dd", attrs={'id': 'ajax_ethnicities'})
	profileHeightTag = profileSoup.find("dd", attrs={'id': 'ajax_height'})
	profileBodyTypeTag = profileSoup.find("dd", attrs={'id': 'ajax_bodytype'})
	profileDietTag = profileSoup.find("dd", attrs={'id': 'ajax_diet'})
	profileSmokingTag = profileSoup.find("dd", attrs={'id': 'ajax_smoking'})
	profileDrinkingTag = profileSoup.find("dd", attrs={'id': 'ajax_drinking'})
	profileDrugsTag = profileSoup.find("dd", attrs={'id': 'ajax_drugs'})
	profileReligionTag = profileSoup.find("dd", attrs={'id': 'ajax_religion'})
	profileJobTag = profileSoup.find("dd", attrs={'id': 'ajax_job'})
	profileIncomeTag = profileSoup.find("dd", attrs={'id': 'ajax_income'})
	profileChildrenTag = profileSoup.find("dd", attrs={'id': 'ajax_children'})
	profilePetsTag = profileSoup.find("dd", attrs={'id': 'ajax_pets'})
	profileLanguagesTag = profileSoup.find("dd", attrs={'id': 'ajax_languages'})
	summary0 = profileSoup.find("div", attrs={'id': 'essay_text_0'})
	summary1 = profileSoup.find("div", attrs={'id': 'essay_text_1'})
	summary2 = profileSoup.find("div", attrs={'id': 'essay_text_2'})
	summary3 = profileSoup.find("div", attrs={'id': 'essay_text_3'})
	summary4 = profileSoup.find("div", attrs={'id': 'essay_text_4'})
	summary5 = profileSoup.find("div", attrs={'id': 'essay_text_5'})
	summary6 = profileSoup.find("div", attrs={'id': 'essay_text_6'})
	summary7 = profileSoup.find("div", attrs={'id': 'essay_text_7'})
	
	userdata['educationString'] = checkData(profileEducationTag)
	userdata['Ethnicities'] = checkData(profileEthnicitiesTag) 
	userdata['Height'] = checkData(profileHeightTag)
	userdata['BodyType'] = checkData(profileBodyTypeTag)
	userdata['Diet'] = checkData(profileDietTag)
	userdata['Smoking'] = checkData(profileSmokingTag)
	userdata['Drinking'] = checkData(profileDrinkingTag)
	userdata['Drugs'] = checkData(profileDrugsTag)
	userdata['Religion'] = checkData(profileReligionTag)
	userdata['Job'] = checkData(profileJobTag)
	userdata['Income'] = checkData(profileIncomeTag)
	userdata['Children'] = checkData(profileChildrenTag)
	userdata['Pets'] = checkData(profilePetsTag)
	userdata['Languages'] = checkData(profileLanguagesTag)
	profile_description = ""
	
	if checkData(summary0):
		profile_description += checkData(summary0)
	if checkData(summary1):
		profile_description += checkData(summary1)
	if checkData(summary2):
		profile_description += checkData(summary2)
	if checkData(summary3):
		profile_description += checkData(summary3)
	if checkData(summary4):
		profile_description += checkData(summary4)
	if checkData(summary5):
		profile_description += checkData(summary5)
	if checkData(summary6):
		profile_description += checkData(summary6)
	if checkData(summary7):
		profile_description += checkData(summary7)
	
	userdata['Description'] = profile_description
	storeData = json.dumps( userdata )
	db_merge[username] = storeData
	print "Stored %s" % (username)
db_merge.close()
