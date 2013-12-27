
from crawlers.Coderwall import Coderwall
from models.CoderwallUserDB import CoderwallUserDB
import urllib2
import urlparse

db = CoderwallUserDB()

twitterUsers = db.getAllTwitterUsers()
githubUsers = db.getAllGithubUsers()
linkedinUsers = db.getAllLinkedinUsers()

print len(twitterUsers)
print len(githubUsers)
print len(linkedinUsers)

print [db.getTwitterUsername(u) for u in twitterUsers]

inter = set(twitterUsers) & set(linkedinUsers) & set(githubUsers)
print len(inter)
print inter

#print [db.getTwitterProfile(u) for u in twitterUsers]
