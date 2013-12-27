from BeautifulSoup import BeautifulSoup
import urllib2, re


class Coderwall:


  KNOWN_SOCIAL_NETWORKS = ["twitter", "github", "linkedin"]


  def _makeTeamUrl(self, teamName):
    # https://coderwall.com/team/london-software-craftsmanship-community-lscc
    return "https://coderwall.com/team/" + urllib2.quote(teamName)

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
    matches = filter(lambda l : l in classes, self.KNOWN_SOCIAL_NETWORKS)

    assert len(matches) <= 1  # we should find *at most* one social network per anchor

    if len(matches) == 0:
      return None
    else:
      return {
        "link"    : url,
        "website" : matches[0]
      }

  def _getMemberProfileUrl(self, username, dataformat=None):
    url  = "https://coderwall.com/" + urllib2.quote(username)
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


  def _getMemberProfile(self, username):
    url = self._getMemberProfileUrl(username, dataformat="json")
    response = urllib2.urlopen(url)
    json = response.read()
    return json

