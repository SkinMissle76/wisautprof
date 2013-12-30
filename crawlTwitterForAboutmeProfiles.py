from models.AbouemeDB import AboutmeDB
from crawlers.LinkedinDOM import Linkedin
from models.AboutmeWithProfilesDB import AboutmeWithProfilesDB
import pprint


def fetchTwitterProfile(u, adb, ltadb):
  twitterProfile = None
  return twitterProfile

adb = AboutmeDB()  # about.me database
lc  = Linkedin()   # Linkedin crawler
ltadb = AboutmeWithProfilesDB()

usernames = adb.getAllUsersWithTwitterAndLinkedinProfiles() # interesting profiles

fake = enumerate(usernames[:3])



for i, u in fake:
  print u
  if not ltadb.has(u): # if we've never seen the user
    p = fetchTwitterProfile(u, adb, ltadb)
    ltadb.add(u, p)











