from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
import string
import re
import csv

contentlist = []
ps = PorterStemmer()
text = "Spanoulis, played an instrumental role on the senior men's Greek national team's EuroBasket 2005 gold medal team  \U0001f602."

#emoji removal

emoji_pattern = re.compile(u'('
    u'\ud83c[\udf00-\udfff]|'
    u'\ud83d[\udc00-\ude4f\ude80-\udeff]|'
    u'[\u2600-\u26FF\u2700-\u27BF])+', 
    re.UNICODE)
print text
print(emoji_pattern.sub(r'', text)) # no emoji


#lowercase, stemming, remove stop_words
s = text.translate(string.maketrans("",""), string.punctuation)
s = s.lower()
stop_words = set(stopwords.words("english"))
words = word_tokenize(s)
filtered_sentence = [w for w in words if w not in stop_words]
for x in filtered_sentence:
    print (ps.stem(x))

"""
# save to txt
contentlist.append(text)
print contentlist
f = open("normalized.txt", 'ab')
wrt = csv.writer(f, dialect='excel')
try:
    wrt.writerow(text)
except UnicodeEncodeError, UnicodeEncodeError:
    return True
"""