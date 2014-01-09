#!/bin/python2.7
import shelve
import sys
import json
import re
import urllib
import urllib2
import time
import string
import os

from bs4 import BeautifulSoup
db_twitter_female = shelve.open("data/Twitter_results_db_dump_FEMALE.shelve")
db_twitter_male = shelve.open("data/Twitter_results_db_dump_MALE.shelve")

fp = open("data/manually_tagged/users_okcupid_verified.json")
tweetData = fp.read()
fp.close()
profileData = json.loads(tweetData)


def AGE_REAL_TO_SYS(realAge):
  if (realAge > 100 or realAge < 0):
    raise NameError("yo watch out dude, realAge must be between 0 and 100, yours is %s" % realAge)
  return ((realAge-50)/50)
def _processPunctuation(text):
	t = re.sub("https?:\/\/.*(\s+|$)", '', text)
	t = t.replace("\n", "").replace("'", "")

	for p in string.punctuation:
		t = t.replace(p, " "+p+" ")

	return t


counter_profiles = 0
for profile in profileData:
	username = str(profile['okcupidUsername'])
	twitterData = None

	if db_twitter_female.has_key(username):
		# Use female database
		print "Female user found"
		twitterData = db_twitter_female[username]
	else:
		if db_twitter_male.has_key(username):
			# Use male database
			print "Male user found"
			twitterData = db_twitter_male[username]
		
		else:
			print "Username did not appear is twitter database %s" % username
			continue

	twitterData = json.loads(twitterData['str'])
	directory = "data/manually_tagged/generatedProfiles/%s/" % twitterData['userid']
	if not os.path.exists(directory):
    		os.makedirs(directory)
	else:
		print "User already has generated data, skipping"
		continue
	
	fp_age = open("%slibshorttext_age.txt" % directory, "a")
	fp_education = open("%slibshorttext_education.txt" % directory, "a")
	fp_gender = open("%slibshorttext_gender.txt" % directory, "a")
	fp_location = open("%slibshorttext_location.txt" % directory, "a")

	for tweet in twitterData['tweets']:
		age = AGE_REAL_TO_SYS(float(profile['age']))
		age_outLine = "%s\t%s\n" % (age, _processPunctuation(tweet).encode('utf-8'))
		education_outLine = "%s\t%s\n" % (int(profile['education']), _processPunctuation(tweet).encode('utf-8'))
		gender_outLine = "%s\t%s\n" % (int(profile['gender']), _processPunctuation(tweet).encode('utf-8'))
		location_outLine = "%s\t%s\n" % (int(profile['location']), _processPunctuation(tweet).encode('utf-8'))
		
		fp_age.write(age_outLine)
		fp_education.write(education_outLine)
		fp_gender.write(gender_outLine)
		fp_location.write(location_outLine)

	fp_age.close()
	fp_education.close()
	fp_gender.close()
	fp_location.close()

print "Wrote %s profiles" % counter_profiles

db_twitter_female.close()
db_twitter_male.close()
fp_polarity.close()
fp_emotions.close()
