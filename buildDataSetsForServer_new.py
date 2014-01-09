import sys, os
from models.testDataBuilder_new import DemographicsTestDataBuilder, SentimentTestDataBuilder


dbtd = DemographicsTestDataBuilder(shelveFilename="final_db_users_aboutme.shelve")
sbtd = SentimentTestDataBuilder(shelveFilename="final_db_tweets.shelve")

dbtd.run()
sbtd.run()



