__author__ = 's149830'

import csv
import ast
import SemanticFeatureExtraction
import SyntacticFeatureExtraction
import UserFeatureExtraction
import re

f = open('backup2.txt','r')
rawTweets = f.readlines()
tweetData = []
semanticExtract = SemanticFeatureExtraction.semanticFeatureExtractor()
syntacticExtract = SyntacticFeatureExtraction.syntacticFeatureExtractor()

feature_list = []



for tweet in rawTweets:
    tweetData.append(ast.literal_eval(tweet))

for tweet in tweetData[0:200]:
    feature = []

    #Extract basic features
    userName = tweet['user']['screen_name'].encode('utf-8')
    userID = tweet['user']['id']
    text = tweet['text'].encode('utf-8')
    publication = tweet['created_at'].encode('utf-8')
    followers = tweet['user']['followers_count']
    following = tweet['user']['friends_count']
    status = tweet['user']['statuses_count']

    #urls = tweet['entities']['urls'][0]['url'] if tweet['entities']['urls'][0] else 'None'
    feature.append(userName)
    feature.append(userID)
    feature.append(text)
    feature.append(publication)
    feature.append(followers)
    feature.append(following)
    feature.append(status)
    #feature.append(urls)

    #Extract semantic features
    opinion = semanticExtract.opinionWords(text)
    vulgar = semanticExtract.vulgarWords(text)
    act = semanticExtract.speechAct(text)
    biGrams = semanticExtract.biGrams(text)
    feature.append(opinion)
    feature.append(vulgar)
    feature.extend(act)
    feature.extend(biGrams)

    #Extract syntactic features
    Punctuation = syntacticExtract.punctuation(text)
    tweetSpecific = syntacticExtract.specificCharacter(text)
    abbriviation = syntacticExtract.abbreviation(text)
    url = syntacticExtract.containsURL(text)
    feature.extend(Punctuation)
    feature.extend(tweetSpecific)
    feature.append(abbriviation)
    feature.append(url)

    #Extract user features
    origin = UserFeatureExtraction.originality(userName, status)
    credit = UserFeatureExtraction.credibility(userName)
    influence = UserFeatureExtraction.influence(userName)
    feature.append(origin)
    feature.append(credit)
    feature.append(influence)

    #Determine if there is a url in the text

    feature_list.append(feature)

with open('newDataSet.csv', 'wb') as dts:
    wrt = csv.writer(dts, dialect='excel')
    for feature in feature_list:
        wrt.writerow(feature)



