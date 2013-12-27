
#user is URL
def getLocation(user):
  # do something with the API
  data = application.get_profile(selectors=['id', 'first-name', 'last-name', {'location':['name']}], member_url=user)
  loc = data[u'location']
  loc2 = loc[u'name']
  loc3 = loc2.split(' ', 1 );
 
  location = {}

  location["country"] = loc3[1] # change
  location["city"] = loc3[0]     # change
#  location["zipcode"] = "" #change
  return location


def getEducation(user):
  # do something with API
  education = ""         # change
  return education

