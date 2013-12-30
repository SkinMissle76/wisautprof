
import shelve
import cPickle as pickle
import urlparse

DATA_DIR = "./data/"
FILE_NAME = "linkedin_twitter_aboutme_profiles_db.shelve"

# aboutme -> (linkedin, twitter)

class AboutmeWithProfilesDB:

  _db = None

  def __init__(self, filename = FILE_NAME):
    self._db = shelve.open(DATA_DIR + filename)

  def _initKey(self, username):
    if not self.has(username):
      self._db[username] = {
        "username" : username
      }


  def addLinkedin(self, username, linkedinObject):
    assert type(username) == str
    self._initKey(username)
    obj = self.get(username)
    obj["linkedin"] = linkedinObject
    self._db[username] = obj

  def addTwitter(self, username, twitterObject):
    assert type(username) == str
    raise NotImplemented

  def has(self, username):
    assert type(username) == str
    return self._db.has_key(username) and self.get(username) != None

  def hasLinkedin(self, username):
    if self.has(username):
      p = self.get(username)
      return p.has_key("linkedin") and p["linkedin"] != None
    else:
      return False

  def hasTwitter(self, username):
    if self.has(username):
      p = self.get(username)
      return p.has_key("twitter") and p["twitter"] != None
    else:
      return False

  def get(self, username):
    assert type(username) == str
    return self._db[username]

  def isLocatedInUK(self, username):
    locality = self.getLocation(username)
    return True

  def getLocation(self, username):
    profile = self.get(username)
    return profile["linkedin"]["locality"]














