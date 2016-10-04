from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import json
import csv

"""
import csv
import sys
"""

ckey = 'IhyKiqN6JJgvmeBQeBKiPoCtX'
csecret = 'DPiWDUCymkYxNYBMkwaTkZD85oHDwC23gtOJ2woE0BFaCrJo3Z'
atoken = '2609369460-otRuCCeuDmZxOwug2gJZlhF3PKPNA4tn0msGwH9'
asecret = 'mejOpj5q4mgg03wMOxBTVuZ6ZOjiTuxhBpMGFne1Cj4c0'

class listener(StreamListener):
    def on_data(self, data):
        try:
            all_data = json.loads(data)
            with open("backup.txt", 'a') as backup:
                backup.write(str(all_data) + "\n")
                backup.close()

            text = str(all_data["text"]).encode("utf-8")

        # print "text" + text
            id = str(all_data["id"]).encode("utf-8")

        # print "id" + str(id)
            timestamp = str(all_data["timestamp_ms"]).encode("utf-8")

        # print "stimestamp" + str(timestamp)
            sn = str(all_data["user"]["screen_name"]).encode("utf-8")

        # text = data.split(',"text":"')[1].split('","source')[0]
        # name = data.split(',"screen_name":"')[1].split('","location')[0]
            contentlist = []
            contentlist.append(text)
            contentlist.append(id)
            contentlist.append(timestamp)
            contentlist.append(sn)
            print contentlist
            f = open("tweets3.csv", 'ab')
            wrt = csv.writer(f, dialect='excel')
            try:
                wrt.writerow(contentlist)
            except UnicodeEncodeError, UnicodeEncodeError:
                return True
            return True
        except BaseException, e:

            print 'failed on data',type(e),str(e)
            time.sleep(3)

    def on_error(self, status):
        print "Error status:" + str(status)


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
Stream.userstream()
twitterStream.filter(track=["zika"], languages=['en'])
