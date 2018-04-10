from helpers.db.polarityAndCategory import addPolarityToMissingTweet
from pymongo import MongoClient
import config


if __name__ == "__main__":
    client = MongoClient(config.db_clientTopic) #same as topics one now
    usersCollection = client[config.db_users][config.db_collectionUsersTweets]
    topicsCollection = client[config.db_topic][config.db_collection_topic]

    addPolarityToMissingTweet(usersCollection, topicsCollection, 'inTopicCollection')
