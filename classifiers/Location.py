from string import lower
from models.CitiesCountiesDB import CountiesDB


class LinkedinLocation:

  def __init__(self):
    self._cdb = CountiesDB()

  def getCounty(self, locationStr):
    l = self._splitLocationString(locationStr)
    if len(l) == 2:
      city, county = l[0], l[1]
      foundCounty1 = self._cdb.getCityCounty(city)
      foundCounty2 = self._cdb.getCountyByName(county)
    elif len(l) == 1:
      cityOrCounty = l[0]
      foundCounty1 = self._cdb.getCityCounty(cityOrCounty)
      foundCounty2 = self._cdb.getCountyByName(cityOrCounty)
    else:
      return None

    if foundCounty1 is not None:
      return foundCounty1
    elif foundCounty2 is not None :
      return foundCounty2
    else:
      return None



  def _splitLocationString(self, locationStr):
    return filter(lambda i : not self._strAreEqual(i, "United Kingdom"),
                  locationStr.split(", "))

  def _strAreEqual(self, a, b):
    return str.lower(str(a)) == str.lower(str(b))



