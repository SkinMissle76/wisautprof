# -*- encoding: utf-8 -*-
# User Demographics 1.0 sample client for Python
# (c) Daedalus
# Edit the parameters and call "python userdemographicsclient-1.0.py"

import httplib
import urllib
import json

# Variables
host = 'textalytics.com'
api = '/core/userdemographics-1.0.php'
key = '28660aa987aa522ab876a3ef747d1206'

#API request
def sendPost(user, name, description):
  params = urllib.urlencode({'key': key,'user': user, 'name': name, 'desc': description})
  headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
  conn = httplib.HTTPConnection(host)
  conn.request("POST", api, params, headers)
  response = conn.getresponse()
  return response

def getDemographics(user, name, description):
  response_text = sendPost(user, name, description)
  data = response_text.read()
  r = json.loads(data)

  # Show the response
  print "Response"
  print "================="
  print data
  print "\n"

  # Show information
  print "Information about the user: "
  print "==============================="

  info = ''

  try:
    info += 'Type: '
    if r['type'] == 'P':
      info += 'PERSON'
    elif r['type'] == 'O':
      info += 'ORGANIZATION'
    info += "\n"
  except KeyError:
    info += ''

  try:
    info += 'Gender: '
    if r['gender'] == 'M':
      info += 'MALE'
    elif r['gender'] == 'F':
      info += 'FEMALE'
    info += "\n"
  except KeyError:
    info += ''

  try:
    info += 'Age: ' + r['age'] + "\n"
  except KeyError:
    info += ''

  if info != '':
    print info
  else:
    print "Not found"

  print "\n"