
from crawlers.LinkedinDOM import Linkedin

URLS = [
  "http://www.linkedin.com/in/mdilnot",
  "http://uk.linkedin.com/pub/simon-ridgwell/77/9b4/197"
]



#user comes as URL
def getUserEducation(user):
	lc = Linkedin()           # this guys is the linkedin crawler
	educations = []
	profile = lc.getProfile(user)
	pr1 = profile["education"]
	for ed in pr1:
		educations.append(ed["school"])
	return educations

#user comes as URL. Returns True if the user is from UK, and False if not	
def isUserFromUK(user):
	lc = Linkedin()           # this guys is the linkedin crawler
	profile = lc.getProfile(URLS[0])
	pr1 = profile["locality"]
	list = pr1.split(",", 1)
	if list[1] == ' United Kingdom':
		return True
	else:
		return False