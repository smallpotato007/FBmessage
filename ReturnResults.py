#!D:/usr/Python27/python.exe -u 
# coding: utf-8
import urllib 
import urlparse
import subprocess
import facebook
import time
import json
import cgi
import cgitb; cgitb.enable()
# get the info from the html form
form = cgi.FieldStorage()
# get 
#file = urllib.urlopen("https://graph.facebook.com/{'userid'}/statuses?access_token={'access_token'}")
#{
"""the json return from 

data: [
    {
      "id": "2022626523940", 
      "from": {
        "name": "name", 
        "id": "userid"
      }, 
      "message": "messgae", 
      "updated_time": "2011-08-26T16:19:50+0000"
    }, 
   ......
"""

# Parameters of your app and the id of the profile you want to mess with.
FACEBOOK_APP_ID     =  "your app id"
FACEBOOK_APP_SECRET = "appsecret"
FACEBOOK_PROFILE_ID = {'profileid'}
SearchDate=form['searchstr'].value

oauth_args = dict(client_id     = FACEBOOK_APP_ID,
                  client_secret = FACEBOOK_APP_SECRET,
                  grant_type    = 'client_credentials')
oauth_curl_cmd = ['curl',
                  'https://graph.facebook.com/oauth/access_token?' + urllib.urlencode(oauth_args)]
oauth_response = subprocess.Popen(oauth_curl_cmd,
                                  stdout = subprocess.PIPE,
                                  stderr = subprocess.PIPE).communicate()[0]

try:
    oauth_access_token = urlparse.parse_qs(str(oauth_response))['access_token'][0]
except KeyError:
    print('Unable to grab an access token!')
    exit()

facebook_graph = facebook.GraphAPI(oauth_access_token)


# Try to get message from API.
try:
    fb_response=urllib.urlopen("https://graph.facebook.com/{'userid'}/statuses?access_token={oauth_access_token}&limit=50")
    messages=json.read(fb_response)
    for message in messages:
        t1 = time.strptime(SearchDate, "%Y%m%d")
        t2 = time.strptime(message["updated_time"], "%Y%m%d")
        if t2 < t1 :
            print message["message"]+'<br/>'
            print message["updated_time"]+'<br/>'
        
except facebook.GraphAPIError as e:
    print 'can not get message from facebook:', e.type, e.message
