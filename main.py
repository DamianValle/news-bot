import tweepy
import random
import logging
from keys import keys
from utils import remove_urls, replace_words

def bot(self):

	#Logging utility for both local and cloud runtime.
	log = "bot.log"
	logging.basicConfig(filename=log,level=logging.INFO,format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
	logging.info('Started script')

	# Perform authentication.
	CONSUMER_KEY = keys['consumer_key']
	CONSUMER_SECRET = keys['consumer_secret']
	ACCESS_TOKEN = keys['access_token']
	ACCESS_TOKEN_SECRET = keys['access_token_secret']

	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

	api = tweepy.API(auth)


	# Define accounts to choose from and pick one randomly.
	accounts = ["nytimes", "nytimestech", "nytimesatwar", "nytimeswell", "nytimesmusic", "nytimesarts", "nytopinion"]
	selected_account = random.choice(accounts)

	# Get selected account's last 5 tweets.
	tweets = api.user_timeline(screen_name=selected_account, 
		count=5, 
		include_rts = False, 
		tweet_mode = 'extended')

	# Iterate until finding at most one tweet with at least a word match.
	for tweet in tweets:
		logging.info("Text was: " + tweet.full_text)
		text = replace_words(tweet.full_text)
		if(text == "-1"):
			logging.info("There was no match")
		else:
			api.update_status(replace_words(tweet.full_text), 
			in_reply_to_status_id = tweet.id, 
			auto_populate_reply_metadata=True)
			logging.info("Tweeted: " + text)

			break