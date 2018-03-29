from tweepy import RateLimitError
from time import sleep

def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except RateLimitError:
            sleep(15*60)