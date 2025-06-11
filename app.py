# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("elon_musk_tweets_with_sentiment.csv")

st.title("Elon Musk Tweet Sentiment Analysis")

# Pie Chart
sentiment_counts = df['sentiment'].value_counts()
st.subheader("Sentiment Distribution")
st.bar_chart(sentiment_counts)

# Show data
if st.checkbox("Show raw data"):
    st.write(df)
