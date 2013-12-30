from crawlers.Bing import Bing
from models.BingResultsDB import BingResultsDB
from models.CitiesCountiesDB import CountiesDB
from models.tables import LOCATIONS_TABLE
from urlparse import urlparse

STORAGE_FILE = "Bing_results_db.shelve"
db = BingResultsDB(filename=STORAGE_FILE)

apiKeys = [
  'y4OkQbeZWhhWu7nV6A2bAZi9DuS0I1WskS4VHlivbK0',
  'zv/DMQadTbSp+MGKRzdnGBnwvZjIj0RWdOiRaQzl/G4',
  '2KbKV5Y0n6oItW2wVgbvmeI4C2uCDNrZnyCgYkg5Kvo']
bc = Bing(apiKeys)

def getLocationsToSearch():
  c_db = CountiesDB()
  cities = c_db.getAllCities()

  #sortedCities = sorted(cities, key = lambda c : c["city"])
  #return sortedCities
  counties = map(lambda c : c["county"], c_db.getAllCounties())
  print counties

def getAllCitiesToSearch()
  c_db = CountiesDB()
  cities = c_db.getAllCities()
  
  sortedCities = sorted(cities, key = lambda c : c["city"])
  return sortedCities

def getAllCountiesToSearch():
  c_db = CountiesDB()
  counties = map(lambda c : c["county"], c_db.getAllCounties())
  print counties

def getOtherLocationKeywordsToSearch():
  return ["United Kingdom", "Great Britain", "UK", "GB"]





def getUsernameFromLink(url):
  path = urlparse(url).path
  username = path[1:]
  return username

def getLink(linkObject, location):
  title = linkObject["Title"]
  url = linkObject["Url"]
  username =  getUsernameFromLink(url)

  return {
    "title"    : title,
    "username" : username,
    "url"      : url,
    "location" : location,
    "raw"      : linkObject
  }




def searchLocation(location, startPage, numberOfPages):
  query = location + " linkedin twitter site:http://about.me"
  results = bc.search(query, startPage, numberOfPages)
  return results




def searchAllLocation():
  allResults = {}
  #for i, l in LOCATIONS_TABLE.iteritems():
  #  print "now searching for profiles from", l
  #  results = searchLocation(l, 0, 15)
  #  formattedResults = map(lambda r : getLink(r, i), results)
  #  for r in formattedResults:
  #    username = r["username"]
  #    allResults[username] = r
  #    db.add(str(username), r)
  #return results

  start = 502
  locations = getLocationsToSearch()
  nbOfLocations = len(locations)
  for i, c in enumerate(locations):
    if i > start:
      print "now searching for profiles from", c["city"], str(i) + "/" + str(nbOfLocations)
      results = searchLocation(c["city"], 0, 10)
      formattedResults = map(lambda r : getLink(r, c), results)
      for r in formattedResults:
        username = r["username"]
        allResults[username] = r
        db.add(str(username), r)

  return allResults



#results = searchAllLocation()
getLocationsToSearch()







