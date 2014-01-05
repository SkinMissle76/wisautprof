from classifiers.SentimentPolarityEmotion import SentimentPolarityEmotionClassifier
from pprint import pprint

apikey = "8a77503e17148fb5f3d5fd7d1e80ce86c23b6133"
SPEC = SentimentPolarityEmotionClassifier(apikey)
result = SPEC.analyse("I love this movie")

pprint(result)
print result["dominant_emotion"]
print result["article_sentiment"]["sentiment"]

