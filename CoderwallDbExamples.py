
from crawlers.Coderwall import Coderwall
from models.CoderwallUserDB import CoderwallUserDB


db = CoderwallUserDB()

twitterUsers = db.getAllTwitterUsers()
print len(twitterUsers)
