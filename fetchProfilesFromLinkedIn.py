
from crawlers.LinkedinDOM import Linkedin

URLS = [
  "http://www.linkedin.com/in/mdilnot",
  "http://uk.linkedin.com/pub/simon-ridgwell/77/9b4/197"
]



lc = Linkedin()           # this guys is the linkedin crawler


profiles = []
for url in URLS:
  profile = lc.getProfile(url)
  profiles.append(profile)

print [p["fullName"] for p in profiles]
