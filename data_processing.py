import pandas as pd

def preprocess_data(input_file):
    """
    Preprocesses data to ensure consistency and removes null entries.
    """
    data = pd.read_csv(input_file)
    data.dropna(subset=['text'], inplace=True)  # Remove rows with missing text
    data['text'] = data['text'].str.strip()    # Strip leading/trailing spaces
    return data

# Example usage:
# clean_data = preprocess_data("tweets.csv")
