from classifiers.Education import LinkedinEducation
from pyquery import PyQuery as PQ

CURRENT_YEAR = 2013

class LinkedinAge:

  _lec = LinkedinEducation()



  def getAge(self, education, blogUrl):
    yearOfStartOfUniversity = self._getYearOfStartOfUniversity(education)
    yearOfEndOfSchool = self._getYearOfEndOfSchool(education)
    if yearOfStartOfUniversity is not None:
      return 18 + (CURRENT_YEAR - yearOfStartOfUniversity)
    elif yearOfEndOfSchool is not None:
      return 18 + (CURRENT_YEAR - yearOfEndOfSchool)
    elif blogUrl is not None:
      return self._askAgeAnalyser(blogUrl)
    else:
      return None

  def _getYearFromLinkedinDate(self, s):
    if s is not None:
      return int(s.split("-")[0])
    else:
      return None

  def _getHigh(self, education):
    return self._lec.filterHigh(education)

  def _getMid(self, education):
    return self._lec.filterMid(education)

  def _getStartPeriods(self, education):
    return [e["period"]["start"] for e in education]

  def _getEndPeriods(self, education):
    return [e["period"]["end"] for e in education]

  def _getYearOfStartOfUniversity(self, education):
    highedu = self._getHigh(education)
    starts = self._getStartPeriods(highedu)
    startsYears = [self._getYearFromLinkedinDate(s) for s in starts if s is not None]
    #s = min(startsYears)
    if len(startsYears) > 0:
      return min(startsYears)
    else:
      return None

  def _getYearOfEndOfSchool(self, education):
    midedu = self._getMid(education)
    ends = self._getEndPeriods(midedu)
    endYears = [self._getYearFromLinkedinDate(s) for s in ends if s is not None]
    #s = min(endYears)
    if len(endYears) > 0:
      return min(endYears)
    else:
      return None

  def _askAgeAnalyser(self, blogUrl):
    url = "http://www.ageanalyzer.com/?url=" + blogUrl
    dom = PQ(url=url)
    ageRaw =  dom("#verdict").find("strong").text()
    return self._processAgeAnalyserFormat(ageRaw)


  def _processAgeAnalyserFormat(self, ageRaw):
    boundaries = ageRaw.split("-")
    if len(boundaries) == 2:
      return (int(boundaries[0]) + int(boundaries[1]))/2
    else:
      return None


