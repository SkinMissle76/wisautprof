# coding=utf-8
from crawlers.Coderwall import Coderwall
from models.CoderwallUserDB import CoderwallUserDB

OVERWRITE_DB = False

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
  "erlang-solutions",
  "hachette-uk",
  "interkonect-services-uk-limited",
  "central-media-uk",
  "orange-labs-uk",
  "kainos-recuitment",
  "eutechnyx",
  "pyrocms",
  "hurstdev",
  "mamas-papas",
  "commerce-guys",
  "nimbleworks",
  "wiredmedia",
  "total-synergy",
  "gylphi",
  "tamarou",
  "clock",
  "unep-wcmc",
  "buddycloud",
  "jobandtalent",
  "esendex",
  "3squared",
  "overheard",
  "carwow",
  "etch",
  "the-league-of-extraordinary-developers",
  "datasift",
  "thap-ltd",
  "madebyawesome",
  "open-source-agility",
  "urban-appetite",
  "neutral-tone",
  "social-genius",
  "creative-aura",
  "wildfire-interactive-inc",
  "tdm-oss-services"
]

def getTeamsNames():
  teams = list(set(TEAMS)) # removing duplicates
  return teams

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
  return uObject

def fetchAllTeamMembers(db):

  # instanciating an instance of the crawler
  c = Coderwall()
  allTeamMembers = []

  numberOfProcessedTeams = 0
  numberOfTeams = len(getTeamsNames())

  for team in getTeamsNames():
    numberOfProcessedTeams += 1
    print "\n Working with team:", team, "("+ str(numberOfProcessedTeams) + "/" + str(numberOfTeams) +")"
    # fetching members of a team
    members = c.findTeamMembers(team)
    print len(members), "member found in this team, let's see who we don't already have..."
    usernames = [c._getMemberUsername(m) for m in members]

    #d =   [c._getMemberSocialLinks(u) for u in usernames]
    for u in usernames:
      if not db.isStored(str(u)) or OVERWRITE_DB:
        uObject = fetchMember(u, team, c)
        allTeamMembers.append(uObject)
        assert(uObject != None)
        db.storeUser(str(u), uObject)
        print "added", u, "into database"
        print ""

  return allTeamMembers

db = CoderwallUserDB()
a = fetchAllTeamMembers(db)
print "result:", len(a), "members found"
print "all stored in"
