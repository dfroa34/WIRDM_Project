import csv
import nltk
from nltk.corpus import opinion_lexicon
from nltk.stem import porter
with open('StemedSemanticMykola.csv','rb') as semantic:
    with open('SyntacticFeatureMykola.csv','rb') as syntactic:
        with open('newMykola3.csv','rb') as usernLabel:
            #Read semantic features
            SemReader = csv.reader(semantic)
            #Read syntactic features
            SynReader = csv.reader(syntactic)
            #Read user features
            RestReader = csv.reader(usernLabel)

            features = []
            Semantic = []
            Syntactic = []
            RestFeature = []
            new_features = []

            # Load the semantic features
            for sem in SemReader:
                Semantic.append(sem)

            # Load the syntactic features
            for syn in SynReader:
                Syntactic.append(syn)

            # Load the user features
            for re in RestReader:
                RestFeature.append(re)

            # Loop through three feature lists, then append features in the same position together.
            for i, se in enumerate(Semantic):
                feature = []
                feature.extend(Semantic[i])
                feature.extend(Syntactic[i])
                feature.extend(RestFeature[i])
                features.append(feature)

            #If there are any samples contains 'N/A', then delete this sample.
            for item in features:
                if 'N/A' in item:
                    continue
                new_features.append(item)

# Write the features into the file
with open('newMykola5.csv','wb') as new:
    wtr = csv.writer(new)
    for feature in new_features:
        wtr.writerow(feature)


