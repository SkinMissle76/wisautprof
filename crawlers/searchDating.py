#!/bin/python2.7
from bs4 import BeautifulSoup
import urllib2
import sys
import re
import json
import time
import random
import collections

cities = ["Birmingham", "Bradford", "Brighton & Hove", "Bristol", "Cambridge", "Canterbury", "Carlisle", "Chelmsford", "Chester", "Chichester", "Coventry", "Derby", "Durham", "Ely", "Exeter", "Gloucester", "Hereford", "Kingston upon Hull", "Lancaster", "Leeds", "Leicester", "Lichfield", "Lincoln", "Liverpool", "City of London", "Manchester", "Newcastle upon Tyne", "Norwich", "Nottingham", "Oxford", "Peterborough", "Plymouth", "Portsmouth", "Preston", "Ripon", "Salford", "Salisbury", "Sheffield", "Southampton", "St Albans", "Stoke-on-Trent", "Sunderland", "Truro", "Wakefield", "Wells", "City of Westminster", "Winchester", "Wolverhampton", "Worcester", "York", "Aberdeen", "Dundee", "Edinburgh", "Glasgow", "Inverness", "Perth", "Stirling", "Bangor", "Cardiff", "Newport", "St Asaph", "St David's", "Swansea", "Armagh", "Belfast", "Derry", "Lisburn", "Newry"]
citiesCount = {"Bath" : "Somerset", "Birmingham" : "West Midlands", "Bradford" : "West Yorkshire", "Brighton & Hove" : "East Sussex", "Bristol" : "Gloucestershire", "Cambridge" : "Cambridgeshire", "Canterbury" : "Kent", "Carlisle" : "Cumbria", "Chelmsford" : "Essex", "Chester" : "Cheshire", "Chichester" : "West Sussex", "Coventry" : "West Midlands", "Derby" : "Derbyshire", "Durham" : "Durham", "Ely" : "Cambridgeshire", "Exeter" : "Devon", "Gloucester" : "Gloucestershire", "Hereford" : "Herefordshire", "Kingston upon Hull" : "East Riding of Yorkshire", "Lancaster" : "Lancashire", "Leeds" : "West Yorkshire", "Leicester" : "Leicestershire", "Lichfield" : "Staffordshire", "Lincoln" : "Lincolnshire", "Liverpool" : "Merseyside", "City of London" : "Greater London", "Manchester" : "Greater Manchester", "Newcastle upon Tyne" : "Tyne and Wear", "Norwich" : "Norfolk", "Nottingham" : "Nottinghamshire", "Oxford" : "Oxfordshire", "Peterborough" : "Cambridgeshire", "Plymouth" : "Devon", "Portsmouth" : "Hampshire", "Preston" : "Lancashire", "Ripon" : "North Yorkshire", "Salford" : "Greater Manchester", "Salisbury" : "Wiltshire", "Sheffield" : "South Yorkshire", "Southampton" : "Hampshire", "St Albans" : "Hertfordshire", "Stoke-on-Trent" : "Staffordshire", "Sunderland" : "Tyne and Wear", "Truro" : "Cornwall", "Wakefield" : "West Yorkshire", "Wells" : "Somerset", "City of Westminster" : "Greater London", "Winchester" : "Hampshire", "Wolverhampton" : "West Midlands", "Worcester" : "West Midlands", "York" : "North Yorkshire"}


#Uses google to retrieve profiles from OkCupid.com

# Step 1: Retrieve city lists from Wikipedia for areas in England
##fp = urllib2.urlopen("http://en.wikipedia.org/wiki/List_of_towns_in_England")
##wiki_data = fp.read()
##fp.close()
##
##wiki_soup = BeautifulSoup(wiki_data)
##wiki_dict = {}
##for table in wiki_soup.find_all("table", attrs={"class": "wikitable"}):
##	for tr in table.find_all("tr"):
##		wiki_dict[tr.contents[1].string] = tr.contents[3].string
##
##sorted_dict = collections.OrderedDict(sorted(wiki_dict.items()))

# site%3Aokcupid.com+%22f+%2F+Aldershot, United Kingdom%22
# Step 2: Query google using the wikipedia dict

output = open("dump.txt", "a+")

#url = "https://www.google.nl/?ei=nf6hUrX3MejL0QWQmoHwDQ#q=site:okcupid.com+\"f+/+%s, United Kingdom\"&start=%d"
#url = "http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=site%%3Aokcupid.com+%%22f+%%2F+%s, United Kingdom%%22"
url = "https://www.googleapis.com/customsearch/v1?key=%s&cx=%s&q=site%%3Aokcupid.com+%%22F+%%2F+%s%%2C+United+Kingdom%%22&start=%s"

###################################################################
#
#
key = "AIzaSyDBh3kkK6qtpRELDJ4t-IMM_qEHQ8sdBf0"
offset = 693
search_engine_id = "016584094713900655717:rb8kgl4eucs"
#
#
###################################################################

for city in cities:
	start = 1
	errorCount = 0
	if city == "Birmingham":
		start = 101
	next = True
	while next:
		try:
			time.sleep(5)

			google_url = url % (key, search_engine_id, city, start)
			google_url = re.sub(" ", "%20", google_url)

			print city
			print google_url
			print "Fetching %s on offset: %s" % (city, start)
			fp = urllib2.urlopen(google_url)
			google_data = fp.read()
			fp.close()
			google_json = json.loads(google_data)
			if 'items' not in google_json:
				next = False
				continue
			google_results = google_json['items']

			if 'nextPage' not in google_json['queries']:
				next = False
			start += 10

			for profile in google_results:
				print profile['link']
				print profile['title']
				output.write("%s | %s | %s\n" % (profile['link'], profile['title'], city))
				print "============================="
		except:
			time.sleep(30)
			errorCount += 1
			if errorCount > 3:
				next = False
			continue
