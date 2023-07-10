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
        
        prediction = movie_predict.generateMovieSuggestions(user_id, X.items())
        console.log(prediction)
        return jsonify(prediction)
    else:
        return 'Content-Type not supported!'



if __name__ == '__main__':
    # Load model
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    print('Model loaded')
    app.run(debug=True, port=3000)
