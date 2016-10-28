__author__ = 's149830'

import csv
import json
import ast
import SemanticFeatureExtraction
import SyntacticFeatureExtraction
import UserFeatureExtraction
import sys

f = open('backup2.txt','r')
rawTweets = f.readlines()
tweetData = []
semanticExtract = SemanticFeatureExtraction.semanticFeatureExtractor()
syntacticExtract = SyntacticFeatureExtraction.syntacticFeatureExtractor()

feature_list = []

for tweet in rawTweets:
    tweetData.append(ast.literal_eval(tweet))

for tweet in tweetData[0:5]:
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
    feature.extend(Punctuation)
    feature.extend(tweetSpecific)
    feature.append(abbriviation)

    #Extract user features

    feature_list.append(feature)

print feature_list[0]

with open('newDataSet.csv', 'w') as dts:
    wtr = csv.writer(dts, sys.stdout)
    wtr.writerow(feature_list[0])





