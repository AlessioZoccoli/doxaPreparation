import config
from pymongo import MongoClient
from lib.queries.query import aggregateByNumOfTweets

if __name__ == "__main__":
    dbClient = MongoClient(config.db_clientTopic)
    collection = dbClient[config.db_topic][config.db_collection_topic]

    dbClient = MongoClient(config.db_clientTopic)
    collection = dbClient[config.db_topic][config.db_collection_topic]


    print(aggregateByNumOfTweets(collection, 50))
