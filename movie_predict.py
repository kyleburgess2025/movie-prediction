from collections import defaultdict
import numpy as np
import pandas as pd
import pickle
from sklearn.metrics import mean_squared_error

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

#For references: RMSE is 0.1606
#trainRMSE = mean_squared_error(trainPredictions, trainLabels, squared=False)
#print(f"Train RMSE: {trainRMSE:.4f}")

# Generate Movie Suggestions
def generateMovieSuggestions(movie_id, rating, num_suggestions=5):
    similar_movies = mostSimilar(movie_id, num_suggestions)
    suggestions = [(movie, predictRating('user_id', movie, rating)) for _, movie in similar_movies]
    suggestions.sort(key=lambda x: x[1], reverse=True)  # Sort suggestions by predicted rating
    return suggestions[:num_suggestions]  # Return only the highest rated movies

# Save the Trained Model
pickle.dump(predictRating, open('model.pkl', 'wb'))

# Example, user provides a movie they watched and the rating they gave it
movie_id = '123'  # Replace with the movie ID for which you want suggestions
rating = 0.93
suggestions = generateMovieSuggestions(movie_id, rating)
print(f"Movie Suggestions for '{movie_id}':")
for movie, predicted_rating in suggestions:
    print(f"Movie: {movie} | Predicted Rating: {predicted_rating:.2f}")