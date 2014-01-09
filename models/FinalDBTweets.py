
import shelve


DATA_DIR = "./data/"
FILE_NAME = "final_db_tweets.shelve"


class FinalDBTweets:
  _db = None

  def __init__(self, filename = FILE_NAME):
    self._db = shelve.open(DATA_DIR + filename)

  def add(self, tweetId, polarity, emotion, text):
    self._db[tweetId] = {
      "text" : text,
      "polarity" : polarity,
      "emotion" : emotion
    }