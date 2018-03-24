from pymongo import MongoClient
from collections import Counter, defaultdict
import config


dbClient = MongoClient(config.db_client)
collection = dbClient[config.db_name][config.db_collection_name]

# Remember to add the index !
# collection.create_index([('id_str', ASCENDING)], unique=True)

def getNRandomUsers(n, coll):
    """
     getting N random users

    getNRandomUsers(100, db.myColl)
    :param n: number of users
    :param coll: db collection
    :return: list of screen_names associated with users
    """

    randDocs = coll.aggregate([{"$sample": {"size": n}}])
    randUsers = set([doc["user"]["screen_name"] for doc in randDocs])

    _counter = len(randUsers)

    while _counter < n:
        moreDocs = coll.aggregate([{"$sample": {"size": n - _counter}}])
        moreUsers = set([doc["user"]["screen_name"] for doc in moreDocs])
        _counter = len(moreUsers)
        print(_counter)
        randUsers.update(moreUsers)

    return randUsers


"""

print(getNRandomUsers(100, collection))

{'pytfenty', 'Jakob20877831', 'qwertyhatezthis', 'lordevibez', 'Corporate_Buyer', 'WhoWhatWearAU', 'KevRique', 'xSaany1', 
'spidey5231', 'JeskEyre', 'eve20_y', 'jamiescottsmith', 'natural_beauT', 'irenelasagna', 'Ibstar01', 'milaninitaly', 
'mug_noodle', 'J_Cquea', 'AndresB_films', 'theywillbefree', 'rajivronald', 'ho_dameron', 'therealsuzn', 'Leppycole',
 'LurieforHouston', 'youngjaerui', 'KariSkelton', 'LibSniper4Trump', 'wtfRAEKEN', 'femysoko', 'Iboromam', 'sandrbullok',
  'slimehateclub', 'guysmiley22', 'mehindaa', 'jezezzy', 'bsb5ivefan97', '13Alaaa', 'CaBriaShonell', 'AppleTMBini', 
  'bibliotaku', 'CravenMike', 'whtabtpineapple', 'dearmelissa', 'RaCuevas', 'FIickersGomez', 'CanalDlobu', 'jdouts', 
  'amyjwelding', 'del_wrestling', 'VuhJJDentata', 'YoTheFinesseKid', 'johnson063', 'gabrielitasch', 'eliospn', 
  'karlhacontreras', 'darIingdaz', 'CStyker', 'Ardi_MGMT', 'ArthurDaBootleg', 'sachatweets2u', 'Abdullahspi', 'lmolleur',
   'taylordough89', 'luminousphil', 'nicholasvangogh', 'cdenisegayle', 'hcjewell', 'J_M_Woods', 'Buffyfunk', 'JimmyThaLox',
    'thequeenmirai', 'rachel_dumke', 'lakeshorelolo', 'marcospereyra14', 'effortlessheart', 'lessthanconnor', 'andivhs', 
    'julianriano', 'carlylane', 'himjstinbieber', 'o1d_dude', 'mitch_bhewitt', 'Rebecca__Franco', 'NegroNoseLlello', 
    'bvckywhitewolf', 'yongduil', 'ao_cielo', 'urgirlviolet', 'TaccolaA', 'giftedkordei', 'are_eh_lee', 'lolzyoooo', 
    'north_p_', 'marcusuntrell', 'Mathilde_Felton', 'johnwaynexz', 'hoxtonmovies', 'AhmedNaguib_', 'PJMags6887'}

"""


def getAllUsers(coll):
    """
    getting every users
    :param coll:
    :return: set of all users's screen_names
    """
    return set([user['user']['screen_name'] for user in coll.find({}, {"user.screen_name": True})])




def mostActiveUsers(coll):
    """
    getting the most active users (by number of tweets)
    :param coll:
    :return:
    """
    _count = Counter()
    _count.update([user['user']['screen_name'] for user in coll.find({}, {"user.screen_name": True})])

    return _count.most_common()



