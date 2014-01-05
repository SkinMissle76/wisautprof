

import requests, json
import cStringIO

#url =
#-H "AUTHENTICATION:8a77503e17148fb5f3d5fd7d1e80ce86c23b6133" \
#-H "ACCEPT:application/json" \
#-H "VERSION:2.2" \
#http://api.lymbix.com/tonalize \
#-d "article=He was happy and surprised instead of being an angry guy. \
#            Although he wasn't too happy about it he said yes anyways! \
#            What do you think of this decision? \
#    &return_fields=[] \
#    &reference_id=1243122"


import pycurl
from pprint import pprint



class SentimentPolarityEmotionClassifier:
  _curl = None
  def __init__(self, apikey):
    self._curl = pycurl.Curl()
    self._curl.setopt(self._curl.URL, 'http://api.lymbix.com/tonalize')
    self._curl.setopt(self._curl.HTTPHEADER, ['Accept:application/json', "AUTHENTICATION:8a77503e17148fb5f3d5fd7d1e80ce86c23b6133","VERSION:2.2"])

  def analyse(self, text):
    response = cStringIO.StringIO()
    self._curl.setopt(self._curl.WRITEFUNCTION, response.write)
    self._curl.setopt(self._curl.POSTFIELDS, "article=" +text+ "&return_fields=[]&reference_id=124312")
    self._curl.perform()
    output = response.getvalue()
    asdictOutput = json.loads(output)
    return asdictOutput




