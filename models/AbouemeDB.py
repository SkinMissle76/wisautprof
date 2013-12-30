
import shelve
import cPickle as pickle
import urlparse

DATA_DIR = "./data/"
FILE_NAME = "aboutme_profiles_db.shelve"

class AboutmeDB:

  _db = None

  def __init__(self, filename = FILE_NAME):
    self._db = shelve.open(DATA_DIR + filename)

  def add(self, username, linkObject):
    assert type(username) == str
    self._db[username] = linkObject

  def has(self, username):
    assert type(username) == str
    return self._db.has_key(username) and self.get(username) != None

  def get(self, username):
    assert type(username) == str
    return self._db[username]

  def getSocialProfile(self, username, website):
    profile = self.get(username)
    socialProfiles = profile["socialProfilesLinks"]
    wantedSocialProfile = filter(lambda sp : sp["website"] == website, socialProfiles)
    return wantedSocialProfile

  def hasSocialProfile(self, username, website):
    socialProfile = self.getSocialProfile(username, website)
    if len(socialProfile) > 0:
      url = socialProfile[0]["url"]
      return len(url) > 0
    else:
      return False

  def hasTwitterProfile(self, username):
    return self.hasSocialProfile(username, "twitter")

  def hasLinkedinProfile(self, username):
    return self.hasSocialProfile(username, "linkedin")

  def getAllUsersWithTwitterAndLinkedinProfiles(self):
    f = lambda u : self.hasLinkedinProfile(u) and self.hasTwitterProfile(u)
    return filter(f, self._db.keys())








