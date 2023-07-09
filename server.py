from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
import pickle
import numpy as np
import json
import movie_predict

app = Flask(__name__)
api = Api(app)

# Create parser for the payload data
parser = reqparse.RequestParser()
parser.add_argument('data')

# Define how the api will respond to the post requests
class MoviePredicter(Resource):
    def post(self):
        args = parser.parse_args()
        X = np.array(json.loads(args['data']))
        prediction = model.predictRating(X)
        return jsonify(prediction.tolist())

api.add_resource(MoviePredicter, '/predict')

if __name__ == '__main__':
    # Load model
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    print('Model loaded')
    app.run(debug=True)