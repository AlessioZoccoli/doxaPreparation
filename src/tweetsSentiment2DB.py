import config
from pymongo import MongoClient
from lib.sentimentAnalysis.sentiment import tweetPolarityOneHot



dbClient = MongoClient(config.db_clientTopic)
collection = dbClient[config.db_nameTopic][config.db_collection_nameTopic]

def addPolarity(coll):
    """
    addPolarity() for each document in collection adds its polarity and category in terms of one hot encoding
    eg. (POSITIVE, NEUTRAL, NEGATIVE) -> (1, 0, 0)
    :return: None
    """
    for doc in coll.find():
        polarity, category = tweetPolarityOneHot(doc['full_text'])

        coll.update_one({"_id": doc["_id"]}, {"$set": {
            "polarity": polarity,
            "positive": category[0],
            "neutral": category[1],
            "negative": category[2]
        }})


if __name__ == "__main__":
    addPolarity(collection)