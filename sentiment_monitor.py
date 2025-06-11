from transformers import pipeline

# Load the sentiment-analysis model
sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    result = sentiment_pipeline(text)
    return result[0]

if __name__ == "__main__":
    print("Brand Sentiment Monitor")
    sample_text = input("Enter your brand review or comment: ")
    sentiment = analyze_sentiment(sample_text)
    print(f"\nSentiment: {sentiment['label']}")
    print(f"Confidence: {round(sentiment['score'] * 100, 2)}%")
