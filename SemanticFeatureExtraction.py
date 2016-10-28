import csv
from profanity import profanity

#######################################################################################################################

class semanticFeatureExtractor:

#----------------------------------------------------------------------------------------------------------------------

    #Check for opinion words by comparing every word in a tweet
    #with every opinion word in the list of opinion words
    #
    #Input:
    #   - tweet: a tweet to check for any opinion words
    #   Please note that the input needs to be a PREPROCESSED tweet!
    #Output:
    #   - opinion: a single boolean value (0, 1) indicating the
    #      presence of a certain opinion word in the given tweet
    def opinionWords(self, tweet):
        with open('OpinionWords.csv', 'rb') as lexicon:
            reader = csv.reader(lexicon)
            opinion = 0
            for row in reader:
                for opinionWord in row:
                    if opinionWord in tweet:
                        opinion = 1
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

    #Check for vulgar words by comparing every word in a tweet
    #with every vulgar word in the list of vulgar words
    #
    #Input:
    #   - tweet: a tweet to check for any vulgar words
    #Output:
    #   - vulgar: a single boolean value (0, 1) indicating
    #       the presence of a vulgar word in the given tweet
    def vulgarWords(self, tweet):
        vulgar = 0
        if profanity.contains_profanity(tweet):
            vulgar = 1
        return vulgar

#----------------------------------------------------------------------------------------------------------------------

    #Check for speech act verbs by comparing every word in a tweet
    #with every speech act verb in the list of speech act verbs
    #
    #Input:
    #   - tweet: a tweet to check for any speech act verbs
    #   Please note that the input needs to be a PREPROCESSED tweet!
    #Output:
    #   - speechAct: a list of boolean values (0, 1) indicating
    #       the presence of a speech act verb in the given tweet
    def speechAct(self, tweet):
        with open('SpeechActVerbs.csv', 'rb') as lexicon:
            reader = csv.reader(lexicon)
            speechAct = []
            for row in reader:
                for speechActWord in row:
                    if speechActWord in tweet:
                        speechAct += [1]
                    else:
                        speechAct += [0]
            lexicon.close()
        return speechAct

    # Semantic analysis of English performative verbs
    # http://www.uqtr.ca/~vandervk/english_performative_verbs_ch6.pdf

#----------------------------------------------------------------------------------------------------------------------

    #Check for the appearance of the most common bigrams in a tweet
    #
    #Input:
    #   - tweet: a tweet to check for any of the bigrams
    #Output:
    #   - biGram: a list of boolean values (0, 1) indicating
    #      the presence of a bigram in the given tweet
    def biGrams(self, tweet):
        with open('BiGrams.csv', 'rb') as lexicon:
            reader = csv.reader(lexicon)
            biGram = []
            for row in reader:
                for biGramWords in row:
                    if biGramWords in tweet:
                        biGram += [1]
                    else:
                        biGram += [0]
            lexicon.close()
        return biGram

#######################################################################################################################