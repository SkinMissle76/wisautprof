import twitter


class TwitterCrawler:
  api = None
  def __init__(self, apiKeys):
    self.api = twitter.Api(
        consumer_key =         apiKeys['consumer_key'],
        consumer_secret =      apiKeys['consumer_secret'],
        access_token_key =     apiKeys['access_token_key'],
        access_token_secret =  apiKeys['access_token_secret'])

  def searchTweets(self, term, max_id = None):
    searchResults = self.api.GetSearch(
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
    user = self.api.GetUser(userId)
    return user


