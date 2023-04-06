# app.py 2
import numpy as np
import pickle
from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('data')

with open('classifier_model.pkl', 'rb') as f:
    model = pickle.load(f)

class IrisClassifier(Resource):
    def post(self):
        args = parser.parse_args()
        x = np.array(args['data'])
        predictions = model.predict(x)
        return jsonify(predictions.tolist())

api.add_resource(IrisClassifier, '/iris')

if __name__ == '__main__':
    app.run(debug=True)


"""
class IrisClassifier(Resource):
    def post(self):
        args = parser.parse_args()
        x = np.array(json.loads(args['data']))
        predictions = model.predict(x)
        return jsonify(predictions.tolist())

    
api.add_resource(IrisClassifier, '/iris')

if __name__ == '__main__':
    # Load model
    with open('classifier_model.pkl', 'rb') as f:
        model = pickle.load(f)

    app.run(debug=True)





# load pickle model
model = pickle.load(open("classifier_model.pkl", "rb"))

@app.route("/predict", methods = {"POST"})

def predict():
    json_ = request.json
    query_df = pd.DataFrame(json_)
    predictions = model.predict(query_df)
    return jsonify({"Prediction": list(predictions)})

if __name__ == '__main__':
    app.run(debug=True)

"""