from collections import defaultdict
import numpy as np
import pandas as pd
import pickle

# Load the datasets
train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

# Data Pre-processing, extracting movie and user id's and grouping
train['user_id'], train['movie_id'] = zip(*train['userId_movieId'].str.split('_'))
usersPerItem = train.groupby('movie_id')['user_id'].apply(set).to_dict()
itemsPerUser = train.groupby('user_id')['movie_id'].apply(set).to_dict()
ratingDict = dict(zip(zip(train['user_id'], train['movie_id']), train['rating']))
ratingMean = train['rating'].mean()

# Model Training
userAverages = {u: train.loc[train['user_id'] == u, 'rating'].mean() for u in itemsPerUser}
itemAverages = {i: train.loc[train['movie_id'] == i, 'rating'].mean() for i in usersPerItem}

# Using Jaccard similarity 
def jaccard(A, B):
    num = len(A.intersection(B))
    den = len(A.union(B))
    if den == 0:
        return 0
    return num / den

def mostSimilar(i, N):
    similarities = []
    if i in usersPerItem:
        users = usersPerItem[i]
        for i2 in usersPerItem:
            if i2 == i:
                continue
            sim = jaccard(users, usersPerItem[i2])
            similarities.append((sim, i2))
        similarities.sort(reverse=True)
    return similarities[:N]

def predictRating(user, item, rating):
    ratings = []
    similarities = []
    for d in train.loc[train['user_id'] == user].itertuples():
        i2 = d.movie_id
        if i2 == item:
            continue
        ratings.append(d.rating - itemAverages[i2])
        similarities.append(jaccard(usersPerItem[item], usersPerItem[i2]))
    if sum(similarities) > 0:
        weightedRatings = [(x * y) for x, y in zip(ratings, similarities)]
        return itemAverages[item] + sum(weightedRatings) / sum(similarities)
    else:
        # User hasn't rated any similar items
        return ratingMean

# Model Evaluation
trainPredictions = [predictRating(d.user_id, d.movie_id, d.rating) for d in train.itertuples()]
trainLabels = train['rating']

# Generate Movie Suggestions
def generateMovieSuggestions(user_id, input_movies, train_df, num_suggestions=5):
    # Check if user_id exists in the training dataset
    if user_id not in itemsPerUser:
        # Create a new DataFrame with the input movies and ratings
        new_rows = [{'user_id': user_id, 'movie_id': movie_id, 'rating': rating} for movie_id, rating in input_movies]
        new_df = pd.DataFrame(new_rows)
        # Concatenate the new DataFrame with the existing train_df
        train_df = pd.concat([train_df, new_df], ignore_index=True)
        # Update the itemsPerUser dictionary with the new user_id
        itemsPerUser[user_id] = set([movie_id for movie_id, _ in input_movies])
    
    similarities = []
    for movie_id, rating in input_movies:
        similar_movies = mostSimilar(movie_id, num_suggestions)
        suggestions = [(movie, predictRating(user_id, movie, rating)) for _, movie in similar_movies]
        suggestions.sort(key=lambda x: x[1], reverse=True)  # Sort suggestions by predicted rating
        similarities.extend(similar_movies)
    similarities = list(set(similarities))  # Remove duplicates
    similarities.sort(reverse=True)  # Sort similarities in descending order
    suggestions = [movie for _, movie in similarities[:num_suggestions]]  # Extract movie suggestions
    return suggestions

# Save Model
pickle.dump(predictRating, open('model.pkl', 'wb'))

# Test
user_id = 'user123'  # Replace with the user ID
input_movies = [('123', 0.93), ('456', 0.85), ('789', 0.75)]  # Replace with the input movie IDs and ratings
suggestions = generateMovieSuggestions(user_id, input_movies, train, num_suggestions=5)
print(f"Movie Suggestions for '{user_id}':")
for movie in suggestions:
    print(movie)
