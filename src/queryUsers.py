import config
from pymongo import MongoClient
from lib.queries.query import mostActiveUsers
import pprint

dbClient = MongoClient(config.db_client)
collection = dbClient[config.db_name][config.db_collection_name]

dbClient = MongoClient(config.db_client)
collection = dbClient[config.db_name][config.db_collection_name]

if __name__ == "__main__":
    #print(mostActiveUsers(collection, 100))
    pprint.pprint(mostActiveUsers(collection, 0)[:100])