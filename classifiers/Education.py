from models.tables import EDUCATION_TABLE_INVERTED



class OkcupidEducation:
  HIGH_IND = [
    "two-year college",
    "college/university",
    "masters program",
    "law school",
    "med school",
    "Ph.D program"
  ]
  MID_IND = ["high school" ]
  LOW_IND = ["space camp"  ]

  GRADUATED_IND = ["Graduated from"]
  WORKING_IND   = ["Working on"    ]
  DROPPED_IND   = ["Dropped out of"]


  def getEducationLevelFromString(self, s):

    if self._hasDropped(s):
      if self._inHighEducation(s):
        return EDUCATION_TABLE_INVERTED["Mid"]
      elif self._inMidEducation(s):
        return EDUCATION_TABLE_INVERTED["Low"]
      elif self._inLowEducation(s):
        return EDUCATION_TABLE_INVERTED["Low"]
      else:
        return None
    #elif self._hasGraduated(s) or self._isWorkingOn(s):
    else:
      if self._inHighEducation(s):
        return EDUCATION_TABLE_INVERTED["High"]
      elif self._inMidEducation(s):
        return EDUCATION_TABLE_INVERTED["Mid"]
      elif self._inLowEducation(s):
        return EDUCATION_TABLE_INVERTED["Low"]
      else:
        return None

  # private
  def _inHighEducation(self, s):
    return self._stringContainsOnOf(s, self.HIGH_IND)
  def _inMidEducation(self, s):
    return self._stringContainsOnOf(s, self.MID_IND)
  def _inLowEducation(self, s):
    return self._stringContainsOnOf(s, self.LOW_IND)

  def _hasDropped(self, s):
    return self._stringContainsOnOf(s, self.DROPPED_IND)
  def _isWorkingOn(self, s):
    return self._stringContainsOnOf(s, self.WORKING_IND)
  def _hasGraduated(self, s):
    return  self._stringContainsOnOf(s,self.DROPPED_IND)

  # helpers
  def _stringContainsOnOf(self, string, array):
    matches = [ str.lower(e) in str.lower(string) for e in array]
    return any(matches)


class LinkedinEducation:


  HIGH_IND = [
    "university", "politec", "polytech", "Institute", "academy", 'U. of ',
    "business", "management", "marketing", "Univers", "science", "economics", "political", "Glamorgan IHE"
  ]

  MID_IND = [
    "high school", "high", "Grammar", "boys", "girls", "college"
  ]

  LOW_IND = [
    "elementary"
  ]


  def getEducation(self, schoolNameList):
    if len(schoolNameList) > 0:
      levels = [self._getLevel(s) for s in schoolNameList]
      return max(levels)
    else:
      return EDUCATION_TABLE_INVERTED["Mid"]

  def filterHigh(self, schoolList):
    return filter(lambda x : self._getLevel(x["school"]) >= 3,
                  schoolList)
  def filterMid(self, schoolList):
    return filter(lambda x : self._getLevel(x["school"]) < 3,
                  schoolList)

  def _getLevel(self, schoolName):
    if self._isHigh(schoolName):
      return EDUCATION_TABLE_INVERTED["High"]
    elif self._isMid(schoolName):
      return EDUCATION_TABLE_INVERTED["Mid"]
    else:
      return EDUCATION_TABLE_INVERTED["Low"]

  def _isHigh(self, schoolName):
    return self._stringContainsOnOf(schoolName, self.HIGH_IND)

  def _isMid(self, schoolName):
    return self._stringContainsOnOf(schoolName, self.MID_IND)

  def _isLow(self, schoolName):
    return self._stringContainsOnOf(schoolName, self.LOW_IND)

  def _stringContainsOnOf(self, string, array):

    s = str.lower(str(
      string.encode("ascii", "ignore")
    ))
    matches = [ str.lower(str(e)) in s for e in array]
    return any(matches)
