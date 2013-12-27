# -*- coding: utf-8 -*-
import urllib
import urllib2
import json

class Bing:


  def __init__(self, apiKeys):
    self.top = 50             # max nb of results to return (must be <= 50)
    self.apiKeys = apiKeys


  def _searchFromSkipToTop(self, query, skip):
    result = self._bingSearch(query, "Web", skip, self.top)
    return result

  def search(self, query, startPage, nbOfPages):
    skip = startPage*self.top

    results = []
    for page in range(0, nbOfPages):
      result = self._searchFromSkipToTop(query, skip)
      results.extend(result)
    return results

  def _bingSearch(self, query, search_type, skip, top):
    #search_type: Web, Image, News, Video
    key = self.apiKeys[0]
    query = urllib.quote(query)
    # create credential for authentication
    user_agent = 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)'
    credentials = (':%s' % key).encode('base64')[:-1]
    auth = 'Basic %s' % credentials
    url = 'https://api.datamarket.azure.com/Data.ashx/Bing/Search/'+search_type+'?Query=%27'+query+'%27&$skip='+str(skip)+'&$top='+ str(top) +'&$format=json'
    request = urllib2.Request(url)
    request.add_header('Authorization', auth)
    request.add_header('User-Agent', user_agent)
    request_opener = urllib2.build_opener()
    response = request_opener.open(request)
    response_data = response.read()
    json_result = json.loads(response_data)
    result_list = json_result['d']['results']
    return result_list
