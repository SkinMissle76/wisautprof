import json
from models.tables import EMOTIONS_TABLE


AFFECTION_FRIENDLINES ="affection_friendliness"
ENJOYMENT_ELATION =  "enjoyment_elation"
AMUSEMENT_EXCITEMENT =  "amusement_excitement"
CONTENTMENT_GRATITUDE =  "contentment_gratitude"
HUMILIATION_SHAME =  "humiliation_shame"
FEAR_UNEASINESS =  "fear_uneasiness"
ANGER_LOATHING =  "anger_loathing"
SADNESS_GRIEF =  "sadness_grief"
NEUTRAL =  "Neutral"

class SentimentPolarityEmotionClassifier:

  EMOTIONS = [
    AFFECTION_FRIENDLINES,
    ENJOYMENT_ELATION,
    AMUSEMENT_EXCITEMENT,
    CONTENTMENT_GRATITUDE,
    HUMILIATION_SHAME,
    FEAR_UNEASINESS,
    ANGER_LOATHING,
    SADNESS_GRIEF,
  ]
  BASIC_EMOTIONS = {
    "neutral" : [NEUTRAL],
    "joy" : [ENJOYMENT_ELATION],
    "sadness" : [SADNESS_GRIEF],
    "anger" : [ANGER_LOATHING],
    "fear" : [FEAR_UNEASINESS],
    "surprise" : [AMUSEMENT_EXCITEMENT],
    "trust" : [CONTENTMENT_GRATITUDE, AFFECTION_FRIENDLINES],
    "disgust" : [ANGER_LOATHING, HUMILIATION_SHAME],
    "anticipation" : [ENJOYMENT_ELATION, FEAR_UNEASINESS, AMUSEMENT_EXCITEMENT]
  }

  def _matchToBasicEmotion(self, emotionArray, dominantEmotion):
    if len(emotionArray) == 2:
      if self._mathBothEmotionsWith(emotionArray[0], emotionArray[1], "anticipation"):
        return self._mathBothEmotionsWith(emotionArray[0], emotionArray[1], "anticipation")
      if self._mathBothEmotionsWith(emotionArray[0], emotionArray[1], "trust"):
        return self._mathBothEmotionsWith(emotionArray[0], emotionArray[1], "trust")
      if self._mathBothEmotionsWith(emotionArray[0], emotionArray[1], "disgust"):
        return self._mathBothEmotionsWith(emotionArray[0], emotionArray[1], "disgust")

    if self._matchEmotionWith(dominantEmotion, "joy"):
      return self._matchEmotionWith(dominantEmotion, "joy")
    if self._matchEmotionWith(dominantEmotion, "surprise"):
      return self._matchEmotionWith(dominantEmotion, "surprise")
    if self._matchEmotionWith(dominantEmotion, "fear") :
      return self._matchEmotionWith(dominantEmotion, "fear")
    if self._matchEmotionWith(dominantEmotion, "disgust") :
      return self._matchEmotionWith(dominantEmotion, "disgust")
    if self._matchEmotionWith(dominantEmotion, "trust"):
      return self._matchEmotionWith(dominantEmotion, "trust")
    if self._matchEmotionWith(dominantEmotion, "anger"):
      return self._matchEmotionWith(dominantEmotion, "anger")
    if self._matchEmotionWith(dominantEmotion, "sadness"):
      return self._matchEmotionWith(dominantEmotion, "sadness")
    if self._matchEmotionWith(dominantEmotion, "neutral"):
      return self._matchEmotionWith(dominantEmotion, "neutral")

  def _matchEmotionWith(self, emotion, basicEmotion):
    if emotion["emotion"] in self.BASIC_EMOTIONS[basicEmotion]:
      return basicEmotion
    else:
      return None


  def _mathBothEmotionsWith(self, emotion1, emotion2, basicEmotion):
    if emotion1["emotion"] in self.BASIC_EMOTIONS[basicEmotion] \
      and emotion2["emotion"] in self.BASIC_EMOTIONS[basicEmotion]:
      return basicEmotion
    else:
      return None

  def _areCouplable(self, emotionsArray):
    for be, emotions in self.BASIC_EMOTIONS.iteritems():
      if emotionsArray[0] in emotions and emotionsArray[1]:
        return True
    return False

  def _getAllEmotions(self, lo):
    emotions = {}
    for e in self.EMOTIONS:
      emotions[e] = {"emotion": e, "rating" : lo[e]}
    return emotions

  def _getTwoMostDominantEmotions(self, lo):
    emotions = self._getAllEmotions(lo)
    sortedEmotions = sorted(emotions.values(), key = lambda e : e["rating"], reverse=True)
    firstDominantEmotion = sortedEmotions[0]
    secondDominantEmotion = sortedEmotions[1]
    return [firstDominantEmotion, secondDominantEmotion]

  #def _needToBeMixed(self, emotion1, emotion2):
  #  diff = (emotion1[1] - emotion2[1]) / 10.0
  #  return diff < 3/10.0

  def getRelevantEmotions(self, lo):
    domEmotions = self._getTwoMostDominantEmotions(lo)

  def _getDominantEmotion(self, lo):
    return {
      "emotion" : lo["dominant_emotion"],
      "rating"  : 0
    }


  def getEmotion(self, lo):
    domEmotions = self._getTwoMostDominantEmotions(lo)
    domEmotion = self._getDominantEmotion(lo)
    basicEmotion = self._matchToBasicEmotion(domEmotions, domEmotion)
    return self._getBasicEmotionId(basicEmotion)

  def getPolarity(self, lo):
    polarity = lo["article_sentiment"]["sentiment"]
    if polarity == "Positive":
      return 1
    elif polarity == "Negative":
      return -1
    else:
      return 0

  def _getBasicEmotionId(self, basicEmotion):
    for i, be in EMOTIONS_TABLE.iteritems():
      if str.lower(be) == basicEmotion:
        return i






#lo = json.loads('{'
#                '"anger_loathing": 3.0, '
#                '"enjoyment_elation": 1.34, '
#                '"amusement_excitement": 10.0, '
#                '"contentment_gratitude": 7.22, '
#                '"humiliation_shame": 0.0, "average_intensity": 2.1, '
#                '"fear_uneasiness": 1.0, "ignored_terms": ["But"], '
#                '"affection_friendliness": 2.1, "intense_sentence": {"dominant_emotion": "affection_friendliness", "intensity": 10.0, "sentence": "@ duffman7306 But still smiling ."}, "coverage": 3.0, '
#                '"sadness_grief": 10.0, "article": " @ duffman7306 But still smiling .  .  . ", "clarity": 50.0, "article_sentiment": {"score": 5.0, "sentiment": "Negative"}, "dominant_emotion": "Neutral"}')
#spec = SentimentPolarityEmotionClassifier()
#emotions = spec._getTwoMostDominantEmotions(lo)
#domEmotion = spec._getDominantEmotion(lo)
#print emotions
#print domEmotion
#print spec._areCouplable(emotions)
#print spec._matchToBasicEmotion(emotions, domEmotion)
#print spec.getEmotion(lo)
#print spec.getPolarity(lo)





