
import shelve
import cPickle as pickle

DATA_DIR = "./data/"
FILE_NAME = "twitter_user_db.shelve"

class TwitterUserDB:

  _db = None

  def __init__(self, filename = FILE_NAME):
    self._db = shelve.open(DATA_DIR + filename)

  def storeUser(self, userId, userObj, userRaw):
    if type(userId) != str:
      raise TypeError("Yo, userId is supposed to be a str, make it str(userId)")
    self._db[userId] = {
      "object" : pickle.dumps(userObj),    # the actual object
      "str" : userRaw                      # saved just in case the "object" is screwed
    }
    
  def isStored(self, userId):
    if type(userId) != str:
      raise TypeError("Yo, userId is supposed to be a str, make it str(userId)")
    return self._db.has_key(userId)


