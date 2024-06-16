
# Stock Sentiment Analysis

## Overview
This project analyzes stock sentiment by retrieving tweets related to a specified stock symbol using the Twitter API. 
It preprocesses the tweet data, conducts sentiment analysis using the VADER sentiment analyzer, and retrieves stock price data from Yahoo Finance. 
The sentiment scores are then aggregated to calculate an average sentiment score, which is compared to the stock price movement over a specified period.


## Usage
1. Set up Twitter API credentials by creating environment variables for `TWITTER_CONSUMER_KEY`, `TWITTER_CONSUMER_SECRET`, `TWITTER_ACCESS_TOKEN`, and `TWITTER_ACCESS_TOKEN_SECRET`.

**Twitter is now X. Yes, we need to update that one..**

2. Run the main script:
   ```sh
   python main.py
   ```
   This will fetch tweets, retrieve stock data, conduct sentiment analysis, and visualize the stock price movement.

## Data Preprocessing
The tweet data is preprocessed to remove URLs and special characters using regular expressions.

## Sentiment Analysis
Sentiment analysis is performed using the VADER (Valence Aware Dictionary and sEntiment Reasoner) sentiment analyzer, which assigns sentiment scores to each tweet.

## Visualization
The stock price movement is visualized using matplotlib to show the trend over time.

## Unit Testing
Unit tests are included to ensure the functionality of key components, such as fetching tweets, retrieving stock data, and analyzing sentiment.
