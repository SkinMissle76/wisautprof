import shelve, json, os, string, shutil, re
from classifiers.Education import OkcupidEducation, EDUCATION_TABLE_INVERTED
from classifiers.SentimentPolarityEmotion import SentimentPolarityEmotionClassifier

EC = OkcupidEducation()

SOURCE_DIRECTORY = "data/"  # where the shelve files are stores
TARGET_DIRECTORY = "data/test_data/"
D_TARGET_DIRECTORY_TESTING  = TARGET_DIRECTORY + "for_testing/Demographics/"
D_TARGET_DIRECTORY_TRAINING = TARGET_DIRECTORY + "for_training/Demographics/"
S_TARGET_DIRECTORY_TESTING  = TARGET_DIRECTORY + "for_testing/Sentiment/"
S_TARGET_DIRECTORY_TRAINING = TARGET_DIRECTORY + "for_training/Sentiment/"

class SentimentTestDataBuilder:
  _db = None
  EMOTION_FILENAME_TESTING = S_TARGET_DIRECTORY_TESTING + "emotion_libshorttext.txt"
  EMOTION_FILENAME_TRAINING = S_TARGET_DIRECTORY_TRAINING + "emotion_libshorttext.txt"
  POLARITY_FILENAME_TESTING = S_TARGET_DIRECTORY_TESTING + "polarity_libshorttext.txt"
  POLARITY_FILENAME_TRAINING = S_TARGET_DIRECTORY_TRAINING + "polarity_libshorttext.txt"

  _nbOfTrainingTweets = 0
  _nbOfTestingTweets = 0

  def __init__(self, shelveFilename):
    self._db = shelve.open(SOURCE_DIRECTORY + shelveFilename)
    self._targetPath = TARGET_DIRECTORY
    self._emptyFolder(S_TARGET_DIRECTORY_TESTING)
    self._emptyFolder(S_TARGET_DIRECTORY_TRAINING)

  def _emptyFolder(self, path):
    for root, dirs, files in os.walk(path):
      for f in files:
        os.unlink(os.path.join(root, f))
      for d in dirs:
        shutil.rmtree(os.path.join(root, d))

  def _mustBeAddedToTrainingSet(self):
    total = self._nbOfTrainingTweets + self._nbOfTestingTweets
    return self._nbOfTrainingTweets < total*2/3.0

  def run(self):
    nbOfTrainingElements = len(self._db.keys())*2/3
    count = 0
    pfileTraining = open(self.POLARITY_FILENAME_TRAINING, "w+")
    efileTraining = open(self.EMOTION_FILENAME_TRAINING, "w+")
    pfileTesting = open(self.POLARITY_FILENAME_TESTING, "w+")
    efileTesting = open(self.EMOTION_FILENAME_TESTING, "w+")
    for i, t in self._db.iteritems():
      count += 1
      p = t["polarity"]
      e = t["emotion"]
      text = t["processedText"].encode("ascii", "ignore")
      if count < nbOfTrainingElements:
        print >> pfileTraining, self._buildDataLine(p, text)
        print >> efileTraining, self._buildDataLine(e, text)
      else:
        print >> pfileTesting, self._buildDataLine(p, text)
        print >> efileTesting, self._buildDataLine(e, text)



  def _writeIntoFile(self, content, path):
    print "writing into", path
    c = content.encode("utf-8")
    f = open(path, "w+")
    f.write(c)
    f.close()

  def _buildDataLine(self, dataValue, tweetText):
    return str(dataValue) + "\t" + tweetText






class DemographicsTestDataBuilder:
  _db = None
  _nbOfTrainingTweets = 0
  _nbOfTestingTweets = 0
  _nbOfValidUsers = 0

  _currentUserPath = None

  def __init__(self, shelveFilename):
    self._db = shelve.open(SOURCE_DIRECTORY + shelveFilename)
    self._targetPath = TARGET_DIRECTORY
    self._emptyFolder(D_TARGET_DIRECTORY_TESTING)
    self._emptyFolder(D_TARGET_DIRECTORY_TRAINING)

  def _emptyFolder(self, path):
    for root, dirs, files in os.walk(path):
      for f in files:
        os.unlink(os.path.join(root, f))
      for d in dirs:
        shutil.rmtree(os.path.join(root, d))


  def _processPunctuation(self, text):
    t = re.sub("https?:\/\/.*(\s+|$)", '', text)
    t = t.replace("\n", "").replace("'", "")

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
     #u = json.loads(self._db[k])
     u = v
     uid = k
     tweets = u["tweets"]
     tweets = [self._processPunctuation(t["text"])
               for t in tweets]


     edu = u["education"]

     print uid, len(tweets), self._nbOfValidUsers
     if len(tweets) > 10:
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
      return D_TARGET_DIRECTORY_TRAINING + str(uid) + "/"
    else:
      return D_TARGET_DIRECTORY_TESTING + str(uid) + "/"

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
















