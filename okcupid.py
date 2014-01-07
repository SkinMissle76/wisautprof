#!/bin/python2.7
import shelve
import sys
import json
import re
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
for user in db_merge.items():
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
		if userdata.has_key('educationString'):
			print "Skipping %s, already visisted" % username
			continue

		time.sleep(1)
		url = profile_url % username
		fp = urllib2.urlopen(url)
		profileData = fp.read()
		fp.close()
		profileSoup = BeautifulSoup(profileData)
	except:
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
	

	storeData = json.dumps( userdata )
	db_merge[username] = storeData
	print "Stored %s, with education: %s" % (username, userdata['educationString'])
db_merge.close()
