import nltk
from textblob import TextBlob
import pandas as pd

# Ensure that NLTK resources are downloaded
nltk.download('vader_lexicon')

def analyze_sentiment(text):
    """
    Analyzes sentiment of a given text using TextBlob.
    Returns polarity score, where -1 is negative and 1 is positive.
    """
    blob = TextBlob(text)
    return blob.sentiment.polarity

def analyze_sentiments_from_file(input_file):
    """
    Analyzes sentiments from a CSV file containing tweets/text data.
    Adds sentiment scores to a DataFrame and returns it.
    """
    data = pd.read_csv(input_file)
    data['sentiment'] = data['text'].apply(analyze_sentiment)
    return data

# Example usage:
# data = analyze_sentiments_from_file("tweets.csv")
# print(data.head())
