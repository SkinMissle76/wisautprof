
import shelve
import cPickle as pickle
import urlparse

DATA_DIR = "./data/"
FILE_NAME = "coderwall_user_db.shelve"

class CoderwallUserDB:

  _db = None

  def __init__(self, filename = FILE_NAME):
    self._db = shelve.open(DATA_DIR + filename)

  def storeUser(self, username, userObject):
    assert type(username) == str
    self._db[username] = userObject
    
  def isStored(self, username):
    assert type(username) == str
    return self._db.has_key(username) and self.get(username) != None

  def numberOfUsers(self):
    return len(self._db)

  def getAllUsernames(self):
    return self._db.keys()

  def getAllTwitterUsers(self):
    #twitterUsers = [self._hasTwitterProfile(username)for username in self._db.keys()]
    twitterUsers = filter(lambda u : self._hasProfile(u, "twitter"), self.getAllUsernames())
    return twitterUsers

  def getAllLinkedinUsers(self):
    linkedinUsers = filter(lambda u : self._hasProfile(u, "linkedin"), self.getAllUsernames())
    return linkedinUsers

  def getAllGithubUsers(self):
    linkedinUsers = filter(lambda u : self._hasProfile(u, "github"), self.getAllUsernames())
    return linkedinUsers

  def getTwitterUsername(self, coderwallUsername):
    return self._getUsernameOn(coderwallUsername, "twitter")

  def getGithubUsername(self, coderwallUsername):
    return self._getUsernameOn(coderwallUsername, "github")

  def getLinkedinUsername(self, coderwallUsername):
    return self._getUsernameOn(coderwallUsername, "linkedin")





  def getSocialLinks(self, username):
    user = self.get(username)
    socialLinks = filter(lambda l : l != None, user["socialLinks"])
    return socialLinks

  def get(self, username):
    assert type(username) == str
    user = self._db[username]
    return user

  # private
  def urlToUsername(self, link, website):
    assert website in ["twitter", "github", "linkedin"] # TODO refactor this with KNOwN_SOCIAL_NETWOKS
    if website == "twitter":
      path = urlparse.urlparse(link).path # gives "/username"
      username = path[1:] # give "username"
      return username
    elif website == "github":
      raise NotImplementedError
    elif website == "linkedin":
      raise NotImplementedError
    else:
      raise ValueError("Invalid website " + website)

  def _hasProfile(self, username, website):
    matches = self._getSocialNetworkProfile(username, website)
    return len(matches) == 1

  def _hasTwitterProfile(self, username):
    matches = self._getSocialNetworkProfile(username, "twitter")
    return len(matches) == 1

  def _getSocialNetworkProfile(self, username, website):
    assert website in ["twitter", "github", "linkedin"] # TODO refactor this with KNOwN_SOCIAL_NETWOKS

    sl = self.getSocialLinks(username)
    matches = filter(lambda l : l["website"] == website, sl)
    assert len(matches) <= 1 # there shouldn't be more than one

    return matches

  def _getUsernameOn(self, coderwallUsername, website):
    p = self._getSocialNetworkProfile(coderwallUsername, website)
    if len(p) > 0:
      return self.urlToUsername(p[0]["link"], website)
    else:
      return None


