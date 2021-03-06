import tweepy  # https://github.com/tweepy/tweepy
import csv

# Twitter API credentials
consumer_key = "IhyKiqN6JJgvmeBQeBKiPoCtX"
consumer_secret = "DPiWDUCymkYxNYBMkwaTkZD85oHDwC23gtOJ2woE0BFaCrJo3Z"
access_key = "2609369460-otRuCCeuDmZxOwug2gJZlhF3PKPNA4tn0msGwH9"
access_secret = "mejOpj5q4mgg03wMOxBTVuZ6ZOjiTuxhBpMGFne1Cj4c0"

# authorize twitter, initialize tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)


def get_all_tweets(screen_name):
    # Twitter only allows access to a users most recent 3240 tweets with this method

    # initialize a list to hold all the tweepy Tweets
    alltweets = []

    # make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name=screen_name, count=200)

    # save most recent tweets
    alltweets.extend(new_tweets)

    # save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    # keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        # print "getting tweets before %s" % (oldest)

        # all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest)

        # save most recent tweets


        alltweets.extend(new_tweets)

        # update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

    # print "...%s tweets downloaded so far" % (len(alltweets))

    # transform the tweepy tweets into a 2D array that will populate the csv
    outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets if
                 'Zika' in tweet.text.encode("utf-8")]
    count1 = 0
    count2 = 0
    for tweet in alltweets:
        if 'Zika' in tweet.text.encode("utf-8"):
            count1 += 1
    # print "%s tweet/s out of %s contain zika term" %(count1, (len(alltweets)))
    for tweet in alltweets:
        if 'Zika' in tweet.text.encode("utf-8"):
            if 'RT' in tweet.text.encode("utf-8"):
                count2 += 1
    print "%s tweet/s out of %s contain zika term and %s of it/them are retweets" % (count1, (len(alltweets)), count2)

    # write the csv
    with open('%s_tweets.csv' % screen_name, 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(["id", "created_at", "text"])
        writer.writerows(outtweets)
    pass

if __name__ == '__main__':
    # pass in the username of the account you want to download
    get_all_tweets("sonar_guy")

#######################################################################################################################

#Try and find all the replies to a certain tweet
#that is classified as a possible rumor
#
#Input:
#   - tweetID: the ID of the tweet that we want to find replies for
#   - screenName: the screenName of the user of the given tweet
#Output:
#    - users: a list of screenNames from users that have replied to
#       the tweet given as an input
def findReplies(tweetID, screenName):
    userName = "to:" + screenName
    users = []
    try:
        for tweets in api.search(userName, count = 100):
            if tweets.in_reply_to_status_id == tweetID:
                if tweets.author.screen_name not in users:
                    users.append(tweets.author.screen_name)
    except Exception, e:
        pass
    return users

#######################################################################################################################