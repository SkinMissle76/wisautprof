#!/bin/python2.7

import unirest
import json

service = "http://text-processing.com/api/sentiment/"

def getPolarity(text):
 global service
 response = unirest.post(service, headers={"Accept": "application/json"},
  params={
   "text": text
  }
 )
 return response
 
response = getPolarity("You are awesome")
print(response.body['label'])
