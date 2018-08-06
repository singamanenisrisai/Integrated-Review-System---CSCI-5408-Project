# This script finally performs sentiment analysis on the extracted reviews from google and perform senti analysis using our trained model
from pyspark.ml import PipelineModel
from pandas import DataFrame
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.sql import SQLContext, SparkSession

sc = SparkContext("local[2]", "Sentiment Predict")
sqlContext = SQLContext(sc)
df = sqlContext.read.csv("reviews.csv",header =True)
model = PipelineModel.load("logreg.model")
print("++++++++ %s  +++++++" % str(model))
predictions = model.transform(df.select("SentimentText"))
predictions.select("SentimentText","prediction").show()
predictions.select("SentimentText","prediction").toPandas().to_csv("Integrated_Reviews.csv")

#References:
# Dalhousie University - CSCI 5408 Assignments.
