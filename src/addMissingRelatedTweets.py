from pymongo import MongoClient, errors

from helpers.db.missingRelatedTweets import missingRelatedTweets
import config


if __name__ == "__main__":
    client = MongoClient(config.db_clientTopic) #same as topics one now
    usersCollection = client[config.db_nameUsers][config.db_collectionUsers]
    topicsCollection = client[config.db_nameTopic][config.db_collection_nameTopic]

    missingRelatedTweets(usersCollection, topicsCollection,
                         errors.DuplicateKeyError, config.relatedTerms_fbCambridgeAnalytica)
