from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
import pickle
import numpy as np
import json


app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('data')


class anomaly_detector(Resource):
    def post(self):
        args = parser.parse_args()
        X = np.array(json.loads(args['data']))
        prediction = model.predict(X)
        print(prediction)
        return jsonify(prediction.tolist())
    
api.add_resource(anomaly_detector, '/spam_detect')

if __name__ == '__main__':
    with open('model.pickle', 'rb') as f:  
        model = pickle.load(f)
    app.run(debug=True)





"""
app = Flask(__name__)

# Load the model
model = pickle.load(open('model.pickle','rb'))

@app.route('/spam_detect', methods=['POST'])
def spam_detect():
    # Get the data from the POST request.
    data = Request.get_json(force=True)
    data = json.loads(data)
    data = list(data.items())
    data = list(zip(*data))
    data = np.asarray(data[1])

    # Make prediction using model loaded from disk as per the data.
    prediction = model.predict(data)
    # Take the first value of prediction
    output = prediction
    return jsonify(output)

if __name__ == '__main__':
    app.run(port=5000, debug=True)

"""    