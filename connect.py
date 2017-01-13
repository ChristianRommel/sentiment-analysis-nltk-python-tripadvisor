import pymongo
from pymongo import MongoClient
from datetime import datetime
client = MongoClient('mongodb://localhost:27017/')
db = client.sentimentdb
def sentiment_title(time, db, ntitle, title_id, sentiment_score, sentieval):
    sentiment = "timestamp"
    db.title_sentiment.insert_one(
        {
        "count" : title_id,
        "title": ntitle,
        "time": time,
        "sentiment_score" : sentiment_score,
        "sentieval" : sentieval
        }
    )
    print "data saved"
    return;
# result = db.restaurants.insert_one(
#     {
#         "address": {
#             "street": "2 Avenue",
#             "zipcode": "10075",
#             "building": "1480",
#             "coord": [-73.9557413, 40.7720266]
#         },
#         "borough": "Manhattan",
#         "cuisine": "Italian",
#         "grades": [
#             {
#                 "date": datetime.strptime("2014-10-01", "%Y-%m-%d"),
#                 "grade": "A",
#                 "score": 11
#             },
#             {
#                 "date": datetime.strptime("2014-01-16", "%Y-%m-%d"),
#                 "grade": "B",
#                 "score": 17
#             }
#         ],
#         "name": "Vella",
#         "restaurant_id": "41704620"
#     }
# )

# def printinfo( name, age ):
#    "This prints a passed info into this function"
#    print "Name: ", name
#    print "Age ", age
#    return;
# printinfo ("Christian", 27)
