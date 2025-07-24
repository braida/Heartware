import pandas as pd

def recommend_content(user_id, sentiment_data, well_being_relevance=0.6):
    """
    Recommends content to a user based on their sentiment history.
    """
    user_data = sentiment_data[sentiment_data['user_id'] == user_id]
    if user_data.empty:
        print(f"No data found for user {user_id}")
        return None
    
    # Calculate average sentiment score for the user
    avg_sentiment = user_data['sentiment'].mean()

    # Content recommendation based on sentiment
    if avg_sentiment > 0:
        print(f"Recommending positive content to user {user_id}")
    else:
        print(f"Recommending uplifting or neutral content to user {user_id}")
    
    # Placeholder for actual content recommendation logic (e.g., API calls, etc.)
    return user_data

# Example usage:
# user_data = recommend_content(1234, sentiment_data)
