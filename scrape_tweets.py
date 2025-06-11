import snscrape.modules.twitter as sntwitter
import ssl
import certifi
import os

# Manually set SSL context
ssl._create_default_https_context = ssl.create_default_context(cafile=certifi.where())

# Search query
query = "Apple"
max_results = 5

for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
    print(f"{i+1}. {tweet.date} - @{tweet.user.username}: {tweet.content}\n")
    if i + 1 >= max_results:
        break
