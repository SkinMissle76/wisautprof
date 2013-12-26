
from tables import EMOTIONS_TABLE, POLARITY_TABLE, EDUCATION_TABLE, GENDER_TABLE, LOCATIONS_TABLE, AGE_SYS_TO_REAL, AGE_REAL_TO_SYS
import json

## classifiers
from classifiers.gender import Gender
GENDER_CLASSIFIER = Gender()



class TwitterUser:

  userId = None
  name = None

  def __init__(self, raw, rawStr):
    self.raw = raw
    self.rawStr = rawStr
    self.userId = self._getIdFromData()
    self.name = self._getNameFromData()
    self.location = self._getLocationFromData()
    self.gender = self._getGenderFromData()


  gender = None        # -1, 1
  age = None           # -1..1
  education = None     # 1, 2, 3
  location = None      # 1..47

  def readGender(self):
    if self.gender != None:
      return GENDER_TABLE[self.gender]

  def readAge(self):
    if self.age != None:
      return AGE_SYS_TO_REAL(self.age)

  def readEducation(self):
    if self.education != None:
      return EDUCATION_TABLE[self.education]

  def readLocation(self):
    if self.location != None:
      return LOCATIONS_TABLE[self.location]

  def jsonify(self):
    return json.dumps({
        "userid"    : self.userid,
        "name"      : self.name,
        "gender"    : self.gender,
        "age"       : self.age,
        "education" : self.education,
        "location"  : self.location,
        "rawStr"    : self.rawStr
    })

  ## data getters

  def _getIdFromData(self):
    return self.raw._id

  def _getNameFromData(self):
    return self.raw._name

  def _getGenderFromData(self):
    name = self._getNameFromData()
    return GENDER_CLASSIFIER.getGender(name)

  def _getLocationFromData(self):
    separator = ", "
    city, country = self.raw._location.split(separator)
    return None # TODO this still returns None all the time, com'on!





class Tweet:

  tweetId = None
  content = None
  date = None
  gpsLocation = None


  def __init__(self, tweetId):
    self.tweetId = tweetId

  polarity = None      # -1, 0, 1
  emotion = None       # 1..8
  
  def readEmotion(self):
    if self.emotion != None:
      return EMOTIONS_TABLE[self.emotion]

  def readPolarity(self):
    if self.polarity != None:
      return POLARITY_TABLE[self.polarity]



