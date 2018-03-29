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
    collectionUsers = dbClientUsers[config.db_nameUsers][config.db_collectionUsers]

    # creates the  index
    collectionUsers.create_index([('id_str', ASCENDING)], unique=True)
    print("indeces: ", sorted(list(collectionUsers.index_information())), "\n")

    selectedUsers = [usr[0] for usr in mostActiveUsers(collectionTweets, 100)]

    #Querying note: max nTweets = 3200
    queryTweetsFromUsersList(selectedUsers, 1000, collectionUsers, catchException=errors.DuplicateKeyError)