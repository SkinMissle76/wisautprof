from models.AbouemeDB import AboutmeDB
from crawlers.LinkedinDOM import Linkedin

adb = AboutmeDB()  # about.me database
lc  = Linkedin()   # Linkedin crawler
usernames = adb.getAllUsersWithTwitterAndLinkedinProfiles() # interesting profiles

for i, u in enumerate(usernames)[:3]:
  linkedinProfileUrl = adb.getSocialProfile(u, "linkedin")["url"]
  linkedinProfile = lc.getProfile(linkedinProfileUrl)
  print linkedinProfile










