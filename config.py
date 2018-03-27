
#######################
#                     #
#       Topics        #
#       Here          #
#                     #
# hashtagify.com      #
# hashtags.org        #
#######################

"""



    Oscars 2018



"""


# Query
oscars2018 = '#Oscars OR #Oscars2018 OR #Oscars90 OR #Oscar OR #OscarSunday OR #redCarpet OR #Hollywood OR #oscars OR #oscar OR #oscars2018 OR #oscars90 OR #AcademyAwards'

oscars2018_date1 = '2018-03-03'
oscars2018_date2 = '2018-03-04'
oscars2018_date3 = '2018-03-05'
oscars2018_date4 = '2018-03-06'

# DB
client_mongo_uri_oscars2018 = 'mongodb://localhost:27017'
db_name_oscars2018 = 'test-database-1'
db_collection_oscars2018 = 'tweets'


"""



    Facebook and Cambridge Analytica, March 2018




"""

#Query
fbCambridgeAnalytica1 = '#CambridgeAnalytica OR #cambridgeanalytica OR #Trump OR #trump OR  #Facebook OR #facebook OR #Mercer OR #Bannon OR #stevebannon OR #privacy Or #Zuckemberg OR #zuckemberg OR #Facebookgate OR #facebookgate OR #putin OR #Putin OR #brexit OR #Brexit OR #cambridgeanalyticauncovered OR #trumprussia'
fbCambridgeAnalytica2 = '#CambridgeAnalytica OR #cambridgeanalytica OR #facebook OR #Facebook'

#fbCA_date1 = '2018-03-19'
#fbCA_date2 = '2018-03-20'
#fbCA_date3 = '2018-03-21'
#fbCA_date4 = '2018-03-22'
#fbCA_date5 = '2018-03-23'
#fbCA_date6 = '2018-03-24'
#fbCA_date7 = '2018-03-25'
#fbCA_date7 = '2018-03-26'

fbCaDates = ['2018-03-19', '2018-03-20', '2018-03-21', '2018-03-22', '2018-03-23', '2018-03-24', '2018-03-25', '2018-03-26', '2018-03-27']

# DB
client_mongo_uri_fbCA = 'mongodb://localhost:27017'
db_name_fbCA = 'fbCambridgenalytica'
db_collection_fbCA2 = 'tweets'


#######################
#                     #
#       Edit          #
#       Settings      #
#                     #
#######################

db_client = client_mongo_uri_fbCA
db_name = db_name_fbCA
db_collection_name = db_collection_fbCA2

topicQuery = fbCambridgeAnalytica2
sinceDateTopic = fbCaDates[7]
untilDateTopic = fbCaDates[8]