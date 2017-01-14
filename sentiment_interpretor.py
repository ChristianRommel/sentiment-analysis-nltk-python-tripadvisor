import re
import time
from pymongo import InsertOne, DeleteOne, ReplaceOne
from array import *
from mongodb_connect import db
import reader
#set the arrays for the interpretor
ntitle = reader.ntitle
ncontent = reader.ncontent
collection = reader.collection
#set the timestamp
time = time.strftime("%d.%m.%Y %H:%M:%S")
#set the wordlists and save them to a new list
poswords = []
negwords = []
negator = []
increaser = []
results = []
with open ('wordlist/positiv.txt', 'r') as obj1:
    for w in obj1:
        pos = w.lower().rstrip()
        pos = re.escape(pos)
        pos = re.compile("{}{}{}".format("\\b", pos, "[a-z]*"))
        # pos = re.compile(pos)
        poswords.append(pos)
with open ('wordlist/negativ.txt', 'r') as obj2:
    for w in obj2:
        neg = w.lower().rstrip()
        neg = re.escape(neg)
        neg = re.compile("{}{}{}".format("\\b", neg, "[a-z]*"))
        # neg = re.compile(neg)
        negwords.append(neg)
with open ('wordlist/negator.txt', 'r') as obj3:
    for w in obj3:
        ngtr = w.lower().rstrip()
        ngtr = re.escape(ngtr)
        ngtr = re.compile(ngtr)
        negator.append(ngtr)
with open ('wordlist/increaser.txt', 'r') as obj4:
    for w in obj4:
        inc = w.lower().rstrip()
        inc = re.escape(inc)
        inc = re.compile(inc)
        increaser.append(inc)
#set score variables
sentiment_score = 0 # for every title
control = 0 # for every token in the title
for n in range(len(ntitle)):
    	for t in ntitle[n]:
            ti = ntitle[n].index(t)
            #Check the positiv words
            for p in poswords:
                match = re.search(p, t)
                if match:
                    print match.group(), 'positiv at', n, ti
                    # print ntitle[n][ti]
                    control += 1
                    sentiment_score += control
                    if ti != 0:
                        for incr in increaser:
                            inc_match = re.search(incr, ntitle[n][ti-1])
                            if inc_match:
                                print "Increaser at ", n, ti-1, ntitle[n][ti-1]
                                control *= 2-1
                                sentiment_score += control
                                control = 0
                        for ne in negator:
                            ne_match = re.search(ne, ntitle[n][ti-1])
                            if ne_match:
                                print "Negator at ", n, ti-1, ntitle[n][ti-1]
                                control *= -2-1
                                sentiment_score += control
                                control = 0
                else:
                    control = 0
            #Check the negativ words
            for nw in negwords:
                match = re.search(nw, t)
                if match:
                    print match.group(), 'negativ at', n, ti
                    # print ntitle[n][ti]
                    control -= 1
                    sentiment_score += control
                    if ti != 0:
                        for incr in increaser:
                            inc_match = re.search(incr, ntitle[n][ti-1])
                            if inc_match:
                                print "Increaser at ", n, ti-1, ntitle[n][ti-1]
                                control *= 2+1
                                sentiment_score += control
                                control = 0
                        for ne in negator:
                            ne_match = re.search(ne, ntitle[n][ti-1])
                            if ne_match:
                                print "Negator at ", n, ti-1, ntitle[n][ti-1]
                                control *= -2+1
                                sentiment_score += control
                                control = 0
                else:
                    control = 0
        if sentiment_score > 0:
            sentieval = "positiv"
        elif sentiment_score == 0:
            sentieval = "neutral"
        elif sentiment_score < 0:
            sentieval = "negativ"
        else:
            print "No sentiment_score is given!"
        print "Sentiment Value", sentiment_score
        print ntitle[n], len(ntitle[n]), "Tokens"
        print sentieval
        print "{}{}{}{}".format(time, " - ", n, ".title was analysed\n\n")
        # sentiment_title(time, db, ntitle[n], n, sentiment_score, sentieval)
        sentiment_score = 0
# print len(ntitle)
# print ntitle[9]
#print ncontent
col = time
# db[col].insert_many([{'titles': i} for i in collection]) works!!!
db[col].insert_many(
    {
        'title': i[0],
        'content': i[1],
        'city': i[2],
        'hotel_name': i[3],
        'review_stars': i[4],
    }
    for i in collection
)
#print results
#print collection[0]
