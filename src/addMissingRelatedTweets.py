from pymongo import MongoClient, errors

from helpers.db.missingRelatedTweets import missingRelatedTweets
import config


if __name__ == "__main__":
    client = MongoClient(config.db_clientTopic)
    usersCollection = client[config.db_users][config.db_collectionUsersTweets]
    topicsCollection = client[config.db_topic][config.db_collection_topic]

    missingRelatedTweets(usersCollection, topicsCollection,
                         errors.DuplicateKeyError, config.relatedTerms_fbCambridgeAnalytica)
