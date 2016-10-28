from operator import itemgetter

def main():
    global dictionary
    dictionary = {}

    #Number of top bigrams (frequency)
    K = 100

    #Replace this one for tweetList filve (attached in the mail)
    fInputTweets = open(
        "C:\\Users\\diego\\Google Drive\\Personal\\TUe\\WIRDM\\Project\\TrainingData\\tweetList.csv")
    inputLine = fInputTweets.readline()
    j = 0
    while inputLine != "":
        list = inputLine.split(' ')
        bigrams = find_bigrams(list)
        storeStatistics(bigrams)
        inputLine = fInputTweets.readline()
    retrieveTopBigrams(K)
    print bigrams

#def main2():

    #Load bigrams
 #   fBigrams = open("C:\\Users\\diego\\Google Drive\\Personal\\TUe\\WIRDM\\Project\\TrainingData\\tweetList.csv")
 #   inputLine = fBigrams.readline()
  #  j = 0
  #  while inputLine != "":
  #      list = inputLine.split(' ')

    #fInputTweets = open("C:\\Users\\diego\\Google Drive\\Personal\\TUe\\WIRDM\\Project\\TrainingData\\tweetList.csv")
    #inputLine = fInputTweets.readline()
    #j = 0
    #while inputLine != "":
     #   list = inputLine.split(' ')
#    return 0

def find_bigrams(input_list):
  return zip(input_list, input_list[1:])

def storeStatistics(bigrams):

    #Retrieve every bigram and look for the key.
    i = 0
    while i < len(bigrams):
        resp = bigrams[i]
        # Get the current bigram
        bi = resp[0] + ' ' + resp[1]

        #Check if the bigram is in the dictionary. If yes, then ++, otherwise, create a new one
        if dictionary.get(bi) is None:
           dictionary[bi] = 1
        else:
            dictionary[bi]+=1
        i+=1



def retrieveTopBigrams(K):
    result = [None]*K
    sortedDictionary = sorted(dictionary.items(),  key=itemgetter(1), reverse=True)

    # Sort dictionary by size
    for i in range(0, len(sortedDictionary)):
        if i < K:
            result[i] = sortedDictionary[i]
    #Retrieve the top K bigrams

    print 'RESULT'
    print result
    return result



if __name__ == "__main__":
    main();





