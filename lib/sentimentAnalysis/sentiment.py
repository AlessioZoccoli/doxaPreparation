from textblob import TextBlob
from lib.language.languageProcessing import cleanedTweet


##########################################################################
#                                                                        #
#   Sentiment Analysis with textblob                                     #
#                                                                        #
##########################################################################


def tweetPolarity(tweetText):
    polarity = TextBlob(cleanedTweet(tweetText)).polarity

    if polarity > 0:
        category = "POSITIVE"
    elif polarity == 0:
        category = "NEUTRAL"
    else:
        category = "NEGATIVE"

    return (polarity, category)


# (POSITIVE, NEUTRAL, NEGATIVE)
def tweetPolarityOneHot(tweetText):
    polarity = TextBlob(cleanedTweet(tweetText)).polarity

    if polarity > 0:
        category = (1,0,0)
    elif polarity == 0:
        category = (0,1,0)
    else:
        category = (0,0,1)

    return (polarity, category)