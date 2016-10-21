import GetUserTweets

#######################################################################################################################

#Calculate an originality score for the user, which is defined as the number of original
#tweets from a user (so not a retweet) divided by the total number of tweets from a user
#
#Input:
#   - username: a user to calculate the originalty score for
#   - numberOfTweets: the last X tweets from the given user to calculate the originality score for
#Output:
#   - originality: the originality score (between 0 and 1) for the given user over the last X tweets
#   - numberOfOriginalTweets: the number of original tweets (so not a retweet) from the given user
#   - numberOfRetweets: the number of retweets from the given user
def originality(username, numberOfTweets):
    numberOfOriginalTweets = 0
    numberOfRetweets = 0
    if numberOfTweets > 200:
        numberOfTweets = 200
    for tweet in GetUserTweets.get_X_tweets(username, numberOfTweets):
        if 'RT' in tweet.text:
            numberOfRetweets += 1
        else:
            numberOfOriginalTweets += 1
    if numberOfRetweets == 0:
        numberOfRetweets = 1
    originality = float(numberOfOriginalTweets) / float(numberOfOriginalTweets+numberOfRetweets)
    return originality, numberOfOriginalTweets, numberOfRetweets

#----------------------------------------------------------------------------------------------------------------------

#Check wheter or not a user has been verified by Twitter. According
#to Twitter a verified account is of general importance to the audience
#
#Input:
#   - username: a user to check the credibility for
#Output:
#   - credible: a boolean value (1, 0) defining whether
#       or not the given user has been verified by Twitter
def credibility(username):
    credible = 0
    user = GetUserTweets.api.get_user(username)
    if user.verified == True:
        credible = 1
    return credible

#----------------------------------------------------------------------------------------------------------------------

#Check how much influence a user has on Twitter. This is
#simply the number of followers for a certain user
#
#Input:
#   - username: a user to check the influence for
#Output:
#   - user.followers_count: the number of followers the given user has
def influence(username):
    user = GetUserTweets.api.get_user(username)
    return user.followers_count

#----------------------------------------------------------------------------------------------------------------------