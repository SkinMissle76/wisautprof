
from BeautifulSoup import BeautifulSoup
import urllib2, re



class Coderwall:




  def _makeTeamUrl(self, teamName):
    # https://coderwall.com/team/london-software-craftsmanship-community-lscc
    return "https://coderwall.com/team/" + teamName

  def findTeamMembers(self, name):
    url = self._makeTeamUrl(name)
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page)

    reg = re.compile(r"\bmember\b")

    return soup.findAll("li", {"class" : reg})

  def _getMemberName(self, member):
    return member.find("h3").getText()

  def _getMemberSocialLinks(self, username):
    url = self._getMemberProfileUrl(username)
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page)

    socialLinksContainer =  soup.find("ul", {"class" : "social-links"})

    anchors = socialLinksContainer.findAll("a")
    return [self._makeSocialLinkFromAnchor(a) for a in anchors]

  def _makeSocialLinkFromAnchor(self, anchor):
    url = anchor["href"]
    classes = anchor["class"]
    knownSocialNetworks = ["twitter", "github", "linkedin"]
    matches = filter(lambda l : l in classes, knownSocialNetworks)
    assert len(matches) <= 1

    if len(matches) == 0:
      return None
    else:
      return {
        "link"    : url,
        "website" : matches[0]
      }

  def _getMemberProfileUrl(self, username, dataformat=None):
    url  = "https://coderwall.com/" + username
    if dataformat == "json":
      url += ".json"
    elif dataformat == None:
      pass
    else:
      raise ValueError("Unknown type of format")

    return url


  def _getMemberUsername(self, member):
    usernameAnchors =  member.findAll("a", {"data-target-type" : "team-member profile"})
    if len(usernameAnchors) > 0:
      username = usernameAnchors[0]["href"]
      cleanUsername = username[1:]
      return cleanUsername
    else:
      return None


  def _getMemberProfile(self, member):
    url = self._getMemberProfileUrl(members)
    json = urllib2.urlopen(url)
    return json






c = Coderwall()
members = c.findTeamMembers("london-software-craftsmanship-community-lscc")
print len(members), "member found"
usernames = [c._getMemberUsername(m) for m in members]
print usernames
#d =   [c._getMemberSocialLinks(u) for u in usernames]


