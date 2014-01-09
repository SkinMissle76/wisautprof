
import shelve


DATA_DIR = "./data/"
FILE_NAME = "final_db_users_aboutme.shelve"


class FinalDBUsers:
  _db = None

  def __init__(self, filename = FILE_NAME):
    self._db = shelve.open(DATA_DIR + filename)

  def add(self, twitterId, age, gender, education, location, tweets = [], other = {}):
    self._db[twitterId] = {
      "age" : age,
      "gender" : gender,
      "education" : education,
      "location" : location,
      "tweets" : tweets,
      "other" : other
    }
  def get(self, twitterId):
    return self._db[twitterId]