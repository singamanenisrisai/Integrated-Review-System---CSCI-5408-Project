#!/usr/bin/env python3
import pandas as pnd
dataoutput = pnd.read_csv("chunk0.csv")
SentiFinal = pnd.DataFrame()

reviews = dataoutput["text"].map(lambda x: x.lower())

dataoutput["inputreviews"]=reviews
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
output = SentimentIntensityAnalyzer()

negative=[]
positive=[]
neutral=[]
compound=[]
sentiAnalysis=[]
sentiScore = []

for review in reviews:
    sentiValues = output.polarity_scores(review)
    negative.append(sentiValues["neg"])
    positive.append(sentiValues["pos"])
    neutral.append(sentiValues["neu"])
    compound.append(sentiValues["compound"])

    if sentiValues["neg"]>sentiValues["pos"]:
        sentiAnalysis.append("Negative")
        sentiScore.append(sentiValues["neg"])
    elif sentiValues["pos"]>sentiValues["neg"]:
        sentiAnalysis.append("Positive")
        sentiScore.append(sentiValues["pos"])
    else:
        sentiAnalysis.append("Neutral")
        sentiScore.append(sentiValues["neu"])

dataoutput["positive"] = positive
dataoutput["neutral"] = neutral
dataoutput["negative"] = negative
dataoutput["compound"] = compound
dataoutput["SentiAnalysis"] = sentiAnalysis
dataoutput["SentiScore"] = sentiScore

SentiFinal["Reviews"] = dataoutput["inputreviews"]
SentiFinal["SentimentAnalysis"] = dataoutput["SentiAnalysis"]
SentiFinal["SentimentScore"] = dataoutput["SentiScore"]

print(SentiFinal)
print(dataoutput)

SentiFinal.to_csv("FinalReview.csv", index=False)
dataoutput.to_csv("sentiReviews.csv", index=False)
