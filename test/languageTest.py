import config
from pymongo import MongoClient
from bson import json_util
from lib.language.languageProcessing import *


dbClient = MongoClient(config.db_clientTopic)
collection = dbClient[config.db_topic][config.db_collection_topic]

cooccurrenceMat = {'CooccurrenceMatrix': cooccurrenceMatrix(collection.find())}

with open('../cooccurrenceMatrix.txt', 'a') as the_file:
    the_file.write(json_util.dumps(cooccurrenceMat))