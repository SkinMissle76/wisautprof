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


