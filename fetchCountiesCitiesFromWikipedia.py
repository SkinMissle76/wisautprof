from models.CitiesCountiesDB import CountiesDB
from crawlers.WikipediaUkCities import WikipediaUKCities



db = CountiesDB()
wc = WikipediaUKCities()

counties = wc.getCounties()
print "fetched information for", len(counties.keys()), "counties"

for i,c in counties.iteritems():
  db.add(str(i), c)



