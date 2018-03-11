import re

emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
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
    r'(?:\S)'  # anything else
]

#
# VERBOSE allows spaces in the regexp to be ignored
# IGNORECASE for case insensitivity
#
tokens_re = re.compile(r'(' + '|'.join(regex_str) + ')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^' + emoticons_str + '$', re.VERBOSE | re.IGNORECASE)


def tokenize(text):
    return tokens_re.findall(text)


def preprocess(text, lowercase=False):
    """
    es.

    myTweet = "RT @ShadowhuntersTV: Here is @DomSherwood1's #Oscars pick. Play The Official Oscars Challenge and make your picks.
                 Ballots close before the…"

    print(preprocess(myTweet))
    ['RT', '@ShadowhuntersTV', ':', 'Here', 'is', '@DomSherwood1', "'", 's', '#Oscars', 'pick', '.', 'Play', 'The', 'Official', 'Oscars',
    'Challenge', 'and', 'make', 'your', 'picks', '.', 'Ballots', 'close', 'before', 'the', '…']

    :param text: String. input text
    :param lowercase: Boolean. If true, output tokens are lowercase
    :return: List of tokens
    """
    tokens = tokenize(text)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens