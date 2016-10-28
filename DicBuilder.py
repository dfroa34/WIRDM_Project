import urllib2
import re
import csv

url = "http://www.netlingo.com/acronyms.php"

response = urllib2.urlopen(url)
content = response.read()

pattern1 = r'<a href="http:\/\/www\.netlingo\.com\/word\/.{1,11}>.{1,12}<\/a>'
pattern2 = r'>.{1,12}<'

ul = re.findall(pattern1, content)
abbs = []

for a in ul[4:]:
    item = re.findall(pattern2,a)[0][1:-1]
    abbs.append(item)

print abbs

with open('abbsDic.csv', 'wb') as f:
    wrt = csv.writer(f)
    for abb in abbs:
        wrt.writerow(abb)
