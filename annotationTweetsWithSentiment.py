from models.FinalDBTweets import FinalDBTweets
from models.FinalDBUsers import FinalDBUsers
import re, string
from lymbix import Lymbix

def _preprocess(text):
  return re.sub(r'^')id

def _processPunctuation(text):
  t = re.sub("https?:\/\/.*(\s+|$)", '', text)
  t = t.replace("\n", "").replace("'", "")

  for p in string.punctuation:
    t = t.replace(p, " "+p+" ")

  return t

apikey = "8a77503e17148fb5f3d5fd7d1e80ce86c23b6133"
l = Lymbix(apikey)
fdbu = FinalDBUsers()
fdbt = FinalDBTweets()

users = fdbu._db.values()
done = 0
total = len(users)

for u in users[:3]:
  for t in u["tweets"]:

    _tid = t["id"]
    _text = t["text"]
    _sentiment = 0
    _polarity = 0
    print _tid, _text
  r = l.tonalize_multiple(["I love you", "I hate you"])

