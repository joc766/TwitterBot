from transformers import TFGPT2LMHeadModel, GPT2Tokenizer
import random
import tweepy
import gpt_2_simple as gpt2
import os
import requests
import csv
import tensorflow as tf
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
# TODO: Replace the 'XXXXX's with your consumer key, consumer secret, access token, 
# and access secret for Twitter. These will be used by Tweepy.

# The Consumer Twitter API key and secret can be found on the Twitter Developer Portal

# You must generate the Access token and secret yourself by running the provided
# get_access.py code. (You must also add your consumer key and secret to that file.)

CONSUMER_KEY = "5XCSYuQrM6drq8sUCE3KtqyB5"
CONSUMER_SECRET = "HTgoUyg3uPyjl8IIEnjGk8QLTu9h1l21vi8CUQCK0HfgHTdiZZ"

ACCESS_TOKEN = "1488596326455693314-meMb01EzUGpuoBop1VQXF9Ez1aXHKw"
ACCESS_SECRET = "wHuykQWGzdxn6DgF7d81VQtc08sNSYVVCaXw9nMC9fZNJ"

gpt2.download_gpt2(model_name="124M")
#gpt2.mount_gdrive()

# Sets up the Twitter API
def getAPI():
    
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    api = tweepy.API(auth)
    return api

"""I ran my code on Google Colab in order to use their GPU
  I also stored my trained model in google drive so that I could run them more easily"""
def run():
  nsteps = 1000
  api = getAPI()

  # (i)
  userID = "jayrosen_nyu"
  corpus = []
  for i in range(5):
      corpus.extend(api.user_timeline(screen_name=userID, count=200, include_rts = False, tweet_mode = 'extended'))
  corpus.extend(api.user_timeline(screen_name="marknorm", count=55, include_rts = False, tweet_mode = 'extended'))
  corpus.extend(api.user_timeline(screen_name="bertkreischer", count=200, include_rts = False, tweet_mode = 'extended'))
  model_name = "124M"
  if not os.path.isdir(os.path.join("models", model_name)):
      print(f"Downloading {model_name} model...")
      gpt2.download_gpt2(model_name=model_name)   # model is saved into current directory under /models/124M/

  #(ii)
  file_name = "tweets.csv"
  if not os.path.isfile(file_name):
    with open(file_name, 'w') as csvfile:
      writer = csv.writer(csvfile)
      writer.writerow(["tweet"])
      for tweet in corpus:
        words = nltk.word_tokenize(tweet.full_text)
        new_words = [word for word in words if word.isalnum()]    
        new_tweet = " ".join([str(item) for item in new_words])
        print(new_tweet)
        writer.writerow([new_tweet])
  sess = gpt2.start_tf_sess()
  gpt2.finetune(sess,
                file_name,
                steps=nsteps,
                restore_from='fresh',
                run_name='run1',
                print_every=10,
                )   # steps is max number of training steps

  #gpt2.copy_checkpoint_from_gdrive(run_name='run1')

  #sess = gpt2.start_tf_sess()
  #gpt2.load_gpt2(sess, run_name='run1')

  nltk.download([
          "names",
          "stopwords",
          "state_union",
          "twitter_samples",
          "movie_reviews",
          "averaged_perceptron_tagger",
          "vader_lexicon",
          "punkt",
      ])

  #(iii)
  freedonia = "FreedoniaNews"
  freedonia_tweets_info = (api.user_timeline(screen_name=freedonia, include_rts = False, tweet_mode = 'extended'))
  freedonia_tweets = []
  for tweet in freedonia_tweets_info:
    freedonia_tweets.append(tweet.full_text)

  freedonia_tweets = [t.replace("://", "//") for t in freedonia_tweets]

  sentiments = []
  for tweet in freedonia_tweets:
    analysis = TextBlob(tweet)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
      sentiment = "positive"
    elif polarity == 0:
      sentiment = "neutral"
    else:
      sentiment = "negative"
    print(sentiment)
    sentiments.append(sentiment)

  subjects = []
  for tweet in freedonia_tweets:
    if "Slyvania" in tweet:
      sub = "Slyvania"
    elif "Ambassador Trentino" in tweet:
      sub = "Ambassador Trentino"
    elif "Freedonia" in tweet:
      sub = "Freedonia"
    elif "Rufus T. Firefly" in tweet:
      sub = "Rufus T. Firefly"
    print(sub)
    subjects.append(sub)

  agrees = {}
  agrees["Slyvania"] = True
  agrees["Ambassador Trentino"] = True
  agrees["Freedonia"] = False
  agrees["Rufus T. Firefly"] = False


  #(iv)
  response = None
  i = random.randrange(8)
  response_sentiment = None
  tweet_sentiment = sentiments[i]
  subject = subjects[i]
  if agrees[subject]:
    if tweet_sentiment == "positive":
      desired_sentiment = "positive"
    else:
      desired_sentiment = "negative"
  else:
    if tweet_sentiment == "positive":
      desired_sentiment = "negative"
    else:
      desired_sentiment = "positive"
  while response_sentiment != desired_sentiment:
    text = gpt2.generate(sess, run_name="run1", prefix=subject, length=40, return_as_list=True, temperature=1, top_k=40, top_p=0.85)[0]
    analysis = TextBlob(text)
    gen_score = analysis.sentiment.polarity
    if gen_score > 0.4:
      response_sentiment = "positive"
    elif gen_score < -0.4:
      response_sentiment = "negative"
    else:
      repsponse_sentiment = "neutral"

  text = text.replace("endoftext", "")
  text = text.replace("https", "")
  text = text.replace("startoftext", "")
  text = text.replace("<|", "")
  text = text.replace("|>", "")

  #print("Found a match for tweet {i}".format(i=i), "The tweet was about {} and had a {} sentiment.\
    #   The response had a {} sentiment".format(subject, tweet_sentiment, response_sentiment))
  #print("The response was {}".format(text))
  response = text


  #(v)
  freedonia_tweet_id = freedonia_tweets_info[i].id
  if len(response) > 279:
    print('here')
    send_it = response[:200]
  else:
    send_it = response
  print(freedonia_tweet_id)
  api.update_status(send_it, freedonia_tweet_id, auto_populate_reply_metadata=True)

if __name__ == "__main__":
  # I ran my code on Google Colab in order to use a GPU
  run()