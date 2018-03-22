from pymongo import MongoClient
import config
from lib.sentimentAnalysis.sentiment import tweetPolarityOneHot



dbClient = MongoClient(config.db_client)
collection = dbClient[config.db_name][config.db_collection_name]


def addPolarity():
    """
    addPolarity() for each document in collection adds its polarity and category in terms of one hot encoding
    eg. (POSITIVE, NEUTRAL, NEGATIVE) -> (1, 0, 0)
    :return: None
    """
    for doc in collection.find():
        polarity, category = tweetPolarityOneHot(doc['text'])

        collection.update_one({"_id": doc["_id"]}, {"$set": {
            "polarity": polarity,
            "positive": category[0],
            "neutral": category[1],
            "negative": category[2]
        }})


