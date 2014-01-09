from models.FinalDBTweets import FinalDBTweets
import json 



db = FinalDBTweets()
#db = {k:"hello"+str(k) for k in range(1,100) }

def storeInFiles():
  FOLDER = "data/autolabeledtweets/"
  count = 0
  limit = 2000
  filecount = 0

  def fileName(num):
    return FOLDER + "tweets_" + str(int(num))

  f = open(fileName( 0 ), "w+")

  for k in db._db.keys():
    count += 1

    if count % limit == 0:
      filecount += 1
      f = open(fileName( filecount ), "w+")

    e = json.dumps(db._db[k])
    print >> f, e 

storeInFiles()
