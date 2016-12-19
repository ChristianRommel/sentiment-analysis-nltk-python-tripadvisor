import re
from array import *
import reader
#set the array for the interpretor
ntitle = reader.ntitle
#set the wordlists and save them to a new list
poswords = []
negwords = []
negator = []
increaser = []
with open ('wordlist/positiv.txt', 'r') as obj1:
    for w in obj1:
        pos = w.lower().rstrip()
        pos = re.escape(pos)
        pos = re.compile(pos)
        poswords.append(pos)
with open ('wordlist/negativ.txt', 'r') as obj2:
    for w in obj2:
        neg = w.lower().rstrip()
        neg = re.escape(neg)
        neg = re.compile(neg)
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
sentiment_score = 0
control = 0
for n in range(len(ntitle)):
    	for t in ntitle[n]:
            ti = ntitle[n].index(t)
            #Check the positiv words
            for p in poswords:
                match = re.search(p, t)
                if match:
                    print match.group(), 'positiv word found on position', n, ti
                    # print ntitle[n][ti]
            #Check the negativ words
            for nw in negwords:
                match = re.search(nw, t)
                if match:
                    print match.group(), 'negativ word found on position', n, ti
                    # print ntitle[n][ti]
        print "{}{}".format(n, ".title was analysed\n\n")
