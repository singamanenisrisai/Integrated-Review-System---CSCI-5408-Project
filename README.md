# Integrated-Review-System---CSCI-5408-Project
Integrated Review System to Conclude Ratings of Different Places using Machine Learning Algorithms 
#### ABSTRACT
##### The statistics show that there are 115,394 number of food and service businesses across Canada and on an average, Canadians make 17 million restaurant visits on a typical day (Summary - Canadian Industry Statistics, 2017). One of the easy ways to choose a restaurant in a new place is reviews or ratings. There could be hundreds of reviews on each restaurant. Therefore, the developed Integrated Review System will do sentiment analysis on the restaurant reviews and provide a consolidated review of the restaurant. This Review system will save a lot of time for the customer and helps the business to understand the emotions of the customers easily.
#### PROBLEM STATEMENT
##### In general, most people rely on online reviews for choosing restaurant. But end up in reading all the reviews or just see the star ratings. There are many websites, applications and forums to help the customers to fetch information and know about the restaurant. But certain times customer might be in a position where, confused to choose the website or application for reviewing. So, the developed application could fill the gap between customers and review process.
#### INTRODUCTION
##### The Integrated Review System is a one stop solution to the people, who rely on the restaurant reviews for the choosing the restaurant. It is aimed to consolidate the reviews from different sources, analyse the reviews and provide the integrated review of the restaurant. The system uses the Yelp reviews dataset from Kaggle website to train the model. The captured reviews from different sources will be loaded into the trained model for predictive analysis and the consolidated review would be provided to the customers and business. Also, the reviews of restaurant are classified into three categories positive, negative, and neutral.
#### VALUE PROPOSITION
##### The developed Integrated Review System would help the customers and as well as the businesses. By getting the data from multiple sources and using it for predictive analysis, draws a line out from other review platforms available in the market. Based on the classified category review, the customers and businesses are benefited in terms of time on review analysis. This can be easily integrated into a graphical user interface in future, so that everyone can have easy access to the review system.
#### IMPLEMANTATION
##### Step1:
##### Requirement Analysis; Researched different data sources for selecting the dataset and required information to kick start the project. In this step, we choose Yelp review dataset for our model training and Google API’s for streaming the latest reviews. Later, we discussed and researched on certain tools to implement the project. The tools will be discussed under tools and technologies section.
##### Step2:
##### Data Pre-processing; In this step we started looking into data cleaning. The extracted Yelp review dataset is a roughly three and half GB. The first challenge here was, we found it difficult to analyse the data manually due to its size. Therefore, we break down the dataset into number of small chucks.
##### By analysing the dataset, we found that there is lot of noisy data such as null values, new line characters etc. Finally, we removed the unnecessary columns and cleaned the data using python script.
#### Step3:
##### Sentiment Analysis; In this step we performed sentiment analysis on the pre-processed dataset by using Vader sentiment analysis library. The library was imported from GitHub repository, it is lexicon and rule-based sentiment analysis tool that was specially designed for analysing the emotions in social media and released under MIT open source license (Cjhutto, 2018). Finally, we derived the review text, sentiment of the text i.e., either positive, negative or neutral and the sentiment score.
#### Step4:
##### Model Training; In this step we started towards our model training. The outcome data of step3 was used for the model training. We used spark Machine Learning libraries for feature extraction and classification. Regex Tokenizer and Count vectors libraries are used for feature extraction and logistic regression algorithm was used for the classification.

#### Submitted by:
#### Hemanth Kurra (B00784050)
#### Srisaichand Singamaneni (B00792835)
