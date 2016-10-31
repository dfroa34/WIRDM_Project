__author__ = 's149830'

import csv
import SemanticFeatureExtraction
import SyntacticFeatureExtraction
import UserFeatureExtraction

"""
The new basic features:
0	    |1	   |2	     |3	               |4	        |5		        |6
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
            if row[10] == 'R':
                labels.append(1)
            elif row[10] == 'NR':
                labels.append(0)
            else:
                labels.append(2)


print "Extract finish..."


Semantic = SemanticFeatureExtraction.semanticFeatureExtractor()
Syntactic = SyntacticFeatureExtraction.syntacticFeatureExtractor()
feature_list = []
count = 0

print
for row in basic:
    feature = []
    # feature += row
    # Extract semantic features
    opinion = Semantic.opinionWords(row[2])
    vulgar = Semantic.vulgarWords(row[2])
    act = Semantic.speechAct(row[2])
    biGrams = Semantic.biGrams(row[2])
    feature.append(opinion)
    feature.append(vulgar)
    feature.extend(act)
    feature.extend(biGrams)

    # Extract syntactic features
    Punctuation = Syntactic.punctuation(row[2])
    tweetSpecific = Syntactic.specificCharacter(row[2])
    abbriviation = Syntactic.abbreviation(row[2])
    url = Syntactic.containsURL(row[2])
    feature.extend(Punctuation)
    feature.extend(tweetSpecific)
    feature.append(abbriviation)
    feature.append(url)

    # Extract user features
    origin = UserFeatureExtraction.originality(row[0], row[6])
    credit = UserFeatureExtraction.credibility(row[0])
    influence = UserFeatureExtraction.influence(row[0])
    egagement = UserFeatureExtraction.engagement(row[0], row[6])
    feature.append(origin)
    feature.append(credit)
    feature.append(influence)
    feature.append(egagement)
    feature.append(labels[count])
    count += 1
    feature_list.append(feature)


print "Finish processing..."

with open('newMykola3.csv','wb') as file:
    wrt = csv.writer(file)
    for feature in feature_list:
        wrt.writerow(feature)
