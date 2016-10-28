import GetUserTweets as userTweets
import datetime

#######################################################################################################################

#Calculate an originality score for the user, which is defined as the number of original
#tweets from a user (so not a retweet) divided by the total number of tweets from a user
#
#Input:
#   - username: a user to calculate the originalty score for
#   - numberOfTweets: the last X tweets from the given user to calculate the originality score for
#Output:
#   - originality: the originality score (between 0 and 1) for the given user over the last X tweets
def originality(username, numberOfTweets):
    numberOfOriginalTweets = 0
    numberOfRetweets = 0
    if numberOfTweets > 200:
        numberOfTweets = 200
    try:
        for tweet in userTweets.api.user_timeline(screen_name = username, count = numberOfTweets, include_rts = True):
            if 'RT' in tweet.text:
                numberOfRetweets += 1
            else:
                numberOfOriginalTweets += 1
        if (numberOfOriginalTweets + numberOfRetweets) == 0:
            numberOfRetweets = 1
        originality = float(numberOfOriginalTweets) / float(numberOfOriginalTweets + numberOfRetweets)
    except Exception, e:
        originality = "N/A"
        pass
    return originality

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
    try:
        user = userTweets.api.get_user(username)
        if user.verified == True:
            credible = 1
    except Exception, e:
        credible = "N/A"
        pass
    return credible

#----------------------------------------------------------------------------------------------------------------------

#Check how much influence a user has on Twitter. This is
#simply the number of followers for a certain user
#
#Input:
#   - username: a user to check the influence for
#Output:
#   - followers: the number of followers the given user has
def influence(username):
    try:
        user = userTweets.api.get_user(username)
        followers = user.followers_count
    except Exception, e:
        followers = "N/A"
        pass
    return followers

#----------------------------------------------------------------------------------------------------------------------

# Check how engaged a user is with Twitter. This means how
# active a user is with tweeting activites on Twitter
#
# Input:
#   - username: a user to check the engagement for
#   - numberOfTweets: the number of tweets from the given user
# Output:
#   - engagement: an indication how active a user is
def engagement(username, numberOfTweets):
    try:
        user = userTweets.api.get_user(username)
        numberOfFavs = user.favourites_count
        accountAge = datetime.datetime.now().date() - user.created_at.date()
        if accountAge.days == 0:
            accountAge.days = 1
        engagement = (float(numberOfTweets + numberOfFavs)) / float(accountAge.days)
    except Exception, e:
        engagement = "N/A"
        pass
    return engagement

#######################################################################################################################