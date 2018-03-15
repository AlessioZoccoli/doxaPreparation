from pymongo import MongoClient
import config
from lib.sentimentAnalysis.sentiment import tweetPolarityOneHot

##########################
#                        #
#   MongoDB Connection   #
#                        #
##########################

dbClient = MongoClient(config.db_client)
collection = dbClient[config.db_name][config.db_collection_name]



for doc in collection.find():
    polarity, category = tweetPolarityOneHot(doc['text'])

    collection.update_one({"_id": doc["_id"]}, {"$set": {
        "polarity": polarity,
        "positive": category[0],
        "neutral": category[1],
        "negative": category[2]
    }})