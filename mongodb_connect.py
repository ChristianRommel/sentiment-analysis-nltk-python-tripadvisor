import pymongo
from pymongo.errors import ConnectionFailure
from pymongo import MongoClient
#Connection to MongoDB
try:
    client = MongoClient('mongodb://localhost:27017/')
except ConnectionFailure:
    print("Server not available")
db = client.sentimentdb
