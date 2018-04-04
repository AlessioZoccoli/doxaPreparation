from lib.sentimentAnalysis.sentiment import tweetPolarityOneHot


def addPolarity(coll):
    """
    addPolarity() for each document in collection adds its polarity and category in terms of one hot encoding
    eg. (POSITIVE, NEUTRAL, NEGATIVE) -> (1, 0, 0)
    :return: None
    """
    for doc in coll.find():
        polarity, category = tweetPolarityOneHot(doc['full_text'])

        coll.update_one({"_id": doc["_id"]}, {"$set": {
            "polarity": polarity,
            "positive": category[0],
            "neutral": category[1],
            "negative": category[2]
        }})


def addPolarityToMissingTweet(collUsrs, collTopic, conditionField):
    """
    addPolarityToMissingTweet(usersTweetsDB.tweets, topicTweetsDB, 'inTopicCollection')

    as addPolarity, addPolarityToMissingTweet() for each document in collUsrs previously added to collTopic,
    sets the related polarity and category in terms of one hot encoding

    :param collUsrs: Collection of the users' tweets
    :param collTopic: Collection of tweets for a specific topic, missing tweets are added here
                        and their polarity and category too
    :param conditionField: if this field is present in the document (in collUsrs), add polarity and category (in collTopic9
    :return:
    """

    for doc in collUsrs.find({conditionField: {"$exists": True}}):
        polarity, category = tweetPolarityOneHot(doc['full_text'])

        collTopic.update_one({"_id": doc["_id"]}, {"$set": {
            "polarity": polarity,
            "positive": category[0],
            "neutral": category[1],
            "negative": category[2]
        }})
