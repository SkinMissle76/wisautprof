from apis import Apis
from crawlers import Twitter as Twitter
from models.twitterUser import TwitterUser
from models.twitterUserDB import TwitterUserDB

apiKeys = Apis.Get().Twitter()

tc = Twitter.TwitterCrawler(apiKeys)
u =  tc.getUser(userId=422854771)
print u
u =  tc.getUser(userName="tkrugg")
print u
#
#db = TwitterUserDB()
#db.storeUser(str(u._id), u, u.__str__())

#tc.getPlaces("query")
#res = tc.searchTweets("hello")
#print res[0]

#data = tc.getStream()





