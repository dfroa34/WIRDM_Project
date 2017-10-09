import tweepy #https://github.com/tweepy/tweepy
import csv
#Twitter API credentials
consumer_key = "dspa2PuUl7kNZjjpxmeJeh4WO"
consumer_secret = "fKJ4zB6pS6bEVZShNKjfUIC6Qk2YjtL20U8qr3goQQuIAPJsEI"
access_key = "27402509-6zlqaqSnr44DgimjhChNHlawxcEiRjJSCrjwdLbFt"
access_secret = "9wzHsutuJFota3HFFaFPX8WXT8S0fp13d76BNboV55xu5"


def get_all_tweets(screen_name):
	#Twitter only allows access to a users most recent 3240 tweets with this method
	
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	

      
	#initialize a list to hold all the tweepy Tweets
	alltweets = []	
	
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)
	
	#save most recent tweets
	alltweets.extend(new_tweets)
	
	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1
	
	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:
		#print "getting tweets before %s" % (oldest)
		
		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
		
		#save most recent tweets
		
		
		alltweets.extend(new_tweets)
		
		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
		
		#print "...%s tweets downloaded so far" % (len(alltweets))
			      
	#transform the tweepy tweets into a 2D array that will populate the csv	
	outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")]for tweet in alltweets if 'Zika' in tweet.text.encode("utf-8")]
	count1=0
	count2=0
	for tweet in alltweets:
		if 'Zika' in tweet.text.encode("utf-8"):
			count1+=1
	#print "%s tweet/s out of %s contain zika term" %(count1, (len(alltweets)))
	for tweet in alltweets:
		if 'Zika' in tweet.text.encode("utf-8"):
			if 'RT' in tweet.text.encode("utf-8"):
				count2+=1
	print "%s tweet/s out of %s contain zika term and %s of it/them are retweets"  %(count1, (len(alltweets)), count2)

		
  
	#write the csv	
	with open('%s_tweets.csv' % screen_name, 'wb') as f:
		writer = csv.writer(f)
		writer.writerow(["id","created_at","text"])
		writer.writerows(outtweets)

              
	pass


if __name__ == '__main__':
	#pass in the username of the account you want to download
	get_all_tweets("sonar_guy")
 