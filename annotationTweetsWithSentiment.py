from models.FinalDBTweets import FinalDBTweets
from models.FinalDBUsers import FinalDBUsers
import re, string, pprint
from lymbix import Lymbix


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

users = fdbu._db.keys()
done = 0
total = len(users)



for i, uid in enumerate(users):
  u = fdbu.get(uid)
  texts = [_processPunctuation(t["text"]) for t in u["tweets"]]

  if not fdbt.hasTweetsOfUser(uid) and len(texts) > 0:
    r = l.tonalize_multiple(texts)
    print uid, i, "/", total, "\t\t\t\t", r
    for j, t in enumerate(u["tweets"]):
      _tid = t["id"]
      _text = t["text"]
      _processedText = _processPunctuation(_text)
      _polarity = 0
      _emotion = 0
      fdbt.add(tweetId=str(_tid), text=_text, processedText=_processedText, sent=r[j], userId=uid)


