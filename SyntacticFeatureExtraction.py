__author__ = 's149830'

import csv

class syntacticFeatureExtractor:
    """
    Input: text of the tweet
    Output: if the text contains '!' and '?'
    """
    def punctuation(self, tweet):
        containQ = 0
        containE = 0
        if ('!' in tweet):
            containQ = 1
        if ('?' in tweet):
            containE = 1
        #print containQ, containE
        return [containQ, containE]

    """
    Input: Text of the tweet
    Output: If the text contains '#', '@' or 'RT'
    """
    def specificCharacter(self, tweet):
        hashtag = 0
        a = 0
        retweet = 0
        if('#' in tweet):
            hashtag = 1
        if('@' in tweet):
            a = 1
        if('RT' in tweet):
            retweet = 1

        return [hashtag, a, retweet]

    """
    Input: Text of the tweet
    Output: If there exist any abbreviations.
    """
    def abbreviation(self, tweet):
        with open('abbsDic.csv', 'rb') as dic:
            rdr = csv.reader(dic)
            acronym = 0
            for row in rdr:
                for abb in row:
                    if(abb) in tweet:
                        acronym = 1
            dic.close()
        return acronym


    #def subTree(self, tweet):


