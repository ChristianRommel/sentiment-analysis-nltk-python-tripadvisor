import csv
import nltk
import re
from array import *
punct = []
stops = []
ntitle = []
ncontent= []
collection = []
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
		review_stars = row['review_stars'].split("von")[0]
		new_title = row['title'].lower()
		new_content = row['content'].lower()
		#print new_title
		for r in punct:
			# r = re.compile(r)
			new_title = re.sub(r, '', new_title)
			new_content = re.sub(r, '', new_content)
		for r in stops:
			#patter = "{}{}{}".format("\\b", r, "\\b")
			#r = re.compile(patter)
			new_title = re.sub(r, '', new_title)
			new_content = re.sub(r, '', new_content)
		#Tokenizer
		new_title = nltk.word_tokenize(new_title)
		new_content = nltk.word_tokenize(new_content)
		#Append to the array
		ntitle.append(new_title)
		ncontent.append(new_content)
		collection.append(
		[
			row['title'],
			row['content'],
			row['city'],
			row['hotel_name'],
			review_stars
		])
#Print the new title
#print ntitle
# print ntitle[0][1]
#print ncontent
#re.purge()
#print collection
# print collection[0][4]
