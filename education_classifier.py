from models.tables import EDUCATION_TABLE_INVERTED
from models.tables import LOCATIONS_TABLE_INVERTED
from crawlers.LinkedinDOM import Linkedin
from decimal import *
import json

URLS = [
  "http://www.linkedin.com/in/mdilnot",
  "http://uk.linkedin.com/pub/simon-ridgwell/77/9b4/197"
]

with open('data/uk_universities_list.json', 'r') as f:
		data_uni = json.load(f)
with open('data/uk_secschools_list.json', 'r') as g:
		data_sch = json.load(g)
with open('data/Cities.json', 'r') as h:
		data_city = json.load(h)
		
lc = Linkedin()           # this guys is the linkedin crawler
profile = lc.getProfile(URLS[0])

		
#user comes as lc.getProfile(URL)
def _getUserEducation(profile):
	educations = []
	pr1 = profile["education"]
	for ed in pr1:
		educations.append(ed["school"])
	return educations

#user comes as lc.getProfile(URL). Returns True if the user is from UK, and False if not	
def _isUserFromUK(profile):
	pr1 = profile["locality"]
	list = pr1.split(",", 1)
	if list[1] == ' United Kingdom':
		return True
	else:
		return False

def _isUniversity(uni):
	words = uni.split()
	for word in words:
		if word == "University" or word == "university":
			return True
	for da in data_uni:
		if uni == da[u'name'] or uni == da[u'acronyms']:
			return True
	return False
	
#edu is list of educations. Returns True if user has university education and False if not
def _isUserFromUni(edu):
	for un in edu:
		if _isUniversity(un):
			return True
	return False

def _isSchool(sch):
	words = sch.split()
	for word in words:
		if word == "College" or word == "High" or word == "college" or word == "high":
			return True
	for da in data_sch:
		if sch == da[u'name']:
			return True
	return False
	
#edu is list of educations. Returns True if user has university education and False if not
def _isUserFromSch(edu):
	for un in edu:
		if _isSchool(un):
			return True
	return False

## User comes as profile
def getEducation(profile):	
	if not _isUserFromUK(profile):
		return NONE
	edu = _getUserEducation(profile)
	if _isUserFromUni(edu):
		return EDUCATION_TABLE_INVERTED["High"]
	elif _isUserFromSch(edu):
		return EDUCATION_TABLE_INVERTED["Mid"]
	else:
		return EDUCATION_TABLE_INVERTED["Low"]

def getLocation(profile):
	if not _isUserFromUK(profile):
		return NONE
	else:
		pr1 = profile["locality"]
		list = pr1.split(",", 1)
		return LOCATIONS_TABLE_INVERTED[data_city[list[0]]]

#returns the age of the user
def getAge(profile):
	
	edu = profile["education"]
	edu1 = _getUserEducation(profile)
	if _isUserFromSch(edu1):
		age = 1000
		for un in edu:
			if _isSchool(un["school"]):
				buff = 2013 - Decimal(un["period"]["end"].split("-", 1)[0]) + 18
				if buff < age:
					age=buff
		return age
	if _isUserFromUni(edu1):
		age = 0
		for un in edu:
			if _isUniversity(un["school"]):
				buff = 2013 - Decimal(un["period"]["start"].split("-", 1)[0]) + 19
				if buff > age:
					age=buff
		return age
