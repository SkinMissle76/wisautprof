
from crawlers.LinkedinDOM import Linkedin

URLS = [
  "http://www.linkedin.com/pub/hank-mcneil/39/a78/208",
  "http://www.linkedin.com/in/mdilnot",
  "http://uk.linkedin.com/pub/simon-ridgwell/77/9b4/197"
]



lc = Linkedin()           # this guys is the linkedin crawler

profile = lc.getProfile(URLS[0])
print profile

