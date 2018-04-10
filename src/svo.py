import config
from pymongo import MongoClient
from pymongo.errors import BulkWriteError
from helpers.db.aggregations import groupByConditional, calculateSentimentObjectivity, calculateVolume, \
    addVolume2Missings
from pprint import pprint

if __name__ == "__main__":

    """
    
        DB setup
    
    """

    client = MongoClient(config.db_clientTopic)

    # topic related tweets
    topicTweetsCollection = client[config.db_topic][config.db_collection_topic]

    # tweets by the most actives
    usersTweetsCollection = client[config.db_users][config.db_collectionUsersTweets]

    # user to SVO attributes coll
    #
    #       NOTE: config.db_collectionUsersSVO is parameter of '$out' in calculateSentimentObjectivity
    #       e.g.
    # NOT the entire collection
    svoCollection = client[config.db_users][config.db_collectionUsersSVO]

    # most actives, see usersTweets
    selectedNamesCollection = client[config.db_users][config.db_collectionSelectedNames]


    """
    
        Counting storing SVO metrics
    
    """

    # counting tweets not related to the topic
    unrelatedTweetsPipeline = groupByConditional(config.aggregationField, config.filteringField)
    unrelatedTweets = usersTweetsCollection.aggregate(unrelatedTweetsPipeline)


    # counting tweets related to the topic by sentiment category, Sentiment, Objectivity and number of tweets
    # is built so that it writes out the result in svoCollection
    selectedUsers = [u[config.aggregationFieldShort] for u in selectedNamesCollection.find()]
    relatedTweetsPipeline = calculateSentimentObjectivity(config.aggregationField, selectedUsers, config.db_collectionUsersSVO)
    # relatedTweets is stored in svoCollection
    relatedTweets = topicTweetsCollection.aggregate(relatedTweetsPipeline)


    # calculating and adding Volume to config.db_collectionUsersSVO
    volumeUpdates = calculateVolume(unrelatedTweets, svoCollection)
    volumeUpdatesMissings = addVolume2Missings(svoCollection)
    volumeUpdates.extend(volumeUpdatesMissings)

    try:
        svoCollection.bulk_write(volumeUpdates, ordered=False)
    except BulkWriteError as bwe:
        pprint(bwe)

