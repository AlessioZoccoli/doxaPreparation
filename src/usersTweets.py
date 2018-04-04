from lib.queries.query import mostActiveUsers, queryTweetsFromUsersList
from pymongo import MongoClient, ASCENDING, errors
import config


if __name__ == "__main__":

    """
        Preparing the DB

    """
    dbClientTweets = MongoClient(config.db_clientTopic)
    dbClientUsers = MongoClient(config.db_clientUsers)

    collectionTweets = dbClientTweets[config.db_nameTopic][config.db_collection_nameTopic]
    collectionUsersTweets = dbClientUsers[config.db_nameUsers][config.db_collectionUsersTweets]
    # users screen_name and useful info to calculate SVO
    collectionUsers = dbClientUsers[config.db_nameUsers][config.db_collectionUsersSVO]


    # creates the  indices
    collectionUsersTweets.create_index([('id_str', ASCENDING)], unique=True)
    collectionUsers.create_index([('screen_name', ASCENDING)], unique=True)


    """
        Querying users of interest    
    
    """

    # calculating the 100 most active users
    selectedUsers = [usr[0] for usr in mostActiveUsers(collectionTweets, 100)]

    # creating a collection for these users (for SVO)
    collectionUsers.insert_many([{'screen_name': u} for u in selectedUsers])

    # Querying note: max nTweets = 3200
    queryTweetsFromUsersList(selectedUsers, 1000, collectionUsersTweets, catchException=errors.DuplicateKeyError)