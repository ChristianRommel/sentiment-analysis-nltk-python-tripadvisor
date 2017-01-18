import pymongo
from pymongo.errors import ConnectionFailure
from pymongo import MongoClient
#Connection to MongoDB
try:
    client = MongoClient('mongodb://localhost:27017/')
except ConnectionFailure:
    print("Server not available")
db = client.sentimentdb
###--Example--###
# def sentiment_title(time, db, ntitle, title_id, sentiment_score, sentieval):
#     sentiment = "timestamp"
#     db.title_sentiment.insert_one(
#         {
#         "count" : title_id,
#         "title": ntitle,
#         "time": time,
#         "sentiment_score" : sentiment_score,
#         "sentieval" : sentieval
#         }
#     )
#     print "data saved"
#     return;
