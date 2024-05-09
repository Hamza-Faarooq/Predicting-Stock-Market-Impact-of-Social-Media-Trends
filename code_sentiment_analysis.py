import tweepy
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import os
import unittest

# Ensure secure handling of API keys (place your keys in environment variables)
consumer_key = os.getenv('TWITTER_CONSUMER_KEY')
consumer_secret = os.getenv('TWITTER_CONSUMER_SECRET')
access_token = os.getenv('TWITTER_ACCESS_TOKEN')
access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

# Authenticate Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Error handling for Twitter API
def get_tweets(symbol, count=100):
    try:
        tweets = api.search(q=symbol, count=count, lang='en')
        df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['tweet'])
        return df
    except tweepy.TweepError as e:
        print(f"Error fetching tweets: {str(e)}")
        return pd.DataFrame()

# Error handling for stock data retrieval
def get_stock_data(symbol, start_date, end_date):
    try:
        stock_data = yf.download(symbol, start=start_date, end=end_date)
        return stock_data
    except Exception as e:
        print(f"Error fetching stock data: {str(e)}")
        return pd.DataFrame()

# Data preprocessing
def preprocess_data(df):
    # Example: Remove URLs and special characters from tweets
    df['tweet'] = df['tweet'].str.replace(r'http\S+|www\S+|[^a-zA-Z0-9\s]', '', regex=True)
    return df

# Sentiment analysis using VADER
def analyze_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    sentiment_score = analyzer.polarity_scores(text)
    return sentiment_score['compound']

# Visualization
def visualize_data(stock_data):
    stock_data['Close'].plot()
    plt.title('Stock Price Movement')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.show()

# Unit testing
class TestStockSentiment(unittest.TestCase):
    def test_get_tweets(self):
        self.assertNotEqual(len(get_tweets('AAPL')), 0)
    
    def test_get_stock_data(self):
        self.assertNotEqual(len(get_stock_data('AAPL', '2024-01-01', '2024-05-01')), 0)
    
    def test_analyze_sentiment(self):
        self.assertTrue(-1 <= analyze_sentiment("Good day!") <= 1)

if __name__ == "__main__":
    unittest.main()

    symbol = 'AAPL'
    start_date = '2024-01-01'
    end_date = '2024-05-01'

    tweets_df = get_tweets(symbol, count=100)
    stock_df = get_stock_data(symbol, start_date, end_date)

    if not tweets_df.empty and not stock_df.empty:
        tweets_df = preprocess_data(tweets_df)
        stock_change = (stock_df['Close'][-1] - stock_df['Close'][0]) / stock_df['Close'][0] * 100

        # Calculate sentiment score
        tweets_df['sentiment_score'] = tweets_df['tweet'].apply(analyze_sentiment)
        avg_sentiment = tweets_df['sentiment_score'].mean()

        # Visualize stock price data
        visualize_data(stock_df)

        print(f"Average sentiment score: {avg_sentiment}")
        print(f"Stock price change (%): {stock_change}")