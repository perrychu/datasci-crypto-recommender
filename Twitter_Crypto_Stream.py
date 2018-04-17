import pandas as pd
import requests
from requests_oauthlib import OAuth1
import cnfg
import tweepy
import json
from pymongo import MongoClient

config = cnfg.load(".twitter_config")

auth = tweepy.OAuthHandler(config["consumer_key"],
                           config["consumer_secret"])
auth.set_access_token(config["access_token"],
                      config["access_token_secret"])

api=tweepy.API(auth)

client = MongoClient(port=27017)
db = client.crypto
livetweets = db.tweets_v3

#livetweets.drop() # only if we want to start from scratch

class StreamListener(tweepy.StreamListener):
    errors = 0

    def on_status(self, status):
        
        # skip non english tweets
        if status.lang != "en": 
            return
    
        # insert into db
        try:
            livetweets.insert_one(status._json)
        except Exception as e:
            print("exception",e)
            pass
    
    def on_error(self, status_code):
        if status_code == 420:
            if(errors >1):
                return false
            time.sleep(60)
        print("Error:",status_code)
        return true

general = ["cryptocurrency","cryptocurrencies","blockchain","crypto"]            
coin_tickers = ["BTC","ETH","XRP","BCH","LTC","NEO","ADA","XLM","EOS","IOTA","MIOTA",
           "DASH","XMR","ETC","XEM","TRX","VEN","USDT","QTUM","LSK","NANO",
           "OMG","BTG","ICX","ZEC","BNB","DGD","BCN","STEEM","XVG","PPT",
           "STRAT","DOGE","SC","RHOC","MKR","SNT","BTS","WTC","DCR","ZRX",
           "KCS","NAS","AION","POWR","REQ"
          ]
coin_names = ["Bitcoin","Ethereum","Litecoin","Cardano","Monero","Vechain","OmiseGo",
              "Stratis","Dogecoin","SiaCoin","RChain","Waltonchain"
             ]
words = (["#" + g for g in general] 
         + ["$" + t for t in coin_tickers]
         + ["#" + t for t in coin_tickers]
         + ["#" + n for n in coin_names]
        )


stream_listener = StreamListener()
stream = tweepy.Stream(auth=api.auth, listener=stream_listener, tweet_mode='extended')
stream.filter(track=words,async = True)
