# Sentiment Aanalysis on Tripadvisor with Python & NLTK
Export tripadvisor hotel data to mongodb with scrapy, 
remove stopwords, tokenize reviews with nltk and segmenting reviews for a sentiment analysis process and dashboard.

In this project we have the focus on german (Deutsch) language. We want to analyse the sentimentals of hotel reviews in Germany.<br>

At first you can get your needed raw data with python and scrapy framework from tripadvisor with this repository: <br>
https://github.com/monkeylearn/hotel-review-analysis

<hr>

We changed the spider request and did a item change. For a more specific request you must put this command into your terminal. <em>Example:</em>

<kbd>scrapy crawl tripadvisor_more -a start_url="https://www.tripadvisor.de/Hotels-g2049630-Dieburg_Hesse-Hotels.html" -o christian-test.csv </kbd>
<br>

This repository is in progress! If you want to collaborate, please send a <a href="mailto:uenvert90@googlemail.com">e-mail</a>. 
<br>
[![pdf.jpg](https://s24.postimg.org/n2h6riy85/pdf.jpg)](https://postimg.org/image/4a5bny1tt/)
