#!/bin/python2.7
import shelve
import sys
import json
import re
import urllib
import urllib2
import time
import string

from bs4 import BeautifulSoup
db_twitter_female = shelve.open("data/Twitter_results_db_dump_FEMALE.shelve")
db_twitter_male = shelve.open("data/Twitter_results_db_dump_MALE.shelve")

fp = open("data/manually_tagged/tweets_labeled.json")
tweetData = fp.read()
fp.close()
tweetData = json.loads(tweetData)

fp_polarity = open("data/manually_tagged/generated_polarity.txt", "a")
fp_emotions = open("data/manually_tagged/generated_emotions.txt", "a")

def _processPunctuation(text):
	t = re.sub("https?:\/\/.*(\s+|$)", '', text)
	t = t.replace("\n", "").replace("'", "")

	for p in string.punctuation:
		t = t.replace(p, " "+p+" ")

	return t


counter_polarity = 0
counter_emotions = 0
for tweet in tweetData:
	if tweet.has_key('text') and tweet.has_key('id') and tweet.has_key('polarity') and tweet.has_key('emotions'):
		# Dump the polarity
		if tweet['polarity']:
			outLine = "%s\t%s\n" % (tweet['polarity'], _processPunctuation(tweet['text'].encode('utf-8')))
			fp_polarity.write(outLine)
			counter_polarity += 1

		# Dump the emotion if available
		if tweet['emotions']:
			outLine = "%s\t%s\n" % (tweet['emotions'], _processPunctuation(tweet['text'].encode('utf-8')))
			fp_emotions.write(outLine)
			counter_emotions += 1
			
		# No emotion detected, so we use neutral
		else:
			outLine = "%s\t%s\n" % (0, _processPunctuation(tweet['text'].encode('utf-8')))
			fp_emotions.write(outLine)
			counter_emotions += 1
	else:
		print "Tweet does not have all the data"

print "Wrote %s tweets to polarity" % counter_polarity
print "Wrote %s tweets to emotions" % counter_emotions

db_twitter_female.close()
db_twitter_male.close()
fp_polarity.close()
fp_emotions.close()
