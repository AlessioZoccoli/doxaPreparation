from nltk.corpus import stopwords
import re, string, operator
from collections import Counter, defaultdict

emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose
        [D\)\]\(\]/\\OpP] # Mouth
    )"""

regex_str = [
    emoticons_str,
    r'<[^>]+>',  # HTML tags
    r'(?:@[\w_]+)',  # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)",  # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',  # URLs
    r'(?:(?:\d+,?)+(?:\.?\d+)?)',  # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])",  # words with - and '
    r'(?:[\w_]+)',  # other words
    r"(?:\w+)\.{2,}(?:.+)",  # ellipsis
    r'(?:\S)'  # anything else
]

#################################################################
#       VERBOSE allows spaces in the regexp to be ignored       #
#       IGNORECASE for case insensitivity                       #
#################################################################
tokens_re = re.compile(r'(' + '|'.join(regex_str) + ')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^' + emoticons_str + '$', re.VERBOSE | re.IGNORECASE)


def tokenize(text):
    return tokens_re.findall(text)


def preprocess(text, lowercase=False):
    """
    es.

    myTweet = "RT @ShadowhuntersTV: Here is @DomSherwood1's #Oscars pick. Play The Official Oscars Challenge and make
    your picks. Ballots close before the…"

    print(preprocess(myTweet))
    ['RT', '@ShadowhuntersTV', ':', 'Here', 'is', '@DomSherwood1', "'", 's', '#Oscars',
    'pick', '.', 'Play', 'The', 'Official', 'Oscars', 'Challenge', 'and', 'make', 'your', 'picks', '.', 'Ballots',
    'close', 'before', 'the', '…']

    :param text: String. input text
    :param lowercase: Boolean. If true, output tokens are lowercase
    :return: List of tokens
    """
    tokens = tokenize(text)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens


############################
#    Stop words handling   #
############################

# … != ... and seems to occur a lot
punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', 'via', '…']


def termsAndEmoji(tokens):
    """
    :param tokens: list of tokens
    :return: same list without stop words, links and mentions
    """
    return [t for t in tokens if t not in stop and not t.startswith(('@', 'http:', 'https:'))]


############################
#    Terms frequency       #
############################

def nMostCommonTerms(docs, n):
    """
    nMostCommonTerms(mongoCollection.find(), 4)
    [('#Oscars', 200), ('Official', 100), ('night', 90), ('The', 89)]

    :param docs: Documents of mongoDB collection.
    :param n: int. n most common terms
    :return: list of tuples [('term'), k]
    """
    _count = Counter()
    for tweet in docs:
        _terms = termsAndEmoji(preprocess(tweet['text'], lowercase=True))
        _count.update(set(_terms))
    return _count.most_common(n)


##################################
#    Terms co-occurrences        #
##################################

def nMostCommonCooccurrences(docs, n):
    """
    nMostCommonCooccurrences(collection, 3)

    :param docs: mongoDB collection
    :param n: int. n most common terms cooccurrences
    :return: list of tuples [('termA', 'termB'), k]
    """

    # If retrieving/updating a non existing value, return a default value specified as defaultdict argument (eg. int)
    comatrix = defaultdict(lambda : defaultdict(int))

    # Populating the matrix
    for tweet in docs:
        _terms = termsAndEmoji(preprocess(tweet['text'], lowercase=True))

        for i in range(len(_terms) - 1):
            for j in range(i+1, len(_terms)):
                term1, term2 = sorted([_terms[i], _terms[j]])
                if term1 != term2:
                    comatrix[term1][term2] += 1

    commons = []

    # For each term search the n most cooccurrent terms
    # reverse=True = Descending
    for t1 in comatrix:
        t1_mostCommons = sorted(comatrix[t1].items(), key=operator.itemgetter(1), reverse=True)[:n]
        for t2, t2_count in t1_mostCommons:
            commons.append(((t1, t2), t2_count))

    mostCommons = sorted(commons, key=operator.itemgetter(1), reverse=True)[:n]
    return mostCommons