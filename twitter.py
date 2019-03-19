import tweepy
#import twitter
import json
#import MySQLdb
import subprocess
import time
from datetime import datetime
import os, sys
import json, urllib,argparse, hashlib, re, sys
#from dateutil import parser

WORDS = ['HPE']

'''
CONSUMER_KEY = "Ty1DiKzWfvhZHrihtn1PXsDcV"
CONSUMER_SECRET = "3qDUsAeQWzuaaRV0pVg05zxiBgPvrlzjAuo1Zgyfncidc6GcJl"
ACCESS_TOKEN = "760730091362119681-lDMTTDXTAQL6rmDUWLnrYmrT0rpV37P"
ACCESS_TOKEN_SECRET = "4Gi0hYQh3lfDHfTILCbL4lkMc4edbk2dIJwzYmITe675v"'''
'''
#
ACCESS_TOKEN = "3315378631-FnAFbhIH2NqrnJlZ1CaRQyM2U6RL4gs9YRaIr2g"
ACCESS_TOKEN_SECRET = "R4acjruLQhbhqmgbv0sEeE2OeEGyeUSvpCuKDC0zQQdh8"
CONSUMER_KEY = "LsPnChxK4jL9RJ7YE0zHJLsWB"
CONSUMER_SECRET = "K8A8DhjUwXovauJfNSOgaDW5811SvSfU64afGXcYpH6YjS3LEz"
'''
#My CREDENTIALS
ACCESS_TOKEN = "<get credentials"  #see above to understand format
ACCESS_TOKEN_SECRET = "get credentials"
CONSUMER_KEY = "get credentials"
CONSUMER_SECRET = "get credentials"



class StreamListener(tweepy.StreamListener):

    def on_connect(self):
        print("We are now connected to the streaming API.")

    def on_error(self, status_code):
        print('An Error has occured: ' + repr(status_code))
        return False

    def on_data(self, data):
        try:
            datajson = json.loads(data)
            print(datajson['text'])
            a=datajson['extended_tweet']
            print(a['full_text'])
  #          import pdb;pdb.set_trace()

        except Exception as e:
                print(e)

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
listener = StreamListener(api=tweepy.API(wait_on_rate_limit=True))
streamer = tweepy.Stream(auth=auth, listener=listener)
print("Tracking: " + str(WORDS))
streamer.filter(track=WORDS)
