# usage
# print GetConfig("twitter_config.json").apiKeys


import json

class Get:


  def Twitter(self):
    filename = "apis/twitter_config.json"

    with open(filename) as configFile:    
      config = json.load(configFile)
      return config["api_keys"]

