#!/bin/python2.7

import unirest
import json

service = "https://loudelement-free-natural-language-processing-service.p.mashape.com/nlp-text/?text="

def getPolarity(text):
 #format text here
 text = ' '.join(text.split())
 text = text.replace(' ', '%20')
 global service
 service = service + text
 print(service)
 response = unirest.get(service,
  headers={
    "X-Mashape-Authorization": "hBe1kBTR8MsdaOYZkoR8pEZPUbECI3RC"
  }
 );
 return response

response = getPolarity("You are awesome")
print(response.body['sentiment-text'])
