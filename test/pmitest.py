from lib.language.languageProcessing import *
from pymongo import MongoClient
import config



dbClient = MongoClient(config.db_clientTopic)
collection = dbClient[config.db_nameTopic][config.db_collection_nameTopic]

positive_vocab = [
    'good', 'nice', 'great', 'awesome', 'outstanding',
    'fantastic', 'terrific', ':)', ':-)', 'like', 'love',
    # shall we also include game-specific terms?
    # 'triumph', 'triumphal', 'triumphant', 'victory', etc.
]
negative_vocab = [
    'bad', 'terrible', 'crap', 'useless', 'hate', ':(', ':-(',
    # 'defeat', etc.
]


myTweets =  collection.find().limit(5)


myMostComTersm = mostCommonTerms(myTweets,0)
print("###### myMostComTersm ######")
print(myMostComTersm)

coMat = cooccurrenceMatrix(myTweets)
print("###### cooccurrences matrix ######")
print(coMat)

myPmi = pmi(myMostComTersm.items(), coMat, 10, positive_vocab, negative_vocab)
print("###### pmi ######")
print(myPmi)
