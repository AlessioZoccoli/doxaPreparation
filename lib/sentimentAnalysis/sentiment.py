from textblob import TextBlob
from lib.language.languageProcessing import cleanedTweet

"""

    Sentiment Analysis with TextBlob
    
    TextBlobs uses


"""


def tweetPolarity(tweetText):
    """
    tweetPolarity("Great") -> (1.0, "Positive")

    :param tweetText: String. Text of the tweet
    :return: tuple (Int, String) with polarity and sentiment class as a textual label
    """
    polarity = TextBlob(cleanedTweet(tweetText)).polarity

    if polarity > 0:
        category = "POSITIVE"
    elif polarity == 0:
        category = "NEUTRAL"
    else:
        category = "NEGATIVE"

    return (polarity, category)



def tweetPolarityOneHot(tweetText):
    """
    tweetPolarityOneHot("Great") -> (1.0, (1,0,0))

    :param tweetText: String. Text of the tweet
    :return: tuple (Int, tuple(Int)) with polarity and sentiment class one hot encoded
    """
    polarity = TextBlob(cleanedTweet(tweetText)).polarity

    if polarity > 0:
        category = (1,0,0)
    elif polarity == 0:
        category = (0,1,0)
    else:
        category = (0,0,1)

    return (polarity, category)



"""

Sentiment Orientation with PMI:                                                                          

SO(t) = SUM( PMI(t,t') for t' in PosVocab) -  SUM( PMI(t,t') for t' in NegVocab)                      
                                                                                                             
P(t) = DF(t)/|D|                                                                                      
P(t1, t2) = DF(t1, t2)/|D|                                                                            
                                                                                                             
"""