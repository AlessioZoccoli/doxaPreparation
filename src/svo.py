import config
from pymongo import MongoClient
from helpers.db.aggregations import groupByConditional, groupBySentimentsInList

if __name__ == "__main__":

    client = MongoClient(config.db_clientTopic)

    topicTweetsCollection = client[config.db_nameTopic][config.db_collection_nameTopic]
    usersTweetsCollection = client[config.db_nameUsers][config.db_collectionUsersTweets]
    selectedUsersCollection = client[config.db_nameUsers][config.db_collectionUsersSVO]


    # counting tweets not related to the topic
    unrelatedTweetsPipeline = groupByConditional(config.aggregationField, config.filterField)
    unrelatedTweets = usersTweetsCollection.aggregate(unrelatedTweetsPipeline)

    selectedUsers = [user[config.aggregationFieldShort]for user in selectedUsersCollection.find()]

    # counting tweets related to the topic by sentiment category and
    relatedTweetsPipeline = groupBySentimentsInList(config.aggregationField, selectedUsers)
    relatedTweets = topicTweetsCollection.aggregate(relatedTweetsPipeline)

