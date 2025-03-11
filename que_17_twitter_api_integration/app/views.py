import tweepy
from django.shortcuts import render
from django.conf import settings
from tweepy import TweepyException  

# Authenticate using the credentials in settings.py
def get_twitter_api():
    auth = tweepy.OAuth1UserHandler(
        settings.TWITTER_API_KEY,
        settings.TWITTER_API_SECRET_KEY,
        settings.TWITTER_ACCESS_TOKEN,
        settings.TWITTER_ACCESS_TOKEN_SECRET
    )
    api = tweepy.API(auth)
    return api

def latest_tweets(request):
    username = 'elonmusk'  
    tweets = []

    try:
        api = get_twitter_api()
        tweets = api.user_timeline(screen_name=username, count=5, tweet_mode='extended')

    except TweepyException as e:
        tweets = []
        print(f"Error fetching tweets: {e}")


    return render(request, 'twitter_app/demo.html', {'tweets': tweets, 'username': username})

