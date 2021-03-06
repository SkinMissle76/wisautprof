from classifiers.SentimentPolarityEmotion import SentimentPolarityEmotionClassifier
from pprint import pprint

from lymbix import Lymbix
apikey = "8a77503e17148fb5f3d5fd7d1e80ce86c23b6133"
# a few other api keys you use if this one has reached its limit
#apikey = "06bb0ef22cc21896451d7d9ed0f53eff6c99cd93"
#apikey = "1321dd7e3e05237514db9ae7812202c23f6b2f5e"

#SPEC = SentimentPolarityEmotionClassifier(apikey)
#result = SPEC.analyse("I love this movie")
#results = SPEC.analyseAll(["I love this movie", "I hate this movie"])

#pprint(results)
#print result["dominant_emotion"]
#print result["article_sentiment"]["sentiment"]

l = Lymbix(apikey)
r = l.tonalize_multiple(["I love you", "I hate you"])
print [i["article_sentiment"] for i in r]
