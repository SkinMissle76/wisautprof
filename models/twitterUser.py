
from tables import EMOTIONS_TABLE, POLARITY_TABLE, EDUCATION_TABLE, GENDER_TABLE, LOCATIONS_TABLE, AGE_SYS_TO_REAL, AGE_REAL_TO_SYS 
import json


class TwitterUser:

  userId = None
  fullName = None

  def __init__(self, userId, fullName):
    self.userId = userId
    self.fullName = fullName


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
        "gender"    : self.gender,
        "age"       : self.age,
        "education" : self.education,
        "location"  : self.location
    })


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



