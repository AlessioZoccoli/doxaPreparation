from bson import SON
from pymongo import UpdateOne


def groupByConditional(fieldGroup, fieldFilter):
    """

    returns a pipeline which aggregates by fieldGroup (eg. screen_name) all the selected users and count how many tweets
    don't have the fieldFilter field (eg. inTopicCollection)

    es.

    fieldGroup = _field
    fieldFilter = "inTopicCollection"

        pipeline = [
        {"$unwind": _field},
        {"$match": {"inTopicCollection": {"$exists": False}}},
        {"$group": {"_id": _field, "count": {"$sum": 1}}},
        {"$sort": SON([("_id", +1)])},
    ]

    :param fieldGroup: field to group by
    :param fieldFilter: field that filters out the documents (by non possession)
    :return: list of dicts, the pipeline
    """

    if not fieldGroup.startswith("$"):
        _fieldGroup = '' + '$' + fieldGroup
    else:
        _fieldGroup = fieldGroup

    pipeline = [
        {"$unwind": _fieldGroup},
        {"$match": {fieldFilter: {"$exists": False}}},
        {"$group": {"_id": _fieldGroup, "count": {"$sum": 1}}},
        {"$sort": SON([("_id", +1)])},
    ]
    # {"$sort": SON([("count", -1), ("_id", -1)])} per numero di tweet e id
    return pipeline


def groupByInList(field, usersList):
    """
    groupByInList return a pipeline which aggregates documents by 'field' if id in usersList

    :param field: the field on which group is applied
    :param usersList: aggregation only on selected users
    :return: list of dicts, the pipeline
    """
    if not field.startswith("$"):
        _field = '' + '$' + field
    else:
        _field = field

    pipeline = [
        {"$unwind": _field},
        {"$group": {"_id": _field, "count": {"$sum": 1}}},
        {"$match": {"_id": {"$in": usersList}}},
        {"$sort": SON([("_id", +1)])},
    ]
    return pipeline


"""

    SENTIMENT, OBJECTIVITY and VOLUME

"""


def calculateSentimentObjectivity(field, usersList, outCollection):
    """
    calculateSentimentObjectivity return a pipeline which aggregates documents by 'field' and outputs
    number of positive/neutral/negatives tweets, total tweets (for this topic),
    sentiment and objectivity.
    NOTE: sigmoid not yet applied to sentiment

    eg. calculateSentimentObjectivity('$user.screen_name', selectedUsers)
        {'_id': 'Pippo', 'positives': 114, 'negatives': 43, 'neutrals': 521}

    :param field: the field on which group is applied
    :param usersList: aggregation only on selected users
    :param outCollection: collection that will store the aggregation
    :return: list of dicts, the pipeline
    """

    if not field.startswith("$"):
        _field = '' + '$' + field
    else:
        _field = field

    pipeline = [
        {"$group": {
            "_id": _field,
            "positives": {"$sum": "$positive"},
            "negatives": {"$sum": "$negative"},
            "neutrals": {"$sum": "$neutral"},
        }
        },
        {"$project": {"_id": 1, "positives": 1, "negatives": 1, "neutrals": 1,
                      "totalTopic": {"$add": ["$positives", "$negatives", "$neutrals"]},
                      "sentiment": {
                          "$divide": [
                              1,
                              {"$add": [1, {
                                  "$pow": [
                                      10,
                                      {"$multiply": [
                                          -1, {"$divide": [
                                              {"$subtract": ["$positives", "$negatives"]},
                                              {"$add": ["$positives", "$negatives"]}
                                          ]}
                                      ]}
                                  ]}
                                        ]}]
                      }}},
        {"$addFields": {
            "objectivity": {
                "$divide": ["$neutrals", "$totalTopic"]
            }
        }},
        {"$match": {"_id": {"$in": usersList}}},
        {"$sort": SON([("_id", +1)])},
        {"$out": outCollection}
    ]

    return pipeline


def calculateVolume(fromCursor, toCollection):
    """
    e.g.
        calculateVolume( aggregationUnrelatedCursor, svoCollection)

        Volume = how much a user wrote about a specific topic / everything wrote by this user

    :param fromCursor: cursor from which unrelated tweets count comes from
    :param toCollection: volume will be added here
    :return: list of update operations
    """

    # collection.find(<cond>)[0] because each cursor will only point to one document

    addVolume = [
        UpdateOne({'_id': el['_id']}, {'$set': {'volume': toCollection.find({'_id': el['_id']})[0]['totalTopic'] / (
                    toCollection.find({'_id': el['_id']})[0]['totalTopic'] + el['count'])}})
        for el in fromCursor
    ]
    return addVolume


def addVolume2Missings(svoColl):
    """
    addVolume2Missings(svoCollection) adds volume as

        totalTopic /(totalTopic + 0) = 1

    to those who haven't be affected be the update in the previous function.

    :param svoColl: volume will be added here
    :return: list of update operations
    """

    return [UpdateOne({'_id': el['_id']}, {'$set': {'volume': 1}}) for el in svoColl.find({'volume': {'$exists': False}})]
