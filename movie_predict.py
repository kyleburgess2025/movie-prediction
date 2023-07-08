from collections import defaultdict
import numpy as np
import pandas as pd
import pickle
from sklearn.metrics import mean_squared_error

# Load the datasets
train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

# Data Pre-processing
train['user_id'], train['movie_id'] = zip(*train['userId_movieId'].str.split('_'))
usersPerItem = train.groupby('movie_id')['user_id'].apply(set).to_dict()
itemsPerUser = train.groupby('user_id')['movie_id'].apply(set).to_dict()
ratingDict = dict(zip(zip(train['user_id'], train['movie_id']), train['rating']))
ratingMean = train['rating'].mean()

# Model Training
userAverages = {u: train.loc[train['user_id'] == u, 'rating'].mean() for u in itemsPerUser}
itemAverages = {i: train.loc[train['movie_id'] == i, 'rating'].mean() for i in usersPerItem}

def jaccard(s1, s2):
    numer = len(s1.intersection(s2))
    denom = len(s1.union(s2))
    if denom == 0:
        return 0
    return numer / denom

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

def predictRating(user, item):
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
trainPredictions = [predictRating(d.user_id, d.movie_id) for d in train.itertuples()]
trainLabels = train['rating']
trainRMSE = mean_squared_error(trainPredictions, trainLabels, squared=False)
print(f"Train RMSE: {trainRMSE:.4f}")

# Generate Movie Suggestions
def generateMovieSuggestions(movie_id, num_suggestions=10):
    similar_movies = mostSimilar(movie_id, num_suggestions)
    return [movie for _, movie in similar_movies]

# Save the Trained Model
pickle.dump(predictRating, open('model.pkl', 'wb'))

# Example usage
movie_id = '123'  # Replace with the movie ID for which you want suggestions
suggestions = generateMovieSuggestions(movie_id)
print(f"Movie Suggestions for '{movie_id}':")
for movie in suggestions:
    print(movie)
