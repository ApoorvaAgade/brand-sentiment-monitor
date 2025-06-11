import pandas as pd
from transformers import pipeline

# Load your tweets
df = pd.read_csv("tweets.csv")

# Load sentiment pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

# Analyze sentiment for each tweet
df['Sentiment'] = df['content'].apply(lambda x: sentiment_pipeline(x)[0]['label'])
df['Confidence'] = df['content'].apply(lambda x: sentiment_pipeline(x)[0]['score'])

# Save results
df.to_csv("tweets_with_sentiment.csv", index=False)

print("✅ Sentiment analysis complete. Results saved to tweets_with_sentiment.csv")
