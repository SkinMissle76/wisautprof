from models.BingResultsDB import BingResultsDB
from models.AbouemeDB import AboutmeDB
from crawlers.Aboutme import Aboutme

def fetchAllProfilesFoundWithBing(aboutmeCrawler, bingDB, aboutmeDB):
  profiles = bingDB.getAll()
  nbOfTreatedProfiles = 0
  nbOfProfiles = len(profiles)
  aboutMeProfiles = {}

  for username, profile in profiles.iteritems():
    nbOfTreatedProfiles += 1
    if not adb.has(username):
      print "fetching", username, "   ", nbOfTreatedProfiles, "/", nbOfProfiles
      url = profile["url"]
      aboutMeProfile = ac.getProfile(url)
      adb.add(str(username), aboutMeProfile)
      aboutMeProfiles[username] = aboutMeProfile
  return aboutMeProfiles


ac  = Aboutme()       # about.me crawler
adb = AboutmeDB()     # about.me db
bdb = BingResultsDB() # bing db
fetchAllProfilesFoundWithBing(ac, bdb, adb)

