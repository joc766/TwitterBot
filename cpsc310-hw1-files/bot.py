import tweepy
import gpt_2_simple as gpt2
# TODO: Replace the 'XXXXX's with your consumer key, consumer secret, access token, 
# and access secret for Twitter. These will be used by Tweepy.

# The Consumer Twitter API key and secret can be found on the Twitter Developer Portal

# You must generate the Access token and secret yourself by running the provided
# get_access.py code. (You must also add your consumer key and secret to that file.)

CONSUMER_KEY = "5XCSYuQrM6drq8sUCE3KtqyB5"
CONSUMER_SECRET = "HTgoUyg3uPyjl8IIEnjGk8QLTu9h1l21vi8CUQCK0HfgHTdiZZ"

ACCESS_TOKEN = "1488596326455693314-meMb01EzUGpuoBop1VQXF9Ez1aXHKw"
ACCESS_SECRET = "wHuykQWGzdxn6DgF7d81VQtc08sNSYVVCaXw9nMC9fZNJ"


# Sets up the Twitter API
def getAPI():
    
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    api = tweepy.API(auth)
    return api

def run():

    api = getAPI()
    # TODO: Implement parts 3 and 4
    # (i)
    userID = "CNN"
    corpus = []
    for i in range(5):
        corpus.extend(api.user_timeline(screen_name=userID, count=200, include_rts = False, tweet_mode = 'extended'))
    # (ii)


    


if __name__ == '__main__':
    run()

