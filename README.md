# Viral-Tweet-With-K-Nearest-Neighbor
A Machine Learning model that predicts whether or a tweet will go viral based on certain 
features associated to that tweet.


## Requirements
-	Pandas
-	Numpy
-	Scikit Learn
-	Seaborn


## The Data
The data associated with this project is I scraped it from the twitter. For, if you need to 
do the same first you'll need the [Twitter Developer Account](https://developer.twitter.com/). And then 
create an app there and so you'll have your secret keys. So I scraped twitter for 5000 tweets. And get the 
data about the tweet text, no of followers that specific user has and no of followees i-e here it is mentioned 
as friends.\
One thing to remember is that I scraped twitter for the keyword Machine Learning you can do at your own also 
one can scrape for some specific user as well.\
Here is the decription of the data 
![Data Description](https://github.com/taneemishere/Viral-Tweet-With-K-Nearest-Neighbor/blob/master/data%20description.PNG)


## Viral or Not
Define the viral tweet, as here if a tweet has greater than thousand retweets that means it is viral otherwise not. For this viral is denoted by 
1 and not viral is 0. We're doing this because as we know the numbers 
do good in machine learning.


## At Last
Plot the classifier score over different values of k and see the result. Here is my result, at most we can have 97+ accuracy which is awesome. Moreover, next we should definitely code for its confidence aka the precision of the algorithm as well.
![Plot](https://github.com/taneemishere/Viral-Tweet-With-K-Nearest-Neighbor/blob/master/plot.png)

## Scraping the Data
To scraping the data from twitter I use [this script](https://github.com/taneemishere/Viral-Tweet-With-K-Nearest-Neighbor/blob/master/Scraping%20Twitter%20Data%20by%20Keyword.py) to scrap and paste the twitter data in the form of csv file. This will create the <keyword>-tweets.csv file. 
  I use the keyword Machine Learning that's why I have ```MachineLearning-tweets.csv``` in the read_csv method.
