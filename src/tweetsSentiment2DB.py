import config
from pymongo import MongoClient
from helpers.db.polarityAndCategory import addPolarity

dbClient = MongoClient(config.db_clientTopic)
collection = dbClient[config.db_nameTopic][config.db_collection_nameTopic]

if __name__ == "__main__":
    addPolarity(collection)