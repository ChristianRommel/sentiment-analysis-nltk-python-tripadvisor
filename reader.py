import csv 
import nltk
import re
from array import *
punct = []
stops = []
ntitle = []
obj1 = open('punctuations.txt', 'r')
for s in obj1:
	#Lowercase words and strip newlines ans whitespaces
	punctuations = s.rstrip()
	punctuations = re.escape(punctuations)
	punct.append(punctuations)
obj1.close
obj2 = open('stopwords.txt', 'r')
for s in obj1:
	#Lowercase words and strip newlines ans whitespaces
	stopwords = s.lower().rstrip()
	stopwords = re.escape(stopwords)
	stops.append(stopwords)
obj2.close



#Expressions
#rgx_list = ['\.', ',', ';', '\(', '\)', ':', '\.\.\.', '!']
#Open a csv
with open('tripadvisor_dieburg.csv') as file: 	
	reader = csv.DictReader(file)
	#Get the title and replace the expressions	
	for row in reader:
		new_title = row['title'].lower()
		for r in punct:
			rgx = re.compile(r)
			new_title = re.sub(rgx, '', new_title)
		for r in stops:
			patter = "{}{}{}".format("\\b", r, "\\b")
			rgx = re.compile(patter)
			new_title = re.sub(rgx, '', new_title)
		#Tokenizer
		nltk.word_tokenize(new_title)	
		#Append to the array	
		ntitle.append(new_title)			
#Print the new title
for n in ntitle:
	print n