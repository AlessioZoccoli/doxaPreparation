from pymongo import MongoClient
from helpers.db.hashtags import getId2Hashtags
import config
from pprint import pprint


if __name__ == "__main__":

    client = MongoClient(config.db_clientUsers)
    collection = client[config.db_nameUsers][config.db_collectionUsers]
    pprint(getId2Hashtags(collection.find()))