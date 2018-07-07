import tweepy
from textblob import TextBlob

consumer_key = 'n6OwK1IBkRCdVTZrHFEc2hS04'
consumer_secret = 'z0gdtUSmeNlyCdYjwPkc61hsJHpVoVNOjan94gESz4SE5ZG12t'

access_token = '1904506933-fGWT7flvHzIg329zb5hvWxT3vTo3F6cPJyEkWvP'
access_token_secret = 'L2R2uhYdhzT5YqOlLoSi9Zo4iQfdYXws0lqmlg8p0YNUE'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('#GeekyRanjitxAmitBhawaniMeetup')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
