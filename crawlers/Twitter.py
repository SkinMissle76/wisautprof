from __future__ import print_function
import twitter
#from twython import TwythonStreamer
from models.tables import LOCATIONS_TABLE
import json
from pprint import pprint as PP


### TODO refactor this part
def countdown(t): # in seconds
  import time
  for i in range(t,0,-1):
    print ("tasks done, now sleeping for %d seconds " + str(i))
    time.sleep(1)

#class MyStreamer(TwythonStreamer):
#  def on_success(self, data):
#    if 'text' in data:
#      print(data)
#
#  def on_error(self, status_code, data):
#    print (status_code)
#
#      # Want to stop trying to get data because of the error?
#      # Uncomment the next line!
#      # self.disconnect()
#
####

class TwitterCrawler:
  apis1 = None
  _currentlyUsedApi = 1

  def __init__(self, apiKeys):
    self.apis1 = [self._makeApi1(apiKey) for apiKey in apiKeys]
    self.apis2 = [self._makeApi2(apiKey) for apiKey in apiKeys]

  def _makeApi1(self, apiKey): # python-twitter
    return twitter.Api(
      consumer_key =         apiKey['consumer_key'],
      consumer_secret =      apiKey['consumer_secret'],
      access_token_key =     apiKey['access_token_key'],
      access_token_secret =  apiKey['access_token_secret'])

  def _makeApi2(self, apiKey): # twython
    return twitter.Api(
      apiKey['consumer_key'],
      apiKey['consumer_secret'],
      apiKey['access_token_key'],
      apiKey['access_token_secret'])

  def _getApi1(self):
    return self.apis1[self._currentlyUsedApi]

  def _switchApi(self):
    self._currentlyUsedApi = (self._currentlyUsedApi + 1) % len(self.apis1)

  def searchTweets(self, term, max_id = None):
    searchResults = self.apis1[0].GetSearch(
        term=term, 
        geocode=None, 
        since_id=None, 
        max_id=max_id, 
        until=None, 
        count=20, 
        lang="en", 
        locale=None, 
        result_type='mixed', 
        include_entities=None)
    #tweets = []
    #for result in searchResults:
    #  raw_r = str(result).replace('\r\n', '')
    #  #r = json.loads(raw_r)
    #  #t = Tweet(id = r["id"], content = r["text"], raw = raw_r, searchTerms = term)
    #  #print t.content
    #  #tweets.append(t)
    #  print raw_r

    #return json.dumps(map(lambda x : x.getJSON(), tweets))
    return searchResults

  def widesearch(self, term, loops=2):
    res = []

    for i in range(loops):
      if len(res) > 0:
        maxId = res[-1].id
        sr = self.searchTweets(term, max_id=maxId)
      else:
        sr = self.searchTweets(term)

      res.extend(sr)

    return res

  def getUser(self, userId = None, userName = None):
    if userId != None:
      user = self.apis1[0].GetUser(userId)
    elif userName != None:
      user = self.apis1[0].GetUser(screen_name = userName)
    else:
      raise ValueError("Neither userId or userName were specified")

    return user

  def getUserTimeline(self, userId = None, userName = None, count = 200):
    if userId != None:
      userTimeline = self.apis1[0].GetUserTimeline(user_id = userId,
                                                   count = count,
                                                   include_rts = False,
                                                   trim_user=True)
    elif userName != None:
      userTimeline = self.apis1[0].GetUserTimeline(screen_name = userName,
                                                   count = count,
                                                   include_rts = False,
                                                   trim_user=True)
    else:
      raise ValueError("Neither userId or userName were specified")

    return userTimeline


  #def getStream(self):
  #  return self.apis2[0].statuses.filter(track="twitter")

#  def getPlaces(self, query):

#    url = "https://api.twitter.com/1.1/geo/search.json"

#    _rateCount = 0
#    datafileName = "data/twitter_places_0"
#    f = open(datafileName,'w')
#    for locationId in LOCATIONS_TABLE.keys():
#      print ("working with location " + str(locationId))

#      locationName = LOCATIONS_TABLE[locationId ]
#      parameters = {}
#      parameters['query'] = locationName
#      parameters['granularity'] = 'city'

#      try:
#        r = self._getApi1()._RequestUrl(url, 'GET', data=parameters)
#        data = self._getApi1()._ParseAndCheckTwitter(r.content)
#        places = data["result"]["places"]
#        allowed_country_codes = ["GB"]
#        only_uk_places = filter(lambda p : p["country_code"] in allowed_country_codes, places)

#        print(json.dumps({
#                "id" : locationId,
#                "name": locationName,
#                "places": [p for p in only_uk_places]
#              }), file=f)
#      except Exception:
#        print("Oops, Api limit reached")
#        countdown(15*60)
#        _rateCount += 1
#        datafileName = "data/twitter_places__" + str(_rateCount)
#        f = open(datafileName,'w')
#        print("Just switched to file " + datafileName)

#        r = self._getApi1()._RequestUrl(url, 'GET', data=parameters)
#        data = self._getApi1()._ParseAndCheckTwitter(r.content)
#        places = data["result"]["places"]
#        allowed_country_codes = ["GB"]
#        only_uk_places = filter(lambda p : p["country_code"] in allowed_country_codes, places)

#        print(json.dumps({
#          "id" : locationId,
#          "name": locationName,
#          "places": [p for p in only_uk_places]
#        }), file=f)













  #def searchUsersByLocation(self, location):





