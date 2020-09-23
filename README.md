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
1 and not viral is 0.


## At Last
Plot the classifier score over different values of k and see the result. Here is mine 
![Plot](https://github.com/taneemishere/Viral-Tweet-With-K-Nearest-Neighbor/blob/master/plot.png)
