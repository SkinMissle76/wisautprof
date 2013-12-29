
import shelve
import cPickle as pickle
import urlparse

DATA_DIR = "./data/"
FILE_NAME = "Bing_results_db.shelve"

class BingResultsDB:

  _db = None

  def __init__(self, filename = FILE_NAME):
    self._db = shelve.open(DATA_DIR + filename)

  def add(self, username, linkObject):
    assert type(username) == str
    self._db[username] = linkObject
    
  def has(self, username):
    assert type(username) == str
    return self._db.has_key(username) and self.get(username) != None

  def numberOfResults(self):
    return len(self._db)

  def get(self, username):
    assert type(username) == str
    return self._db[username]

  def getAll(self):
    profiles = {}
    for username in self._db.keys():
      profiles[username] = self.get(username)
    return profiles




