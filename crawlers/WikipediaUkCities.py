from models.tables import LOCATIONS_TABLE_INVERTED, LOCATIONS_TABLE
from pyquery import PyQuery


class WikipediaUKCities:


  def __init__(self):
    self._url = "http://en.wikipedia.org/wiki/List_of_towns_in_England"
    self._doc = self._getDocument(self._url)
    self._rows = self._getRows(self._doc)

  def _getDocument(self, url):
    PQ = PyQuery(url = url, headers={'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36'})
    return PQ

  def getCities(self):
    return map(self._getCity, self._rows)

  def getCounties(self):
    cities = self.getCities()
    counties = {}
    for countyId in LOCATIONS_TABLE_INVERTED.values():
      county = self._getCounty(countyId, cities)
      counties[countyId] = county
    return counties

  def _getRows(self, doc):
    citiesDOM = doc(".wikitable tr")
    t = PyQuery(citiesDOM).find("td")
    groupsCols = [(t[i], t[i+1], t[i+2])
                    for i in range(0, len(t), 3)]
    return groupsCols

  def _getCityName(self, row):
    #return PyQuery(row).find("a").text()
    return PyQuery(row[0]).text()

  def _getCountyName(self, row):
    return PyQuery(row[1]).text()

  def _getCity(self, row):
    city   = self._getCityName(row)
    county = self._getCountyName(row)

    countyNumber = self._getCountyId(county)

    return {
      "city"     : city,
      "county"   : county,
      "countyId" : countyNumber
    }

  def _getCountyId(self, countyName):
    if LOCATIONS_TABLE_INVERTED.has_key(countyName):
      return LOCATIONS_TABLE_INVERTED[countyName]
    else:
      raise ValueError("Unfound county")

  def _getCounty(self, countyId, cities):
    countyCities = filter(lambda c : c["countyId"] == countyId,
           cities)
    return {
      "countyId" : countyId,
      "county"   : LOCATIONS_TABLE[countyId],
      "cities"   : countyCities
    }


wc = WikipediaUKCities()












