import tweepy
import textblob
from textblob import TextBlob


consumer_key = 'tIlu5VWiX05objcMa6LmHRFt0'
consumer_secret = '6gkyT0LTVpAlNrGeBsDFZ4MBupcrMeO7vTkF9PPFqXOZZRVqTd'

access_token = '868415366027853824-0OwHrmttXkYgXvfzkiP84rJlDTdKLQ4'
access_secret = 'iH4DS0yVayNQvXJ2QgsSVyErxLRj0u3wWaYXlXOmOVZfl'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
public_tweets = api.search("On Assignment Inc.")

for tweet in public_tweets:
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)