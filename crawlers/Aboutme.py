from pyquery import PyQuery
import urlparse
from selenium.webdriver.common.keys import Keys


#from models.BingResultsDB import BingResultsDB
#
#STORAGE_FILE = "Bing_results_db.shelve"
#db = BingResultsDB(filename=STORAGE_FILE)

#print len(db._db)

KNOWN_SOCIAL_NETWORKS = ["twitter", "linkedin", "facebook", "wordpress", "blogger", "tumblr"]

class Aboutme:

  def getProfile(self, url):
    doc = self._getDocument(url)
    socialProfilesLinks = []
    username = self._getUsername(url)
    for website in KNOWN_SOCIAL_NETWORKS:
      socialUrlAlias = self._makeSocialLink(username, website)
      if self._socialProfilLinkExists(socialUrlAlias):
        socialProfilesLinks.append({
          "website" : website,
          "url"     : self._getSocialProfileLink(socialUrlAlias),
        })

    return {
      "url"                 : url,                          # about.me url
      "username"            : self._getUsername(url),       # about.me username
      "socialProfilesLinks" : socialProfilesLinks           # social profiles urls
    }

  def _getDocument(self, url):
    PQ = PyQuery(url = url, headers={'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36'})
    return PQ

  def _makeSocialLink(self, username, website):
    assert website in KNOWN_SOCIAL_NETWORKS
    return "http://about.me/content/" + username + "/" + website

  def _getSocialProfileLink(self, url):
    doc = self._getDocument(url)
    anchor = doc(".top_section a")
    return anchor.attr("href")

  def _socialProfilLinkExists(self, url):
    profile = self._getSocialProfileLink(url)
    return profile != None

  def _getUsername(self, profileUrl):
    path = urlparse.urlparse(profileUrl).path
    username = path[1:]
    return username

