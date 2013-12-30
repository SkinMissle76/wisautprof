from models.AbouemeDB import AboutmeDB
from crawlers.LinkedinDOM import Linkedin
from models.AboutmeWithProfilesDB import AboutmeWithProfilesDB
import pprint

OVERWRITE = False

def fetchLinkedinProfile(u, adb):
  linkedinProfileInfo = adb.getSocialProfile(str(u), "linkedin")
  url = linkedinProfileInfo[0]["url"]
  print url
  linkedinProfile = lc.getProfile(url)
  #pprint.pprint(linkedinProfile)
  return linkedinProfile

adb = AboutmeDB()  # about.me database
lc  = Linkedin()   # Linkedin crawler
ltadb = AboutmeWithProfilesDB()

usernames = adb.getAllUsersWithTwitterAndLinkedinProfiles() # interesting profiles

fake = enumerate(usernames)

done = 0
total = len(usernames)

for i, u in fake:
  done += 1
  if not ltadb.hasLinkedin(str(u)) or OVERWRITE:
    print "now fetching linkedin profile for", u, done, "/", total
    p = fetchLinkedinProfile(u, adb)
    ltadb.addLinkedin(str(u), p)


  #print linkedinProfile










