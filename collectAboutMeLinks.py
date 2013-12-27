from crawlers.Bing import Bing
from models.BingResultsDB import BingResultsDB
from models.tables import LOCATIONS_TABLE
from urlparse import urlparse

STORAGE_FILE = "Bing_results_db.shelve"
db = BingResultsDB(filename=STORAGE_FILE)

apiKeys = ['2KbKV5Y0n6oItW2wVgbvmeI4C2uCDNrZnyCgYkg5Kvo']
bc = Bing(apiKeys)


def getUsernameFromLink(url):
  path = urlparse(url).path
  username = path[1:]
  return username

def getLink(linkObject, locationID):
  title = linkObject["Title"]
  url = linkObject["Url"]
  username =  getUsernameFromLink(url)

  return {
    "title"    : title,
    "username" : username,
    "url"      : url,
    "location" : locationID,
    "raw"      : linkObject
  }




def searchLocation(location, startPage, numberOfPages):
  query = location + " linkedin twitter site:http://about.me"
  results = bc.search(query, startPage, numberOfPages)
  return results




def searchAllLocation():
  allResults = {}
  for i, l in LOCATIONS_TABLE.iteritems():
    print "now searching for profiles from", l
    results = searchLocation(l, 0, 10)
    formattedResults = map(lambda r : getLink(r, i), results)
    for r in formattedResults:
      username = r["username"]
      allResults[username] = r
      db.add(str(username), r)
  return results



results = searchAllLocation()






