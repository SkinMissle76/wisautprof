from __future__ import print_function
import twitter
from models.tables import LOCATIONS_TABLE
import json
from pprint import pprint as PP


### TODO refactor this part
def countdown(t): # in seconds
  import time
  for i in range(t,0,-1):
    print ("tasks done, now sleeping for %d seconds " + str(i))
    time.sleep(1)

###

class TwitterCrawler:
  apis = None
  _currentlyUsedApi = 1

  def __init__(self, apiKeys):
    self.apis = [self._makeApi(apiKey) for apiKey in apiKeys]

  def _makeApi(self, apiKey):
    return twitter.Api(
      consumer_key =         apiKey['consumer_key'],
      consumer_secret =      apiKey['consumer_secret'],
      access_token_key =     apiKey['access_token_key'],
      access_token_secret =  apiKey['access_token_secret'])

  def _getApi(self):
    return self.apis[self._currentlyUsedApi]

  def _switchApi(self):
    self._currentlyUsedApi = (self._currentlyUsedApi + 1) % len(self.apis)

  def searchTweets(self, term, max_id = None):
    searchResults = self.apis[0].GetSearch(
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

  def getUser(self, userId):
    user = self.apis[0].GetUser(userId)

    return user

  def getPlaces(self, query):

    url = "https://api.twitter.com/1.1/geo/search.json"

    _rateCount = 0
    datafileName = "data/twitter_places_0"
    f = open(datafileName,'w')
    for locationId in LOCATIONS_TABLE.keys():
      print ("working with location " + str(locationId))

      locationName = LOCATIONS_TABLE[locationId ]
      parameters = {}
      parameters['query'] = locationName
      parameters['granularity'] = 'city'

      try:
        r = self._getApi()._RequestUrl(url, 'GET', data=parameters)
        data = self._getApi()._ParseAndCheckTwitter(r.content)
        places = data["result"]["places"]
        allowed_country_codes = ["GB"]
        only_uk_places = filter(lambda p : p["country_code"] in allowed_country_codes, places)

        print(json.dumps({
                "id" : locationId,
                "name": locationName,
                "places": [p for p in only_uk_places]
              }), file=f)
      except Exception:
        print("Oops, Api limit reached")
        countdown(15*60)
        _rateCount += 1
        datafileName = "data/twitter_places__" + str(_rateCount)
        f = open(datafileName,'w')
        print("Just switched to file " + datafileName)

        r = self._getApi()._RequestUrl(url, 'GET', data=parameters)
        data = self._getApi()._ParseAndCheckTwitter(r.content)
        places = data["result"]["places"]
        allowed_country_codes = ["GB"]
        only_uk_places = filter(lambda p : p["country_code"] in allowed_country_codes, places)

        print(json.dumps({
          "id" : locationId,
          "name": locationName,
          "places": [p for p in only_uk_places]
        }), file=f)













  #def searchUsersByLocation(self, location):





