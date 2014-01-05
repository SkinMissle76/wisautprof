import cStringIO, pycurl, json

class SentimentPolarityEmotionClassifier:
  _curl = None
  def __init__(self, apikey):
    self._curl = pycurl.Curl()
    self._curl.setopt(self._curl.URL, 'http://api.lymbix.com/tonalize')
    self._curl.setopt(self._curl.HTTPHEADER, ['Accept:application/json', "AUTHENTICATION:" + apikey,"VERSION:2.2"])

  def analyse(self, text):
    response = cStringIO.StringIO()
    self._curl.setopt(self._curl.WRITEFUNCTION, response.write)
    self._curl.setopt(self._curl.POSTFIELDS, "article=" +text+ "&return_fields=[]&reference_id=124312")
    self._curl.perform()
    output = response.getvalue()
    asdictOutput = json.loads(output)
    return asdictOutput

