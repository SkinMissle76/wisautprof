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

db_codewall = shelve.open("data/coderwall_tweets.shelves")

fp = open("data/manually_tagged/Users_CodeWall.json")
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
	username = str(profile['coderwallUsername'])
	twitterData = None

	if db_codewall.has_key(username):
		# Use female database
		print "User found %s" % username
		twitterData = db_codewall[username]
	else:
		print "Username did not appear is twitter database %s" % username
		continue
	if len(twitterData) == 0:
		continue
	if not profile['age']:
		continue
	directory = "data/manually_tagged/generatedProfiles/%s/" % twitterData[0]['user']['id']
	if not os.path.exists(directory):
		os.makedirs(directory)
	fp_age = open("%slibshorttext_age.txt" % directory, "a")
	fp_education = open("%slibshorttext_education.txt" % directory, "a")
	fp_gender = open("%slibshorttext_gender.txt" % directory, "a")
	fp_location = open("%slibshorttext_location.txt" % directory, "a")

	for tweet in twitterData:
		if len(_processPunctuation(tweet['text'])) <= 3:
			continue
		age = AGE_REAL_TO_SYS(float(profile['age']))
		age_outLine = "%s\t%s\n" % (age, _processPunctuation(tweet['text']).encode('utf-8'))
		education_outLine = "%s\t%s\n" % (int(profile['education']), _processPunctuation(tweet['text']).encode('utf-8'))
		gender_outLine = "%s\t%s\n" % (int(profile['gender']), _processPunctuation(tweet['text']).encode('utf-8'))
		location_outLine = "%s\t%s\n" % (int(profile['location']), _processPunctuation(tweet['text']).encode('utf-8'))
		
		fp_age.write(age_outLine)
		fp_education.write(education_outLine)
		fp_gender.write(gender_outLine)
		fp_location.write(location_outLine)

	fp_age.close()
	fp_education.close()
	fp_gender.close()
	fp_location.close()
	counter_profiles += 1

print "Wrote %s profiles" % counter_profiles

