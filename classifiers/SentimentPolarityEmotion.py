import cStringIO, pycurl, json, urllib
from lymbix import Lymbix



class SentimentPolarityEmotionClassifier:
  _lymbix = None

  def __init__(self, apikey):
    self._lymbix = Lymbix(apikey)

  def analyse(self, text):
    return _lymbix.tonalize(text)

  def analyseAll(self, textList):
    return _lymbix.tonalize_multiple(textList)

