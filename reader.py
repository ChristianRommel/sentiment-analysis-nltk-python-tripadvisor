import csv
import nltk
import re
from array import *
punct = []
stops = []
ntitle = []
with open('wordlist/punctuation.txt', 'r') as obj1:
	for s in obj1:
		punctuations = s.rstrip()
		punctuations = re.escape(punctuations)
		punctuations = re.compile(punctuations)
		punct.append(punctuations)
with open('wordlist/stopwords.txt', 'r') as obj2:
	for s in obj2:
		#Lowercase words and strip newlines ans whitespaces
		stopwords = s.lower().rstrip()
		stopwords = re.escape(stopwords)
		stopwords = re.compile("{}{}{}".format("\\b", stopwords, "\\b"))
		stops.append(stopwords)
#Open a csv to retrieve the reviews
with open('tripadvisor_dieburg.csv') as file:
	reader = csv.DictReader(file)
	#Get the title and replace the expressions
	for row in reader:
		new_title = row['title'].lower()
		for r in punct:
			# r = re.compile(r)
			new_title = re.sub(r, '', new_title)
		for r in stops:
			#patter = "{}{}{}".format("\\b", r, "\\b")
			#r = re.compile(patter)
			new_title = re.sub(r, '', new_title)
		#Tokenizer
		new_title = nltk.word_tokenize(new_title)
		#Append to the array
		ntitle.append(new_title)
#Print the new title
#print ntitle[0][1]
#re.purge()
