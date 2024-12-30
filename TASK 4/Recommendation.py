import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
# User-Movie Ratings Matrix
data = {
    "User": ["User1", "User1", "User2", "User2", "User3", "User3", "User4"],
    "Movie": ["Inception", "Titanic", "Inception", "Avatar", "Titanic", "Avatar", "Inception"],
    "Rating": [5, 4, 4, 5, 5, 4, 3],
}

df = pd.DataFrame(data)
user_movie_matrix = df.pivot_table(index="User", columns="Movie", values="Rating").fillna(0)
# Compute cosine similarity between users
user_similarity = cosine_similarity(user_movie_matrix)
user_similarity_df = pd.DataFrame(user_similarity, index=user_movie_matrix.index, columns=user_movie_matrix.index)
def recommend_movies(user, user_movie_matrix, user_similarity_df, top_n=2):
    similar_users = user_similarity_df[user].sort_values(ascending=False).index[1:]
    similar_users_ratings = user_movie_matrix.loc[similar_users]
    weighted_ratings = similar_users_ratings.T.dot(user_similarity_df[user][similar_users])
    recommendations = weighted_ratings[~user_movie_matrix.loc[user].astype(bool)].sort_values(ascending=False)
    return recommendations.head(top_n)

# Example: Recommend movies for User1
recommendations = recommend_movies("User1", user_movie_matrix, user_similarity_df)
print(recommendations)
