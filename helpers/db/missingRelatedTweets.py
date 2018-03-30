

def missingRelatedTweets(collUsrs, collTopics, catchException, terms):

    for tweet in collUsrs.find():
        if len({hashtag['text'] for hashtag in tweet['entities']['hashtags']} & terms) > 0:
            collUsrs.update_one({"_id": tweet["_id"]}, {"$set": {
                "inTopicCollection": 1
            }})
            try:
                collTopics.insert_one(tweet)
            except catchException:
                pass


#print({hashtag['text'] for hashtag in tweet['entities']['hashtags']})
#s = {hashtag['text'] for hashtag in tweet['entities']['hashtags']} & terms
#print(len(s))
