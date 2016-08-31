#This script is meant to teach you about the Twitter API

#A lot of this came from the documentation of www.tweepy.org

import tweepy
import json
import pdb

api_key = 'IKxHibKntB9bctmLnGaPQlNyK'
consumer_secret = 'df5xLIWupfVs3LHPLDmM8vEe05TR5kIDARdr4yiqLpda1dyzxp'

access_token = '2903033000-Q7oHGwPiEyXD9JFRJcA5N9i28XgBzm0P2XtZdfE'
access_token_secret = 'NcjDOU1kIgHHlSrCjxuTc0uaYkv1RjBD42l3M2IuBpQYi'

#pdb.set_trace()

auth = tweepy.OAuthHandler(api_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

try:
	trump_user = api.get_user('realDonaldTrump')
except tweepy.TweepError as e:
	print e.message

#pdb.set_trace()
#print '\n' + 'Donald Trump\'s last tweet:' + '\n' + trump_user._json['status']['text'] + '\n'
print json.dumps(trump_user._json,sort_keys=True,indent = 4,separators = (',',': '))