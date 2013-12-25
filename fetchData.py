from apis import Apis
from crawlers import Twitter as Twitter

apiKeys = Apis.Get().Twitter()

tc = Twitter.TwitterCrawler(apiKeys)

tc.getPlaces("query")
#res = tc.searchTweets("hello")
#print res[0]





