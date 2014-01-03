from models.AbouemeDB import AboutmeDB
from crawlers.LinkedinDOM import Linkedin
from apis import Apis
from crawlers.Twitter import TwitterCrawler
from models.AboutmeWithProfilesDB import AboutmeWithProfilesDB
import twitter
import pprint
import urlparse
import time
import shelve

OVERWRITE = False

def fetchTwitterProfile(u, adb, ltadb):
  twitterProfile = None
  return twitterProfile

adb = AboutmeDB()
ltadb = AboutmeWithProfilesDB()

def _getTwitterUrl(u, adb):
  twitterProfiles = adb.getSocialProfile(u, "twitter")
  firsttwitterProfile = twitterProfiles[0]
  return  firsttwitterProfile["url"]

def _getTwitterUsernameFromUrl(url):
  path = urlparse.urlparse(url).path
  username = path[1:]
  return username

def getTwitterUsername(u, adb):
  twitterUrl = _getTwitterUrl(u, adb)
  return _getTwitterUsernameFromUrl(twitterUrl)

def fetchTwitterProfile(aboutmeUsername, adb, tc):
  tu = getTwitterUsername(aboutmeUsername, adb)
  tProfile = tc.getUser(userName = tu)
  return {
    "profile"  : tProfile.AsDict()
  }


def fetchAllTwitterProfiles(aboutmeUsernames, adb, ltadb, tc):
  unfoundAccountsDB = shelve.open("data/_blankTwitterAccounts.shelves")
  unfounds = unfoundAccountsDB["unfound"]
  total = len(aboutmeUsernames)
  done = 0
  for u in aboutmeUsernames:
    done += 1
    if (not ltadb.hasTwitter(u) or OVERWRITE) and not (u in unfoundAccountsDB["unfound"]):
      try:
        print "now fetching", u, done, "/", total
        tp = fetchTwitterProfile(u, adb, tc)
        ltadb.addTwitter(u, tp)
      except twitter.TwitterError as obj:
        print obj
        if obj.message[0]["code"] == 34: # user unfound
          print "--- print skipping this one, couldn't find id"
          unfounds.append(u)
          unfoundAccountsDB["unfound"] = unfounds
        elif obj.message[0]["code"] == 88: # limit exceeded
          print "waiting..."
          for i in range(15*60):
            time.sleep(1)
            print "waiting...", i/60.0





usernames = ltadb._db.keys()

locatedInUkUsernames = filter(ltadb.isLocatedInUK, usernames) # interesting profiles
print "# found", len(locatedInUkUsernames), \
  " profile in AboutmeDB over", len(usernames),\
  "that come from the UK"

print "fetching now their twitter profiles"

apiKeys = Apis.Get().Twitter()
tc = TwitterCrawler(apiKeys)

fetchAllTwitterProfiles(locatedInUkUsernames, adb, ltadb, tc)