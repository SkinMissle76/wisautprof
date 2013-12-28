from models.CitiesCountiesDB import CountiesDB


filename = "counties_db.shelves"    # this is a file located in /data/
db = CountiesDB(filename)

countyId = 2
county = db.get(str(countyId))
print county["county"]
print county["cities"]
