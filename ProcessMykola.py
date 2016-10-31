__author__ = 's149830'

import csv
import SemanticFeatureExtraction
import SyntacticFeatureExtraction
import UserFeatureExtraction
from nltk.tokenize import TweetTokenizer
from nltk.stem import PorterStemmer

tokenizer = TweetTokenizer()
stemmer = PorterStemmer()

"""
The new basic features:
0	    |1	   |2	     |3	               |4	        |5		        |6
UserName|UserID|TweetText|DateOfPublication|#ofFollowers|#ofFollowings	|#ofStatuses
"""

with open('tweets.csv', 'rb') as ogn:
    reader = csv.reader(ogn, delimiter='\t')
    basic = []
    labels = []
    count = 0

    for row in reader:
        count += 1
        if (row[10] == 'R' or row[10] == 'NR' or row[10] == 'U'):
            newrow1 = row[1:4]
            newrow2 = row[5:9]
            newrow1 = newrow1 + newrow2
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
SemanticFeatures = []
SyntacticFeatures = []
UserFeatures = []
count = 0

print
for row in basic:
    feature = []
    SemanticFeature = []
    SyntacticFeature = []
    UserFeature = []

    # feature += row
    # Extract semantic features
    """
    tokenizedText = tokenizer.tokenize(row[2])
    processedText = ' '.join(stemmer.stem(word) for word in tokenizedText)
    opinion = Semantic.opinionWords(processedText)
    vulgar = Semantic.vulgarWords(row[2])
    act = Semantic.speechAct(processedText)
    biGrams = Semantic.biGrams(row[2])

    feature.append(opinion)
    feature.append(vulgar)
    feature.extend(act)
    feature.extend(biGrams)

    SemanticFeature.append(opinion)
    SemanticFeature.append(vulgar)
    SemanticFeature.extend(act)
    SemanticFeature.extend(biGrams)
    """

    """
    # Extract syntactic features
    Punctuation = Syntactic.punctuation(row[2])
    tweetSpecific = Syntactic.specificCharacter(row[2])
    abbriviation = Syntactic.abbreviation(row[2])
    url = Syntactic.containsURL(row[2])
    feature.extend(Punctuation)
    feature.extend(tweetSpecific)
    feature.append(abbriviation)
    feature.append(url)
    SyntacticFeature.extend(Punctuation)
    SyntacticFeature.extend(tweetSpecific)
    SyntacticFeature.append(abbriviation)
    SyntacticFeature.append(url)
    """


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
    UserFeature.append(origin)
    UserFeature.append(credit)
    UserFeature.append(influence)
    UserFeature.append(egagement)
    UserFeature.append(labels[count])
    count += 1


    #feature_list.append(feature)
    #SemanticFeatures.append(SemanticFeature)
    #SyntacticFeatures.append(SyntacticFeature)
    UserFeatures.append(UserFeature)

"""
print "Finish processing..."

# Write user features
with open('UserFeatureMykola.csv', 'wb') as user:
    wrt = csv.writer(user)
    for feature in UserFeatures:
        wrt.writerow(feature)

# Write semantic features
with open('SemanticFeatureMykola.csv', 'wb') as seman:
    wrt = csv.writer(seman)
    for feature in SemanticFeatures:
        wrt.writerow(feature)

# Write syntactic features
with open('SyntacticFeatureMykola.csv', 'wb') as syn:
    wrt = csv.writer(syn)
    for feature in SyntacticFeatures:
        wrt.writerow(feature)

# Write all features
with open('newMykola4.csv', 'wb') as whole:
    wrt = csv.writer(whole)
    for feature in feature_list:
        wrt.writerow(feature)
"""



