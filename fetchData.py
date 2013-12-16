from apis import Apis
from crawlers import Twitter as Twitter

apiKey = Apis.Get().Twitter()

tc = Twitter.TwitterCrawler(apiKey[0])
res = tc.searchTweets("hello")
print res[0]




