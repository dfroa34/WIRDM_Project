from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import json


"""
import csv
import sys
"""
ckey = 'dspa2PuUl7kNZjjpxmeJeh4WO'
csecret = 'fKJ4zB6pS6bEVZShNKjfUIC6Qk2YjtL20U8qr3goQQuIAPJsEI'
atoken = '27402509-6zlqaqSnr44DgimjhChNHlawxcEiRjJSCrjwdLbFt'
asecret = '9wzHsutuJFota3HFFaFPX8WXT8S0fp13d76BNboV55xu5'

class listener(StreamListener):
    
        def on_data(self,data):
            try:    
                print data                                 
                saveFile = open('output.json','a')
                saveFile.write(data)
                saveFile.write('\n')
                saveFile.close()
            except BaseException, e:
                print 'failed on data',str(e)
                time.sleep(5)

            return True
        
        def on_error (self,status):
            print status
                 
auth = OAuthHandler (ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["zika"], languages=['en'])