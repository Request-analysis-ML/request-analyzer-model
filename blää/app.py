from flask import Flask, jsonify, request
import pandas as pd


app = Flask(__name__)


data_csv = pd.read_csv('csv_files/calculations.csv')
data = data_csv.to_json(orient="records")

@app.route('/test')
def test():
    return 'This is a test.'





@app.route('/', methods=['GET'])
def welcome():
    return 'Hello!' 


@app.route('/data', methods=['GET'])
def print_data():
    return data


@app.route('/numbers', methods=['POST'])
def print_nr():
    req_data = request.get_json()
    num = req_data['numbers']
    return num


"""
@app.route('/predict', methods=['POST'])

def predict(numbers):

    req_data = request.get_json()
    # extract numbers list from request payload
    numbers = req_data['numbers']
    # calculate the sum of the numbers
    result = sum(numbers)
    # create a dictionary containing the result
    response = {'result': result}
    # return the result as a JSON response
    return jsonify(response)

"""


if __name__ == '__main__':
    app.run(debug = True)