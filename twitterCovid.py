
import tweepy
import pandas as pd

#%run ./Keys.py
dosya = open('Keys.py')
  #info = py.load(my_cred_data)
consumerKey = info['A41fUVUERwALBSon7BSZpjyXn']
consumerSecret = info['qgBrCfDnCLqxAGJ8EWjW3sQSNTmgC9qXdg53tPGUNRaus9SQYL']
accessToken = info['861871854902018048-n8anYq7aPSVN0DVTilECUWnQj40xFzh']
accessTokenSecret = info['RKxFCWLrEPLXHu3cnYH67z0rQiv2oU8lCohL8PK0CkVLt']


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True) #important
# searching for tweets for hashtag COVID and 100 tweets
self_tweets = tweepy.Cursor(api.search, q='COVID19, lang="en").items(100)
for tweet in self.tweets:
  print(tweet.text)

def cleanTweet(self, tweet):
   # Remove Links, Special Characters etc from tweet
   return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w +:\ / \ / \S +)", " ", tweet).split())

#To call function in code: 
   sentence = self.cleanTweet(sentence)

# and passing cleaned data to TextBlob 
   analysis = TextBlob(sentence)   

   print(analysis.sentiment)  # print tweet's polarity