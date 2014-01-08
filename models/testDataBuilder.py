import shelve, json, os, string, shutil
from classifiers.Education import OkcupidEducation, EDUCATION_TABLE_INVERTED

EC = OkcupidEducation()

SOURCE_DIRECTORY = "data/"  # where the shelve files are stores
TARGET_DIRECTORY = "data/test_data/"
TARGET_DIRECTORY_TESTING  = TARGET_DIRECTORY + "for_testing/Demographics/"
TARGET_DIRECTORY_TRAINING = TARGET_DIRECTORY + "for_training/Demographics/"

class testDataBuilder:
  _db = None
  _nbOfTrainingTweets = 0
  _nbOfTestingTweets = 0
  _nbOfValidUsers = 0

  _currentUserPath = None

  def __init__(self, shelveFilename):
    self._db = shelve.open(SOURCE_DIRECTORY + shelveFilename)
    self._targetPath = TARGET_DIRECTORY

  def _processPunctuation(self, text):
    t = text.encode("ascii", "ignore")\
      .replace("\n", "").replace("'", "")

    for p in string.punctuation:
      t = t.replace(p, " "+p+" ")

    return t

  def _mustBeAddedToTrainingSet(self):
    total = self._nbOfTrainingTweets + self._nbOfTestingTweets
    return self._nbOfTrainingTweets < total*2/3.0

  def run(self):
   print "contains", len(self._db), "profiles"
   print "contains", len(self._db), "profiles"
   for k, v in self._db.iteritems():
     u = json.loads(self._db[k])
     uid = u["userid"]
     tweets = u["tweets"]
     tweets = [self._processPunctuation(t)
               for t in tweets]


     if u["education"] is not None:
       edu = EC.getEducationLevelFromString(u["education"])
     else:
       edu = EDUCATION_TABLE_INVERTED["Mid"]

     print uid, len(tweets), self._nbOfValidUsers
     if len(tweets) > 0:
       self._nbOfValidUsers+=1
       self._declareUser(uid, tweets)
       self._buildAgeData(uid, u["age"], tweets)
       self._buildGenderData(uid, u["gender"], tweets)
       self._buildEducationData(uid, edu, tweets)
       self._buildLocationData(uid, u["location"], tweets)

  def _declareUser(self, uid, tweets):
    if self._mustBeAddedToTrainingSet():
      path = self._makeUserPath(uid, training=True)
      self._nbOfTrainingTweets += len(tweets)
    else:
      path = self._makeUserPath(uid, training=False)
      self._nbOfTestingTweets += len(tweets)

    self._currentUserPath = path
    folderExists = os.path.exists(path)

    if folderExists:
      shutil.rmtree(path)

    os.mkdir(path)




  def _buildAgeData(self, uid, age, tweets):
    self._buildData(uid, "age", age, tweets)

  def _buildGenderData(self, uid, gender, tweets):
    self._buildData(uid, "gender", gender, tweets)

  def _buildEducationData(self, uid, education, tweets):
    self._buildData(uid, "education", education, tweets)

  def _buildLocationData(self, uid, location, tweets):
    self._buildData(uid, "location", location, tweets)

  # helpers
  def _buildData(self, uid, dataName, dataValue, tweets):
    if self._mustBeAddedToTrainingSet():
      path = self._makeDataPath(uid, dataName)
    else:
      path = self._makeDataPath(uid, dataName)

    content = ""
    for t in tweets:
      content += self._buildDataLine(dataValue, t)
    self._writeIntoFile(content, path)

  def _makeUserPath(self, uid, training=False):
    if training:
      return TARGET_DIRECTORY_TRAINING + str(uid) + "/"
    else:
      return TARGET_DIRECTORY_TESTING + str(uid) + "/"

  def _getUserPath(self):
    return self._currentUserPath


  def _makeDataPath(self, uid, dataName, training=False):
    return self._getUserPath() + "libshorttext_"+ dataName + ".txt"

  def _writeIntoFile(self, content, path):
    print "writing into", path
    c = content.encode("utf-8")
    f = open(path, "w+")
    f.write(c)
    f.close()

  def _buildDataLine(self, dataValue, tweetText):
    return str(dataValue) + "\t" + tweetText + "\n"














