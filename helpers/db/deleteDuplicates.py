from pymongo import MongoClient
import config


if __name__ == "__main__":
    client = MongoClient(config.db_clientUsers)

    # selecting the collection
    mycoll = client[config.db_nameUsers][config.db_collectionUsers]

    # this will aggregate all duplicates
    cursor = mycoll.aggregate(
        [
            {"$group": {"_id": "$id_str", "unique_ids": {"$addToSet": "$_id"}, "count": {"$sum": 1}}},
            {"$match": {"count": {"$gte": 2}}}
        ]
    )


    for el in cursor:
        print("duplicates found --->   ", el)


    # Deleting the duplicates
    response = []
    for doc in cursor:
        del doc["unique_ids"][0]
        for id in doc["unique_ids"]:
            response.append(id)

    mycoll.delete_many({"_id": {"$in": response}})


