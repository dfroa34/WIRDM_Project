import GetUserTweets

def originality(user, numberOfTweets):
    numberOfOriginalTweets = 0
    numberOfRetweets = 0
    for tweet in GetUserTweets.get_X_tweets(user, numberOfTweets):
        if 'RT' in tweet.text:
            numberOfRetweets += 1
        else:
            numberOfOriginalTweets += 1
    if numberOfRetweets == 0:
        numberOfRetweets = 1
    originality = float(numberOfOriginalTweets) / float(numberOfOriginalTweets+numberOfRetweets)
    return originality, numberOfOriginalTweets, numberOfRetweets
