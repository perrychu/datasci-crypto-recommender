# datasci-crypto-recommender
A recommender system for cryptocurrencies based on tweets.

## Summary
This is my unsupervised learning project for Metis (a data science bootcamp). It includes script to capture tweets (via Twitter streaming API using tweepy & MongoDB), a brief exploration of NLP, and a recommender system for tweet hashtags.

The focus of the recommender system is to suggest new cryptocurrencies that a user might be interested based on their current interests or portfolio. I captured tweets with cryptocurrency & blockchain related hashtags, then interpreted each user's hashtags as interest indicators. With these indicators, I can find similar users and suggest new hashtags in a collaborative model.

Some concepts explored in this project are dimension reduction (SVD / NMF), recommender systems, and ways of measuring recommender fit.

## Files
#### Code
* **Twitter_Crypto_Stream.py** - Script to stream cryptocurrency tweets. Requires a local MongoDB server to store results.
* **Twitter_Mongo_EDA** - MongoDB exploration of features and extraction of user and tweet text + hashtag fields to new collection
* **Twitter_Analysis** - Brief exploration of NLP topic modeling on tweet text, and build / evaluation of recommender system using Recall@N metric

#### Docs
* **Crypto_Recommender_Slides.pdf** - Project presentation slides
* **Crypto_Recommender_Writeup.pdf** - Outline of project process

## Results
I used a Recall@N metric, which simulates an evaluation by showing the recommender all but one of a new user's hashtags. The recommender then outputs the top N recommendations, and we measure how often the holdout hashtag shows up in the recommendation.

As a baseline, I implemented a recommender that simply output the most popular hashtags which the user hasn't used yet. The SVD collaborative filtering improved on the baseline by 1% for Recall@5 and by 17% for Recall@10.