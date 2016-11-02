import subprocess
import ConfigParser
import os
from whoosh.lang.porter import stem



#Retrieves the top K most similar tweets given a query
#@input query - the raw query from the interface
#@output a list of similar tweets from our dataset
def retrieveTopKSimilarTweets(query):

    #If you want to test with a sample query
    #query = "mosquito prevention"
    #print query

    #Load properties
    global config
    config= ConfigParser.RawConfigParser()
    config.read('properties.txt')
    global terrierLocation
    terrierLocation = config.get('Properties','terrierLocation')
    K = config.get('Properties','K')

    #Retrieval Process
    indexDocuments()
    newQuery = processQuery(query)
    topic = generateTopicInputFile(newQuery)
    results = executeRetrievalTask(topic)
    return readResults(results, K)



def indexDocuments():
    print "Indexing....................................................................................."
    indexDataset = os.path.abspath("DatasetForIndexing.txt")
    # Add the dataset into the collection.spec file
    f =open(terrierLocation + "\\etc\\collection.spec", 'w')
    f.write(indexDataset)
    f.close()

    #Check if the index folder is empty.
    if os.listdir(terrierLocation + "\\var\\index\\") =="":
      subprocess.check_output('cd ' +
                            '&& trec_terrier.bat -i', stderr=subprocess.STDOUT, shell=True)
#
# Generate the Input File for the IR task.
# The file is in xml format organized as follows: top (topic), num (query id), query
#
def generateTopicInputFile(query):

    print "Generating topic file............................................................................"
    topicFile = 'topicFile.txt'
    f = open(topicFile, 'w')
    f.write('<top> \n')
    f.write('<num> Number: Q1 </num> \n')
    f.write('<query>' + query +'</query> \n')
    f.write('</top>')
    print 'TopicFile: ' + os.path.abspath("topicFile.txt")
    return os.path.abspath("topicFile.txt")


#
#  Execute the retrieval task in Terrier.
#  @return returns the result file with all the relevant tweets for the specific query
#
def executeRetrievalTask(topicLocation):
    print "Executing RetrievalTask........................................................................."
    return_code = subprocess.check_output('cd ' + terrierLocation + '\\bin  && trec_terrier.bat -r -q -Dtrec.model=BM25 -Dtrec.topics='+ topicLocation
                                          ,stderr=subprocess.STDOUT, shell=True)


    offsetPath = return_code.find("results written to")
    resultFile = return_code[offsetPath+19:-32]

    print 'RetrievalResult: ' + resultFile
    return resultFile


#
# Read the result file from the Terrier task
# First, it takes all the tweets ID from the result file and then it retrieves the tweets from the inputDataSet given the tweets id
#
def readResults(results, K):

  #Get tweets id from resultsFile
    print 'Reading Results................................................................................'

    fResults = open(results)
    line = fResults.readline()
    relevantTweets = []

    i=0
    while line != "":
        splitLine = line.split(" ")
        relevantTweets.append(splitLine[2])
        line = fResults.readline()
        i+=1

    print 'Relevant tweets IDs: '
    print relevantTweets[0:int(K)]

    #Get tweet from the IR inputData given the tweet ID
    similarTweets = []

    for i in relevantTweets:
        tweetID = i
        fInputTweets = open("rawtweets.txt")
        inputLine = fInputTweets.readline()
        j=0
        while inputLine is not None and inputLine!="":
            if j == (int(tweetID) - 1):
                similarTweets.append(inputLine)
                break
            j+=1
            inputLine = fInputTweets.readline()

    print 'Relevant tweets text: '
    print  similarTweets[0:int(K)]
    return similarTweets[0:int(K)]


def processQuery(query):
        print 'Processing query:' + query + ' .....................................'
        #Remove stopwords
        resp = ""
        f = open('stopword-list.txt')
        l = f.readlines()
        theList =map(str.strip, l)

        for word in query.split():
            if word not in theList:
                resp = resp +" " + word

        #Use porter stemmer
        resp = stem(resp)

        print 'Query: ' + resp
        return resp


if __name__ == "__main__":
    retrieveTopKSimilarTweets('Zika symptoms are irelevant');


