from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse
import pickle
import numpy as np
import json
import movie_predict
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def process_json():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.get_json()
        X = json["data"]
        print(X)
        user_id = json["user_id"]
        
        prediction = movie_predict.generateMovieSuggestions(user_id, X)
        prediction = [getMovieById(id) for id in prediction]
        return jsonify(prediction)
    else:
        return 'Content-Type not supported!'



if __name__ == '__main__':
    # Load model
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    print('Model loaded')
    app.run(debug=True, port=3000)

def getMovieById(id):
    base = "https://letterboxd.com/tmdb/" + id
    response = requests.get(base)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.find('h1', class_='headline-1').text
