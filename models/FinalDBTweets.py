
import shelve
from classifiers.SentimentPolarityEmotion import SentimentPolarityEmotionClassifier


DATA_DIR = "./data/"
FILE_NAME = "final_db_tweets.shelve"


class FinalDBTweets:
  _db = None
  _uids = None

  def __init__(self, filename = FILE_NAME):
    self._db = shelve.open(DATA_DIR + filename)
    self._uids =[]#[t["user"] for t in self._db.values()]

  def add(self, tweetId, text, processedText, sent, userId):
    self._db[tweetId] = {
      "text" : text,
      "processedText" : processedText,
      "sent" : sent,
      "user" : userId
    }
  def hasTweetsOfUser(self, userid):
    return userid in self._uids

  def update(self, tweetId, polarity, emotion):
    tweet = self._db[str(tweetId)]
    tweet["polarity"] = polarity
    tweet["emotion"] = emotion
    self._db[str(tweetId)] = tweet.copy()

  def updateAllPolaritysAndEmotions(self):
    spec = SentimentPolarityEmotionClassifier()
    for tid in self._db.keys():
      tweet = self._db[tid]
      polarity = spec.getPolarity(tweet["sent"])
      emotion =  spec.getEmotion(tweet["sent"])
      self.update(tid, polarity, emotion)




#d = FinalDBTweets()
#print len(d)
