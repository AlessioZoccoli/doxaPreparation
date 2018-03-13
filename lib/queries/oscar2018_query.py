from pymongo import MongoClient
from lib.queries.query import *




##########################
#                        #
#   MongoDB Connection   #
#                        #
##########################

client = MongoClient('mongodb://localhost:27017')
mydb = client['oscars2018']
coll = mydb['tweets']




##########################
#                        #
#        Query           #
#                        #
##########################

queryOscars = ('#Oscars OR #Oscars2018 OR #Oscars90 OR #Oscar OR #OscarSunday OR #redCarpet OR #Hollywood OR #oscars OR #oscar OR #oscars2018 OR #oscars90 OR #AcademyAwards')

date1 = '2018-03-03'
date2 = '2018-03-04'
date3 = '2018-03-05'
date4 = '2018-03-06'

# Querying and storing data in mongo
# queryString, sinceDate, untilDate, mongoCollection, language='en'
#  ====>  query2TopicDates(queryOscars, date3, date4, coll)

