import shelve


DATA_DIR = "./data/"
FILE_NAME = "counties_db.shelve"

class CountiesDB:

  _db = None

  def __init__(self, filename = FILE_NAME):
    self._db = shelve.open(DATA_DIR + filename)

  def add(self, countyId, countyObject):
    assert type(countyId) == str
    self._db[countyId] = countyObject

  def has(self, countyId):
    assert type(countyId) == str
    return self._db.has_key(countyId)

  def get(self, countyId):
    assert type(countyId) == str
    if self.has(countyId):
      return self._db[countyId]
    else:
      raise ValueError("countyId " + countyId + " has not been found, sorry")

  def getCountyByName(self, countyName):
    counties = self.getAllCounties()
    matches = filter(lambda c : str.lower(c["county"]) == str.lower(countyName),
                     counties)
    if len(matches) > 0:
      return matches[0]["countyId"]
    else:
      return None

  def getAllCounties(self):
    return [self.get(c) for c in self._db.keys()]

  def getAllCities(self):
    cities = []
    for c in self.getAllCounties():
      cities.extend(c["cities"])
    return cities

  def getCity(self, cityName):
    cities = self.getAllCities()
    matches = filter(lambda c : str.lower(str(c["city"]))
                             == str.lower(str(cityName)), cities)
    if len(matches) > 0:
      return matches[0]
    else:
      return None

  def getCityCounty(self, cityName):
    city = self.getCity(cityName)
    if city != None:
      return city["countyId"]
    else:
      return None



  def addCityToCounty(self, countyId, cityName):
    county = self.get(countyId)
    county["cities"].append({
      'city': cityName,
      'county': county["county"],
      'countyId': county["countyId"]
    })
    self._db[str(county["countyId"])] = county.copy()






