import tweepy
from credentials import *


def twitter_setup_AppOnly():
    """
    Utility function to setup the Twitter's API
    with app keys provided.
    """

    # Appliation only authentication (you won't be able to search for users)
    # Wider window of requests
    auth = tweepy.AppAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

    ## Return API with authentication:
    api = tweepy.API(auth)
    return api


def twitter_setup_UserAuth():
    """
    Utility function to setup the Twitter's API
    with all our access keys provided.
    """

    ## Authentication and access using keys:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    api = tweepy.API(auth)
    return api
