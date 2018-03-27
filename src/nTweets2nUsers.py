import config
from pymongo import MongoClient
from lib.queries.query import aggregateByNumOfTweets


dbClient = MongoClient(config.db_client)
collection = dbClient[config.db_name][config.db_collection_name]

dbClient = MongoClient(config.db_client)
collection = dbClient[config.db_name][config.db_collection_name]


print(aggregateByNumOfTweets(collection, 50))
