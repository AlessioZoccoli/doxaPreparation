from setup import *


##########################################################################
#            Query string                                                #
#                                                                        #
#   Collecting trending hashtags from                                    #
#   http://hashtagify.me/hashtag/<inputHashtag>                          #
#   It shows some basic stats about hashtags and some related hashtags   #
#                                                                        #
#   es. http://hashtagify.me/hashtag/oscars2018                          #
#   http://hashtagify.me/hashtag/oscars90                                #
#                                                                        #
##########################################################################


def queryTopic(queryString, sinceDate, untilDate, mongoCollection, language='en'):
    """

    Querying twitter by specifying hashtags (related to the topic)

    :param queryString: String. Terms (es. hashtag) of interest
    :param sinceDate: String. Twitted not before this date
    :param untilDate: String. Twitted not on this date or after
    :param mongoCollection: MongoDB collection. Tweets will be added here.
    :param language: default "en". If condition still necessary
    :return: None
    """

    # Calling the right APIs
    api = twitter_setup_AppOnly()

    for tweet in tweepy.Cursor(api.search, q=queryString, count=100, lan=language, since=sinceDate, until=untilDate).items():
        if(tweet.lang == "en"):
            mongoCollection.insert_one(tweet._json)

    print('{:d} counted'.format(mongoCollection.count()))


def queryUserTweets(screenName, nTweets, sinceDate, untilDate, mongoCollection, language='en'):
    """
    Querying twitter by specifying user's screen_name. Screen name

    :param screenName:
    :param nTweets:
    :param sinceDate:
    :param untilDate:
    :param mongoCollection:
    :param language:
    :return:
    """