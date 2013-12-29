from models.CitiesCountiesDB import CountiesDB


db = CountiesDB()

countyId = 2
county = db.get(str(countyId))
print county["county"]
print county["cities"]
