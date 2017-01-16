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
sentiment_score = 0 # for every review
title_score = 0 # for every title
control_title = 0 # for every token in the title
content_score = 0 # for every comment
control_content = 0 #for ervery token in content
### Title Evaluation ###
for n in range(len(ntitle)):
    	for t in ntitle[n]:
            ti = ntitle[n].index(t)
            #Check the positiv words
            for p in poswords:
                match = re.search(p, t)
                if match:
                    print match.group(), 'positiv at', n, ti
                    # print ntitle[n][ti]
                    control_title += 1
                    title_score += control_title
                    if ti != 0:
                        for incr in increaser:
                            inc_match = re.search(incr, ntitle[n][ti-1])
                            if inc_match:
                                print "Increaser at ", n, ti-1, ntitle[n][ti-1]
                                control_title *= 2-1
                                title_score += control_title
                                control_title = 0
                        for ne in negator:
                            ne_match = re.search(ne, ntitle[n][ti-1])
                            if ne_match:
                                print "Negator at ", n, ti-1, ntitle[n][ti-1]
                                control_title *= -2-1
                                title_score += control_title
                                control_title = 0
                else:
                    control_title = 0
            #Check the negativ words
            for nw in negwords:
                match = re.search(nw, t)
                if match:
                    print match.group(), 'negativ at', n, ti
                    # print ntitle[n][ti]
                    control_title -= 1
                    title_score += control_title
                    if ti != 0:
                        for incr in increaser:
                            inc_match = re.search(incr, ntitle[n][ti-1])
                            if inc_match:
                                print "Increaser at ", n, ti-1, ntitle[n][ti-1]
                                control_title *= 2+1
                                title_score += control_title
                                control_title = 0
                        for ne in negator:
                            ne_match = re.search(ne, ntitle[n][ti-1])
                            if ne_match:
                                print "Negator at ", n, ti-1, ntitle[n][ti-1]
                                control_title *= -2+1
                                title_score += control_title
                                control_title = 0
                else:
                    control_title = 0
        if title_score > 0:
            title_eval = "positiv"
        elif title_score == 0:
            title_eval = "neutral"
        elif title_score < 0:
            title_eval = "negativ"
        else:
            print "No title_score is given!"
        print "Sentiment Value", title_score
        print ntitle[n], len(ntitle[n]), "Tokens"
        print title_eval
        print "{}{}{}{}".format(time, " - ", n, ".title was analysed\n\n")
        # sentiment_title(time, db, ntitle[n], n, title_score, title_eval)
        collection[n].insert(len(collection[n]),title_score)
        collection[n].insert(len(collection[n]), title_eval)
        title_score = 0
        #print collection[n]
# print len(ntitle)
# print ntitle[9]
#print ncontent
col = time
# db[col].insert_many([{'titles': i} for i in collection]) works!!!
db[col].insert_many(
    {
        "_id": i[0],
        'title': i[1],
        'content': i[2],
        'city': i[3],
        'hotel_name': i[4],
        'review_stars': i[5],
        'helpful_reader': i[6],
        'title_score': i[7],
        'title_eval': i[8]
    }
    for i in collection
)
#print results
# print collection[0]
