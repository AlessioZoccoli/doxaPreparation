import config
from pymongo import MongoClient
from helpers.db.polarityAndCategory import addPolarity

dbClient = MongoClient(config.db_clientTopic)
collection = dbClient[config.db_topic][config.db_collection_topic]

if __name__ == "__main__":
    addPolarity(collection)