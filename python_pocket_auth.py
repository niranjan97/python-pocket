#Python script to add/extract unread items from Pocket (www.getpocket.com)
#TODO
#Hide API, build add-item, build export-item, build OAuth2.0 support, build authentication (POST)
import requests
import urllib2
import json

#Request URLS
request_token_url = "https://getpocket.com/v3/oauth/request"
add_item_url = "https://getpocket.com/v3/add"


consumer_key =  "49533-43f3a761e2d416ead5da76c0" #Consumer key to allow access to API (NEEDS TO BE HIDDEN)
redirect_uri = "pocketapp1234:authorizationFinished" #bullshit redirect_uri to pass through to POST request

#------------------------------------------------#
#              AUTHENTICATION                    #
#------------------------------------------------#

payload_reqtoken = {'consumer_key': consumer_key  ,'redirect_uri': redirect_uri } #payload for POST request for first step of Pocket authentication 
rq_token_1 = requests.post(request_token_url, data=payload, json=None)
request_token = rq_token_1.text
request_token_strip = request_token.replace("code=", "")


#USER AUTHENTICATION
auth_url = "https://getpocket.com/auth/authorize?request_token="+request_token_strip+"&redirect_uri="+redirect_uri #login onto getpocket and authorize application
print(auth_url, "authorize python-pocket using web browser")


#CONVERT REQUEST_TOKEN TO ACCESS_TOKEN
access_token_url = "https://getpocket.com/v3/oauth/authorize"
payload_acctoken = {'consumer_key': consumer_key, 'code': request_token_strip}
access_token = requests.post(access_token_url, data=payload_acctoken)
access_token = access_token.text
access_token = access_token.replace("access_token", "")
user_info = access_token.split("&") #user_info[0] = access token, user_info[1] = username
#Authentication complete! Use access token and consumer key to remove, add or retrieve pocket data. 



