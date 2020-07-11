import csv
import string
from nltk.corpus import stopwords
#from nltk.stem.porter import PorterStemmer

stop_words = set(stopwords.words('english'))
#porter = PorterStemmer()

author = []
content = []
date = []
title = []

with open('trydata.csv', 'r', encoding='utf8') as file:
    reader = csv.reader(file)

    for row in reader:
        author.append(row[0])
        content.append(row[1])
        date.append(row[2])
        title.append(row[3])


def cleaning(rawcontent):
    content=[]

    for text in rawcontent:
        clean = ""
        for letter in text:
            if letter in string.ascii_lowercase:
                clean+=letter
            elif letter in string.ascii_uppercase:
                clean+=letter.lower()
            elif letter==' ':
                clean+=letter
    
        clean = clean.split()
        clean=[word for word in clean if word not in stop_words]

        content.append(clean)
    
    return content

title = cleaning(title)
content = cleaning(content)

print(title)
print(content)