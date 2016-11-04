import GetUserTweets as userTweets

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
        for tweets in userTweets.api.search(userName, count = 100):
            if tweets.in_reply_to_status_id == tweetID:
                users.append(tweets.author.screen_name)
    except Exception, e:
        pass
    return users

#######################################################################################################################