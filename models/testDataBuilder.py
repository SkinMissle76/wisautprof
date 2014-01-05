import shelve, json, os

SOURCE_DIRECTORY = "data/"  # where the shelve files are stores
TARGET_DIRECTORY = "data/test_data/"

class testDataBuilder:
  _db = None

  def __init__(self, shelveFilename):
    self._db = shelve.open(SOURCE_DIRECTORY + shelveFilename)

  def run(self):
   for k, v in self._db.iteritems():
     u = json.loads(self._db[k])
     uid = u["userid"]
     tweets = u["tweets"]
     self._declareUser(uid)
     self._buildAgeData(uid, u["age"], tweets)
     self._buildGenderData(uid, u["gender"], tweets)
     self._buildEducationData(uid, u["education"], tweets)
     self._buildLocationData(uid, u["location"], tweets)

     print uid

  def _declareUser(self, uid):
    path = self._getUserPath(uid)
    try:
      os.stat(path)
    except:
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
    path = self._makeDataPath(uid, dataName)
    content = ""
    for t in tweets:
      content += self._buildDataLine(dataValue, t)
    self._writeIntoFile(content, path)

  def _getUserPath(self, uid):
    return TARGET_DIRECTORY + str(uid) + "/"

  def _makeDataPath(self, uid, dataName):
    return self._getUserPath(uid) + "libshorttext_"+ dataName + ".txt"

  def _writeIntoFile(self, content, path):
    print "writing into", path
    c = content.encode("utf-8")
    f = open(path, "w+")
    f.write(c)
    f.close()

  def _buildDataLine(self, dataValue, tweetText):
    return str(dataValue) + "  " + tweetText + "\n"













