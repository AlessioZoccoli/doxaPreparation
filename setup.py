import tweepy
from credentials import *


def twitter_setup_AppOnly(wait=False):
    """
    Utility function to setup the Twitter's API
    with app keys provided.
    """

    # Appliation only authentication (you won't be able to search for users)
    # Wider window of requests
    auth = tweepy.AppAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

    ## Return API with authentication:
    api = tweepy.API(auth, wait_on_rate_limit=wait, wait_on_rate_limit_notify=wait)
    return api


def twitter_setup_UserAuth(wait=False):
    """
    Utility function to setup the Twitter's API
    with all our access keys provided.
    """

    ## Authentication and access using keys:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    api = tweepy.API(auth, wait_on_rate_limit=wait, wait_on_rate_limit_notify=wait)
    return api
