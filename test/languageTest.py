import config
from pymongo import MongoClient
from bson import json_util
from lib.language.languageProcessing import *


dbClient = MongoClient(config.db_client)
collection = dbClient[config.db_name][config.db_collection_name]

cooccurrenceMat = {'CooccurrenceMatrix': cooccurrenceMatrix(collection.find())}

with open('../cooccurrenceMatrix.txt', 'a') as the_file:
    the_file.write(json_util.dumps(cooccurrenceMat))