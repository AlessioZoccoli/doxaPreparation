from setup import *

"""
           Query string                                                
                                                                        
   Collecting trending hashtags from                                    
   http://hashtagify.me/hashtag/<inputHashtag>                          
   It shows some basic stats about hashtags and some related hashtags   
                                                                        
   es. http://hashtagify.me/hashtag/oscars2018                          
   http://hashtagify.me/hashtag/oscars90  
   
   See https://www.hashtags.org/ too                             
                                                                        

"""


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

    api = twitter_setup_AppOnly()

    for tweet in tweepy.Cursor(api.search, q=queryString, tweet_mode='extended', count=100, lan=language, since=sinceDate,
                               until=untilDate).items():
        if tweet.lang == language:
            mongoCollection.insert_one(tweet._json)

    print('{:d} counted'.format(mongoCollection.count()))


"""
    Given a hashtag this site will give 
    https://www.hashtags.org/
    related topics and most prolific users!

"""


def queryUserTweets(screenName, nTweets, mongoCollection, language='en'):
    """
    Querying twitter by specifying user's screen_name

    :param screenName: screen_name of the user's tweet
    :param nTweets: passed as count parameter to Cursor, max = 200
    :param mongoCollection: mongoDB collection
    :param language: language, default 'en'
    :return: None
    """

    if nTweets > 200:
        nTweets = 200

    api = twitter_setup_AppOnly()
    for tweet in tweepy.Cursor(api.user_timeline, screen_name=screenName, tweet_mode='extended', count=nTweets, show_user=True).items():
        if tweet.lang == language:
            mongoCollection.insert_one(tweet._json)

    print('{:d} counted'.format(mongoCollection.count()))
