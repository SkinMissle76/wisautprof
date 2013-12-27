
import shelve
import cPickle as pickle

DATA_DIR = "./data/"
FILE_NAME = "coderwall_user_db.shelve"

class CoderwallUserDB:

  _db = None

  def __init__(self, filename = FILE_NAME):
    self._db = shelve.open(DATA_DIR + filename)

  def storeUser(self, username, userObject):
    assert type(username) == str
    self._db[username] = userObject
    
  def isStored(self, username):
    assert type(username) == str
    return self._db.has_key(username)

  def numberOfUsers(self):
    return len(self._db)

  def getAllTwitterUsers(self):
    twitterUsers = filter(lambda u : self._hasTwitterProfile(u), self._db)
    return twitterUsers

  def _processAll(self):
    return None

  # user scale
  def _hasTwitterProfile(self, username):
    sl = self.getSocialLinks(username)
    matches = filter(lambda l : l["website"] == "twitter", sl)
    assert len(matches) <= 1 # there shouldn't be more than one

    return len(matches) == 1

  def getTwitterProfile(self, username):
    return self.getSocialNetwork(username, "twitter")

  def getSocialNetwork(self, username, website):
    assert website in ["twitter", "github", "linkedin"] # TODO refactor this with KNOwN_SOCIAL_NETWOKS

    sl = self.getSocialLinks(username)
    matches = filter(lambda l : l["website"] == website, sl)
    assert len(matches) <= 1 # there shouldn't be more than one

    return matches[0]

  def getSocialLinks(self, username):
    user = self.get(username)
    socialLinks = filter(lambda l : l != None, user["socialLinks"])
    return socialLinks


  def get(self, username):
    assert type(username) == str
    user = self._db[username]
    return user







