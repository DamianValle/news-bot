import tweepy
from keys import keys
from utils import is_mention_valid


# Perform authentication
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)


for mention in api.mentions_timeline():
	text = mention.text
	if(is_mention_valid(text)):
		pending_dic_file = open('./pending_dic.txt', 'a+')
		pending_dic_file.write(text.split(' ', 1)[1] + "\n")
		pending_dic_file.close()