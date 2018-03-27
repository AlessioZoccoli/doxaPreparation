from pymongo import MongoClient, ASCENDING, errors
import config
from lib.queries.query import *
from time import localtime, strftime


"""
    Preparing the DB

"""
dbClient = MongoClient(config.db_client)
collection = dbClient[config.db_name][config.db_collection_name]

# creates the  index
collection.create_index([('id_str', ASCENDING)], unique=True)
print("indeces: ", sorted(list(collection.index_information())), "\n")


"""
    Dates to query
"""
queryString = config.topicQuery
dateUntil = config.untilDateTopic
dateSince = config.sinceDateTopic


print(dbClient, collection, queryString, dateSince, dateUntil)
print("runned at ", strftime("%Y-%m-%d %H:%M:%S", localtime()))

# Querying and storing data in mongo
# queryString, sinceDate, untilDate, mongoCollection, language='en'

if __name__ == "__main__":
    queryTopic(queryString, dateSince, dateUntil, collection, errors.DuplicateKeyError)

