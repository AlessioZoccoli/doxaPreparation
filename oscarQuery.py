from twitterscraper import query_tweets
from pymongo import MongoClient
import datetime as dt
from bson import json_util

client = MongoClient('mongodb://localhost:27017')
#tweetsDB = client['tweetsDB']


##############################
#                            #
#      Oscar night 2018      #
#                            #
##############################


# Collection
oscar2018 = client['tweetsDB']['oscar2018']

# Query string
queryString = "Oscar2018 OR Oscar OR Oscars OR redcarpet OR Oscars90 OR oscar2018 OR oscar OR oscars OR redcarpet OR oscars90 OR AcademyAwards OR academyawards OR theshapeofwater OR cine"



"""
   SCRAPING             https://github.com/taspinar/twitterscraper
   ENGAGEMENT           http://keyhole.co/preview
   SIMILAR HASHTAGS     http://hashtagify.me/hashtag/oscar



limit to 500 tweets, from March 1st to 9th. Poolsize max value = daysInterval/2


for tweet,i in zip(query_tweets(queryString, limit = 500, begindate = dt.date(2018,3,1), enddate = dt.date.today(), poolsize=4, lang='en'), range(0,500)):
    int2tweet = {i: json_util.loads(tweet.encode('utf-8)}
    oscar2018.insert_one(int2tweet)
"""

file = open("/Users/alessio/tesiMagistrale/doxa/output.txt","w")
for tweet in query_tweets(query_tweets("Trump OR Clinton", limit = 10, begindate = dt.date(2018,3,1), enddate = dt.date.today(), poolsize=4, lang='en'), 10):
    file.write(tweet.encode('utf-8'))
file.close()