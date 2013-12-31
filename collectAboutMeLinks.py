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
  #counties = getAllCountiesToSearch()
  #return counties
  return getOtherLocationKeywordsToSearch()

def getAllCitiesToSearch():
  c_db = CountiesDB()
  cities = c_db.getAllCities()

  sortedCities = sorted(cities, key = lambda c : c["city"])
  return sortedCities

def getAllCountiesToSearch():
  c_db = CountiesDB()
  counties = map(lambda c : c["county"], c_db.getAllCounties())
  return counties

def getOtherLocationKeywordsToSearch():
  #return ["United Kingdom", "Great Britain", "UK", "GB", "England", "Wales", "Scotland"]
  return ["United Kingdom","England", "Wales", "Scotland"]





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
  query = '"' + location + '"' + ' site:http://about.me'
  print query
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

  start = 0
  locations = getLocationsToSearch()
  nbOfLocations = len(locations)
  "About to search for", nbOfLocations, "locations"
  for i, c in enumerate(locations):
    if i >= start:
      print "now searching for profiles from", c, str(i) + "/" + str(nbOfLocations)
      results = searchLocation(c, 0, 100)
      formattedResults = map(lambda r : getLink(r, c), results)
      for r in formattedResults:
        username = r["username"]
        allResults[username] = r
        db.add(str(username), r)

  return allResults



results = searchAllLocation()







