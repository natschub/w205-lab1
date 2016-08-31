#This script is meant to teach you about the Twitter API

#A lot of this came from the documentation of www.tweepy.org

import tweepy
import json
import pdb

#-------------------Put your keys here------------------
api_key = 'Put your thingy here'
consumer_secret = 'Put your thingy here'

access_token = 'Put your thingy here'
access_token_secret = 'Put your thingy here'

#pdb.set_trace()

auth = tweepy.OAuthHandler(api_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

try:
	trump_user = api.get_user('realDonaldTrump')
except tweepy.TweepError as e:
	print e.message

#pdb.set_trace()
print '\n' + 'Donald Trump\'s last tweet:' + '\n' + trump_user._json['status']['text'] + '\n'
print json.dumps(trump_user._json,sort_keys=True,indent = 4,separators = (',',': '))