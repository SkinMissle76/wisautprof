
from crawlers.Coderwall import Coderwall
from models.CoderwallUserDB import CoderwallUserDB


TEAMS = [
  "london-software-craftsmanship-community-lscc",
  "forward",
  "housetrip",
  "creativatree",
  "box-uk",
  "browser-london",
  "amazon-development-centre-london",
  "springer",
  "alphasights",
  "uk2-group",
  "kainos",
  "factory-media",
  "propeller-communications",
  "hailo",
  "ustwo",
  "7digital",
  "simply-business",
  "reevoo",
  "new-bamboo",
  "living-group",
  "erlang-solutions"
]

def fetchMember(username, team, crawlerInstance):
  c = crawlerInstance
  print "working with username:", username
  print "url:",  c._getMemberProfileUrl(username)
  print "social links", c._getMemberSocialLinks(username)
  print "profile:", c._getMemberProfile(username)
  uObject = {
    "username"       : username,
    "profileUrl"     : c._getMemberProfileUrl(username),
    "profileUrlJson" : c._getMemberProfileUrl(username, "json"),
    "profile"        : c._getMemberProfile(username),
    "socialLinks"    : c._getMemberSocialLinks(username),
    "team"           : team
  }

def fetchAllTeamMembers(db):

  # instanciating an instance of the crawler
  c = Coderwall()
  allTeamMembers = []

  for team in TEAMS:
    print "\n Working with team:", team
    # fetching members of a team
    members = c.findTeamMembers(team)
    print len(members), "member found in this team, let's see who we don't already have..."
    usernames = [c._getMemberUsername(m) for m in members]

    #d =   [c._getMemberSocialLinks(u) for u in usernames]
    for u in usernames:
      if not db.isStored(str(u)):
        uObject = fetchMember(u, team, c)
        allTeamMembers.append(uObject)
        db.storeUser(str(u), uObject)
        print "added", u, "into database"
        print ""

  return allTeamMembers

db = CoderwallUserDB()
a = fetchAllTeamMembers(db)
print "result:", len(a), "members found"
print "all stored in"
