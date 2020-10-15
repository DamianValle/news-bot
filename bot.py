import tweepy
from keys import keys
from utils import remove_urls, replace_words

"""
Perform authentication
"""
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

#api.update_status("Hello España")

userID = "el_pais"
tweets = api.user_timeline(screen_name=userID, 
	count=1, 
	include_rts = False, 
	tweet_mode = 'extended')

for tweet in tweets:
	api.update_status(replace_words(tweet.full_text), 
		in_reply_to_status_id = tweet.id, 
		auto_populate_reply_metadata=True)



