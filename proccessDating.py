#!/bin/python2.7
from apis import Apis
from crawlers import Twitter
from models.twitterUser import TwitterUser
from models.twitterUserDB import TwitterUserDB
from urllib import urlencode
from urllib2 import urlopen
import sys
import twitter
import re
import json
import time

apiKeys = Apis.Get().Twitter()
STORAGE_FILE = "Twitter_results_db.shelve"
db = TwitterUserDB(filename=STORAGE_FILE)

tc = Twitter.TwitterCrawler(apiKeys)
re_username_find = re.compile(" OkCupid \| (.*?) /")

# Open the dating data
datingData = open("dump5.txt", "r")

for profile in datingData.readlines():
	username = re_username_find.search(profile)
	if username == None:
		print "No username found in: %s" % profile
		continue
	username = username.group(1)
	print "Processing username: %s" % username
	if db.isStored(username):
		print "Username is already stored, skipping..."
		continue
	try:
		u =  tc.getUser(userName=username)
		tl = tc.getUserTimeline(userName=username)
		postCollection = []
		

		for tweet in tl:
			postCollection.append(tweet.GetText())
		
		u.tweets = postCollection
		print "Found %s tweets" % len(u.tweets)
		newUser = TwitterUser(u, u.__str__())
		newUser.tweets = postCollection
		db.storeUser(username, newUser, newUser.jsonify())
		print "User saved"
	# Something went wrong, store empty userdata to prevent revisit
	except twitter.TwitterError as e:
		db.storeUser(username, None, "")
		print "No twitter profile found for username: %s" % username
	time.sleep(10)
#	sys.exit(0)
#
#url = "http://uclassify.com/browse/uClassify/Ageanalyzer/ClassifyText?"
#
#parameters = {
#	'readkey': 'yzom2rtR7ARGsLWqxfNqSJXxvEA',
#	'text': postCollection.encode("utf-8"),
#	'version': '1.01'}
#
#apiURL = url + urlencode(parameters)
#
#print urlopen(apiURL).read()
