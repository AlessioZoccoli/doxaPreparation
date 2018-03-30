import config
from pymongo import MongoClient
from lib.queries.query import aggregateByNumOfTweets

if __name__ == "__main__":
    dbClient = MongoClient(config.db_clientTopic)
    collection = dbClient[config.db_nameTopic][config.db_collection_nameTopic]

    dbClient = MongoClient(config.db_clientTopic)
    collection = dbClient[config.db_nameTopic][config.db_collection_nameTopic]


    print(aggregateByNumOfTweets(collection, 50))
