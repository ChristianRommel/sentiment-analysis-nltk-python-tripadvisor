import re
import time
from pymongo import InsertOne, DeleteOne, ReplaceOne
from array import *
from mongodb_connect import db
from evaluation import sentieval
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
        # Title Evaluation
        if title_score > 0:
            title_eval = "positiv"
        elif title_score == 0:
            title_eval = "neutral"
        elif title_score < 0:
            title_eval = "negativ"
        else:
            print "No title_score is given!"
        # Resume
        print "Sentiment Value", title_score
        print ntitle[n], len(ntitle[n]), "Tokens"
        print title_eval
        print "{}{}{}{}".format(time, " - ", n, ".title was analysed\n\n")
        #Insert to collection
        collection[n].insert(len(collection[n]),title_score)
        collection[n].insert(len(collection[n]), title_eval)
        title_score = 0
### Content Evaluation ###
for n in range(len(ncontent)):
    	for t in ncontent[n]:
            ti = ncontent[n].index(t)
            #Check the positiv words
            for p in poswords:
                match = re.search(p, t)
                if match:
                    print match.group(), 'positiv at', n, ti
                    # print ncontent[n][ti]
                    control_content += 1
                    content_score += control_content
                    if ti != 0:
                        for incr in increaser:
                            inc_match = re.search(incr, ncontent[n][ti-1])
                            if inc_match:
                                print "Increaser at ", n, ti-1, ncontent[n][ti-1]
                                control_content *= 2-1
                                content_score += control_content
                                control_content = 0
                        for ne in negator:
                            ne_match = re.search(ne, ncontent[n][ti-1])
                            if ne_match:
                                print "Negator at ", n, ti-1, ncontent[n][ti-1]
                                control_content *= -2-1
                                content_score += control_content
                                control_content = 0
                else:
                    control_content = 0
            #Check the negativ words
            for nw in negwords:
                match = re.search(nw, t)
                if match:
                    print match.group(), 'negativ at', n, ti
                    # print ncontent[n][ti]
                    control_content -= 1
                    content_score += control_content
                    if ti != 0:
                        for incr in increaser:
                            inc_match = re.search(incr, ncontent[n][ti-1])
                            if inc_match:
                                print "Increaser at ", n, ti-1, ncontent[n][ti-1]
                                control_content *= 2+1
                                content_score += control_content
                                control_content = 0
                        for ne in negator:
                            ne_match = re.search(ne, ncontent[n][ti-1])
                            if ne_match:
                                print "Negator at ", n, ti-1, ncontent[n][ti-1]
                                control_content *= -2+1
                                content_score += control_content
                                control_content = 0
                else:
                    control_content = 0
        # Content Evaluation
        if content_score > 0:
            content_eval = "positiv"
        elif content_score == 0:
            content_eval = "neutral"
        elif content_score < 0:
            content_eval = "negativ"
        else:
            print "No content_score is given!"
        # Resume
        print "Sentiment Value", content_score
        print ncontent[n], len(ncontent[n]), "Tokens"
        print content_eval
        print "{}{}{}{}".format(time, " - ", n, ".content was analysed\n\n")
        #Insert to collection
        collection[n].insert(len(collection[n]),content_score)
        collection[n].insert(len(collection[n]),content_eval)
        content_score = 0
### Review Evaluation Stars, Title and Content ###
for n in range(len(collection)):
    title_score = collection[n][8]
    content_score = collection[n][10]
    review_stars = collection[n][6]
    #Evaluation
    review_score = title_score + content_score
    if review_score > 0:
        review_eval = "positiv"
    elif review_score == 0:
        review_eval = "neutral"
    elif review_score < 0:
        review_eval = "negativ"
    else:
        print "No review_score is given!"
    #Evaluation review_stars
    if review_stars > 3:
        stars_eval = "positiv"
    elif review_stars == 3:
        stars_eval = "neutral"
    elif review_stars < 3:
        stars_eval = "negativ"
    else:
        print "No review_stars is given!"
    #Insert to collection
    collection[n].insert(len(collection[n]),review_score)
    collection[n].insert(len(collection[n]),review_eval)
    collection[n].insert(len(collection[n]),stars_eval)

### Set collection for MongoDB
col = time
# db[col].insert_many([{'x': i} for i in collection])
db[col].insert_many(
    {
        "_id": i[0],
        'title': i[1],
        'content': i[2],
        'content_lenght': i[3],
        'city': i[4],
        'hotel_name': i[5],
        'review_stars': i[6],
        'helpful_reader': i[7],
        'title_score': i[8],
        'title_eval': i[9],
        'content_score': i[10],
        'content_eval' : i[11],
        'review_score': i[12],
        'review_eval' : i[13],
        'stars_eval' : i[14]
    }
    for i in collection
)
sentieval(collection)
