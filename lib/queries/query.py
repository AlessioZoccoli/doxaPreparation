from setup import *
from collections import Counter, defaultdict
from helpers.rateLimitations import limit_handled


"""
           Query string                                                
                                                                        
   Collecting trending hashtags from                                    
   http://hashtagify.me/hashtag/<inputHashtag>                          
   It shows some basic stats about hashtags and some related hashtags   
                                                                        
   es. http://hashtagify.me/hashtag/oscars2018                          
   http://hashtagify.me/hashtag/oscars90  
   
   See https://www.hashtags.org/ too                             
                                                                        

"""


def queryTopic(queryString, sinceDate, untilDate, mongoCollection, catchException, language='en'):
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
            try:
                mongoCollection.insert_one(tweet._json)
            except catchException:
                pass

    print('{:d} total counted'.format(mongoCollection.count()))


"""
    Given a hashtag this site will give 
    https://www.hashtags.org/
    related topics and most prolific users!

"""


def queryUserTweets(screenName, nTweets, mongoCollection, catchException, api, language='en'):
    """
    Querying twitter by specifying user's screen_name

    :param screenName: screen_name of the user's tweet
    :param nTweets: passed as count parameter to Cursor, max = 200
    :param mongoCollection: mongoDB collection
    :param catchException: errors due to the index/ces
    :param language: language, default 'en'
    :return: None
    """

    for tweet in tweepy.Cursor(api.user_timeline, screen_name=screenName, tweet_mode='extended', count=200, show_user=True).items(nTweets):
        if tweet.lang == language:
            try:
                mongoCollection.insert_one(tweet._json)
            except catchException:
                pass

    print('{:d} total counted'.format(mongoCollection.count()))


def queryTweetsFromUsersList(users, nTweets, mongoCollection, catchException, language='en'):
    """

    :param users: Set of users by their screen_name
    :param nTweets: passed as count parameter to Cursor, max = 200
    :param mongoCollection: mongoDB collection (destination)
    :param catchException: errors due to the index/ces
    :param language: language, default 'en'
    :return: None
    """
    api = twitter_setup_UserAuth(wait=True)

    print(len(users))

    for user in users:
        cursor = limit_handled(tweepy.Cursor(api.user_timeline, screen_name=user, tweet_mode='extended', count=200, show_user=True).items(nTweets))
        for tweet in cursor:
            if tweet.lang == language:
                try:
                    mongoCollection.insert_one(tweet._json)
                except catchException:
                    pass



"""

    Some other useful functions to Analyize users

"""


def getNRandomUsers(n, coll):
    """
     getting N random users

    getNRandomUsers(100, db.myColl)
    :param n: number of users
    :param coll: db collection
    :return: list of screen_names associated with users
    """

    randDocs = coll.aggregate([{"$sample": {"size": n}}])
    randUsers = set([doc["user"]["screen_name"] for doc in randDocs])

    _counter = len(randUsers)

    while _counter < n:
        moreDocs = coll.aggregate([{"$sample": {"size": n - _counter}}])
        moreUsers = set([doc["user"]["screen_name"] for doc in moreDocs])
        _counter = len(moreUsers)
        print(_counter)
        randUsers.update(moreUsers)

    return randUsers


def getAllUsers(coll):
    """
    getting every users
    :param coll: db collection
    :return: set of all users's screen_names
    """
    return set([user['user']['screen_name'] for user in coll.find({}, {"user.screen_name": True})])


def mostActiveUsers(coll, n):
    """
    getting the most active users (by number of tweets)
    :param coll: db collection
    :param n: number of users
    :return: tuple (user, nTweets)
    """
    _count = Counter()
    _count.update([user['user']['screen_name'] for user in coll.find({}, {"user.screen_name": True})])

    if n > 0:
        mCommons = _count.most_common(n)
    else:
        mCommons = _count.most_common()
    return mCommons


def aggregateByNumOfTweets(coll, n):
    """

    aggregateByNumOfTweets(mongoCollection, 100): agregates 100 most actives users by number of tweets, descending order.


    :param coll: db collection
    :param n: number of users
    :return: tuple (nOfTweets, nOfUsers)
    """

    # new dictionary keys
    nOfTweets = defaultdict(list)
    users2nTweets = mostActiveUsers(coll, n)

    for usr, ntweets in users2nTweets:
        nOfTweets[ntweets].append(usr)

    return {key: len(value) for key,value in nOfTweets.items()}


