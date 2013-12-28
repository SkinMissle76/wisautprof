
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