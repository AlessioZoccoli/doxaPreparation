from bson import SON


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
    groupByInList return a pipeline which aggregates documents by 'field'

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

    SENTIMENT AND OBJECTIVITY!

"""
def groupBySentimentsInList(field, usersList):
    """
    groupBySentimentsInList return a pipeline which aggregates documents by 'field' and outputs
    number of positive/neutral/negatives tweets, total tweets (for this topic),
    sentiment and objectivity.
    NOTE: sigmoid not yet applied to sentiment

    eg. groupBySentimentsInList('$user.screen_name', selectedUsers)
        {'_id': 'Pippo', 'positives': 114, 'negatives': 43, 'neutrals': 521}

    :param field: the field on which group is applied
    :param usersList: aggregation only on selected users
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
                              {"$subtract": ["$positives", "$negatives"]},
                              {"$add": ["$positives", "$negatives"]}
                          ]
                      },
                      }},
        {"$addFields": {
            "objectivity": {
                "$divide": ["$neutrals", "$totalTopic"]
            }
        }},
        {"$match": {"_id": {"$in": usersList}}},
        {"$sort": SON([("_id", +1)])},
    ]

    return pipeline