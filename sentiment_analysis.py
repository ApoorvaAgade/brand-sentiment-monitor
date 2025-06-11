import pandas as pd
from transformers import pipeline

# Load your CSV file (make sure the filename matches your saved file)
df = pd.read_csv('elon_musk_tweets.csv')

# Initialize the Hugging Face sentiment-analysis pipeline
sentiment_analyzer = pipeline('sentiment-analysis')

# Replace 'content' with the column name in your CSV where tweets are stored
df['sentiment'] = df['Text'].apply(lambda tweet: sentiment_analyzer(tweet)[0]['label'])

# Save the new CSV with sentiment results
df.to_csv('elon_musk_tweets_with_sentiment.csv', index=False)

print("Sentiment analysis complete. Results saved to elon_musk_tweets_with_sentiment.csv")
