from models.tables import EDUCATION_TABLE_INVERTED


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

class OkcupidEducation:


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
    return self._stringContainsOnOf(s, HIGH_IND)
  def _inMidEducation(self, s):
    return self._stringContainsOnOf(s, MID_IND)
  def _inLowEducation(self, s):
    return self._stringContainsOnOf(s, LOW_IND)

  def _hasDropped(self, s):
    return self._stringContainsOnOf(s, DROPPED_IND)
  def _isWorkingOn(self, s):
    return self._stringContainsOnOf(s, WORKING_IND)
  def _hasGraduated(self, s):
    return  self._stringContainsOnOf(s, DROPPED_IND)

  # helpers
  def _stringContainsOnOf(self, string, array):
    matches = [ str.lower(e) in str.lower(string) for e in array]
    return any(matches)






test = [
  "High school",
  "graduated from law school",
  "dropped out of law school",
  "Graduated college/university",
  "Working on college/university",
  "Dropped out of space camp",
  "Graduated from masters program"
]

ec = OkcupidEducation()
for s in test:
  print s, ec.getEducationLevelFromString(s)

