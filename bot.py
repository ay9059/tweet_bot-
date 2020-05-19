import tweepy

consumer_key = 'q2DLfHWWx0sCakj7GrTWirbcL'
secret_key = 'wOpiNcNQCLqEEWmMZsM2RQXeQ5CSmZbUnwBkF7EirpahXIgmLl'

key = '1262879777502965771-Tf4BGHWM62Tqhuz8jftOlKTsoHHlNL'
secret = '1262879777502965771-Tf4BGHWM62Tqhuz8jftOlKTsoHHlNL'


auth= tweepy.OAuthHandler(consumer_key, secret_key)
auth.set_access_token(key, secret)

api = tweepy.API(auth)
public_tweets = api.search('Ubisoft')
for tweet in public_tweets:
    print(tweet)