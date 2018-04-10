from lib.queries.query import mostActiveUsers, queryTweetsFromUsersList
from pymongo import MongoClient, ASCENDING, errors
import config


if __name__ == "__main__":

    """
        Preparing the DB

    """
    dbClientTweets = MongoClient(config.db_clientTopic)
    dbClientUsers = MongoClient(config.db_clientUsers)

    collectionTweets = dbClientTweets[config.db_topic][config.db_collection_topic]
    collectionUsersTweets = dbClientUsers[config.db_users][config.db_collectionUsersTweets]

    # creating the  indices
    collectionUsersTweets.create_index([('id_str', ASCENDING)], unique=True)

    """
        Querying users of interest    
    
    """

    # calculating the 100 most active users
    # this will also store the list in a new collection so that other functions (e.g. aggregations for SVO) can read it
    selectedUsers = [usr[0] for usr in mostActiveUsers(collectionTweets, 100)]

    collectionSelectedUsers = dbClientUsers[config.db_users][config.db_collectionSelectedNames]
    collectionSelectedUsers.create_index([(config.aggregationFieldShort, ASCENDING)], unique=True)
    collectionSelectedUsers.insert_many([{config.aggregationFieldShort: u} for u in selectedUsers])


    # Twitter API call
    queryTweetsFromUsersList(selectedUsers, 1000, collectionUsersTweets, catchException=errors.DuplicateKeyError)