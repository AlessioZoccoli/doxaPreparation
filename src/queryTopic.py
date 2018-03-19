from pymongo import MongoClient
import config
from lib.queries.query import *




##########################
#                        #
#   MongoDB Connection   #
#                        #
##########################

dbClient = MongoClient(config.db_client)
collection = dbClient[config.db_name][config.db_collection_name]


##########################
#                        #
#        Query           #
#                        #
##########################

"""
    Dates to query
"""
queryString = config.topicQuery
dateUntil = config.untilDateTopic
dateSince = config.sinceDateTopic



# Querying and storing data in mongo
# queryString, sinceDate, untilDate, mongoCollection, language='en'
query2TopicDates(queryString, dateSince , dateUntil, collection)
