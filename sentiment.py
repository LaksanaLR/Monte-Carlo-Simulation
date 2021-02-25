import tweepy
import textblob
from textblob import TextBlob


consumer_key = ''
consumer_secret = ''

access_token = ''
access_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
public_tweets = api.search("On Assignment Inc.")

for tweet in public_tweets:
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
