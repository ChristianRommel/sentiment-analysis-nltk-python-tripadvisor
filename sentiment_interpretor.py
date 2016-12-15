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
        w.rstrip()
        poswords.append(w)
with open ('wordlist/negativ.txt', 'r') as obj2:
    for w in obj2:
        w.rstrip()
        negwords.append(w)
with open ('wordlist/negator.txt', 'r') as obj3:
    for w in obj3:
        w.rstrip()
        negator.append(w)
with open ('wordlist/increaser.txt', 'r') as obj4:
    for w in obj4:
        w.rstrip()
        increaser.append(w)
#set score variables
sentiment_score = 0
control = 0
for n in range(len(ntitle)):
	print n
	for t in ntitle[n]:
		print t
