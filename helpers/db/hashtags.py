from collections import defaultdict


def getId2Hashtags(collection):
    """
    returns a (default)dict associating IDs to hashtags

    :param collection:
    :return: defaultdict(id_str, [hashtag1, ... ,hashtagN])
    """

    id2hashtags = defaultdict(set)

    for el in collection:
        for h in el['entities']['hashtags']:
            id2hashtags[el['id_str']].add(h['text'])

    return id2hashtags


