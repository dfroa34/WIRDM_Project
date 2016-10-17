__author__ = 's149830'

import csv

class syntacticFeatureExtractor:
    def punctuation(self, tweet):
        containQ = False
        containE = False
        if ('!' in tweet):
            containQ = True
        if ('?' in tweet):
            containE = True
        print containQ, containE
        return containQ, containE

    def specificCharacter(self, tweet):
        hashtag = False
        a = False
        retweet = False
        if('#' in tweet):
            hashtag = True
        if('@' in tweet):
            a = True
        if('RT' in tweet):
            retweet = True
        return hashtag, a, retweet

    def abbreviation(self, tweet):
        with open('acronymsDic.csv', 'rb') as dic:
            rdr = csv.reader(dic)
            acronym = False
            for row in rdr:
                for abb in row:
                    if(abb) in tweet:
                        acronym = True
            dic.close()
        return acronym

    #def subTree(self, tweet):


