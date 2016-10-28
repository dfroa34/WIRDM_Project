__author__ = 's149830'

import csv
import SemanticFeatureExtraction
import SyntacticFeatureExtraction
import UserFeatureExtraction
"""
The new basic features:
1	    |2	   |3	     |4	               |5	        |6		        |7
UserName|UserID|TweetText|DateOfPublication|#ofFollowers|#ofFollowings	|#ofStatuses

"""
with open('tweets.csv','rb') as ogn:
    reader = csv.reader(ogn, delimiter='\t')
    basic = []
    labels = []
    count = 0
    for row in reader:
        count += 1
        if(row[10] == 'R' or row[10] == 'NR' or row[10] == 'U'):
            newrow1 = row[1:4]
            newrow2 = row[5:9]
            newrow1 = newrow1+newrow2
            basic.append(newrow1)
            labels.append(row[10])


Semantic = SemanticFeatureExtraction.semanticFeatureExtractor()
Syntactic = SyntacticFeatureExtraction.syntacticFeatureExtractor()
feature_list = []

for row in basic:
    feature = []
    # Extract semantic features
    opinion = Semantic.opinionWords(row[3])
    vulgar = Semantic.vulgarWords(row[3])
    act = Semantic.speechAct(row[3])
    biGrams = Semantic.biGrams(row[3])
    feature.append(opinion)
    feature.append(vulgar)
    feature.extend(act)
    feature.extend(biGrams)

    # Extract syntactic features
    Punctuation = Syntactic.punctuation(row[3])
    tweetSpecific = Syntactic.specificCharacter(row[3])
    abbriviation = Syntactic.abbreviation(row[3])
    url = Syntactic.containsURL(row[3])
    feature.extend(Punctuation)
    feature.extend(tweetSpecific)
    feature.append(abbriviation)
    feature.append(url)

    # Extract user features
    origin = UserFeatureExtraction.originality(row[0], row[6])
    credit = UserFeatureExtraction.credibility(row[0])
    influence = UserFeatureExtraction.influence(row[0])
    feature.append(origin)
    feature.append(credit)
    feature.append(influence)

    feature_list.append(feature)

with open('newMykola.csv','wb') as Mykola:


