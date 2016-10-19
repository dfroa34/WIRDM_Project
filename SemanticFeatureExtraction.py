import csv
from profanity import profanity

#######################################################################################################################

class semanticFeatureExtractor:

#----------------------------------------------------------------------------------------------------------------------

    #Check for opinion words by comparing every word from every tweet
    #with every opinion word in the list of opinion words
    #
    #Please note that the input needs to be a PROCESSED tweet!
    def opinionWords(self, tweet):
        with open('OpinionWords.csv', 'rb') as lexicon:
            reader = csv.reader(lexicon)
            opinion = False
            for row in reader:
                for opinionWord in row:
                    if opinionWord in tweet:
                        opinion = True
            lexicon.close()
        return opinion

    #The OpinionWords list and the papers can all be downloaded from
    #http://www.cs.uic.edu/~liub/FBS/sentiment-analysis.html
    #
    #If you use this list, please cite one of the following two papers:
    #
    #Minqing Hu and Bing Liu. "Mining and Summarizing Customer Reviews."
    #   Proceedings of the ACM SIGKDD International Conference on Knowledge
    #   Discovery and Data Mining (KDD-2004), Aug 22-25, 2004, Seattle,
    #   Washington, USA,
    #Bing Liu, Minqing Hu and Junsheng Cheng. "Opinion Observer: Analyzing
    #   and Comparing Opinions on the Web." Proceedings of the 14th
    #   International World Wide Web conference (WWW-2005), May 10-14,
    #   2005, Chiba, Japan.

#----------------------------------------------------------------------------------------------------------------------

    #Check for vulgar words in the input tweets
    def vulgarWords(self, tweet):
        vulgar = False
        if profanity.contains_profanity(tweet):
            vulgar = True
        return vulgar

#----------------------------------------------------------------------------------------------------------------------

    #Check for speech act verbs in the input tweets by comparing every word
    #from every tweet with every speech act verb in the list of speech act verbs
    #
    #Please note that the input needs to be a PROCESSED tweet!
    def speechAct(self, tweet):
        with open('SpeechActVerbs.csv', 'rb') as lexicon:
            reader = csv.reader(lexicon)
            speechAct = False
            for row in reader:
                for speechActWord in row:
                    if speechActWord in tweet:
                        speechAct = True
            lexicon.close()
        return speechAct

    # Semantic analysis of English performative verbs
    # http://www.uqtr.ca/~vandervk/english_performative_verbs_ch6.pdf

#######################################################################################################################