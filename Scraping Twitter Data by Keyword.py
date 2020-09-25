# Imports
import tweepy
import pandas as pd
import time

# Credentials

consumer_key = "XXXXXXXXXXXXX"
consumer_secret = "XXXXXXXXXXXXX"
access_token = "XXXXXXXXXXXXX"
access_token_secret = "XXXXXXXXXXXXX"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

tweets = []

def random_tweets(text_query, count):
    try:      
        # Creation of query method using parameters
        tweets = tweepy.Cursor(api.search,q=text_query).items(count)

        # Pulling information from tweets iterable object
        tweets_list = [[tweet.text, tweet.retweet_count, tweet.user.followers_count, tweet.user.friends_count] for tweet in tweets]

        # Creation of dataframe from tweets list
        tweets_df = pd.DataFrame(tweets_list,columns=['Text', 'No-of-Retweets', 'Followers', 'Friends'])

        # Converting dataframe to CSV 
        tweets_df.to_csv('{}-tweets.csv'.format(text_query), sep=',', index = False)

    except BaseException as e:
          print('failed on_status,',str(e))
          time.sleep(3)

# Input username to scrape tweets and name csv file
# Max recent tweets pulls x amount of most recent tweets from that user
keyword = 'Machine Learning'
count = 5000

# Calling function to turn username's past X amount of tweets into a CSV file
random_tweets(keyword, count)
