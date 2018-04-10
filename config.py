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
db_name_oscars2018 = 'oscars2018'
db_collection_oscars2018 = 'tweets'

"""



    Facebook and Cambridge Analytica, March 2018




"""

# Query
fbCambridgeAnalytica1 = '#CambridgeAnalytica OR #cambridgeanalytica OR #Trump OR #trump OR  #Facebook OR #facebook OR #Mercer OR #Bannon OR #stevebannon OR #privacy Or #Zuckemberg OR #zuckemberg OR #Facebookgate OR #facebookgate OR #putin OR #Putin OR #brexit OR #Brexit OR #cambridgeanalyticauncovered OR #trumprussia'
fbCambridgeAnalytica2 = '#CambridgeAnalytica OR #cambridgeanalytica OR #facebook OR #Facebook'

relatedTerms_fbCambridgeAnalytica = {"CambridgeAnalytica", "CambridgeAnalyticaUncovered", "CambridgeAnalytics",
                                     "zuckerberg", "Zuckerberg", "Facebook", "facebook", "deleteFacebook",
                                     "deletefacebook", "DeleteFacebook", "facebookdown", "FacebookDataBreach",
                                     "MarkZuckerberg", "markzuckemberg"}

fbCaDates = ['2018-03-19', '2018-03-20', '2018-03-21', '2018-03-22', '2018-03-23', '2018-03-24', '2018-03-25',
             '2018-03-26', '2018-03-27']

# DB
client_mongo_uri_fbCA = 'mongodb://localhost:27017'
db_name_fbCA = 'fbCambridgeanalytica'
db_collection_fbCA2 = 'tweets'

#############################################################################
#                                                                           #
#       Users  who tweetted about Facebook and Cambridge Analytica          #
#                                                                           #
#############################################################################

client_mongo_uri_UsersFbCA = client_mongo_uri_fbCA
db_usersTweetFbCa = db_name_fbCA
db_collection_UsersFbCaTweets = 'users100Tweets'  # tweets from 100 selected users
db_collection_usersFbCaSVO = 'users100SVO'  # these 100 users and SVO attributes

#######################
#                     #
#       Edit          #
#       Settings      #
#                     #
#######################

db_clientTopic = client_mongo_uri_fbCA
db_topic = db_name_fbCA
db_collection_topic = db_collection_fbCA2

topicQuery = fbCambridgeAnalytica2
sinceDateTopic = fbCaDates[7]
untilDateTopic = fbCaDates[8]

db_clientUsers = client_mongo_uri_UsersFbCA
db_users = db_usersTweetFbCa
db_collectionUsersTweets = db_collection_UsersFbCaTweets
db_collectionUsersSVO = db_collection_usersFbCaSVO

###############
# Aggregation #
###############
aggregationField = "$user.screen_name"
aggregationFieldShort = "screen_name"
filteringField = "inTopicCollection"
db_collectionSelectedNames = 'selectedUsers'
