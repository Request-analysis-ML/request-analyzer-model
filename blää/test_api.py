import requests

url = 'http://localhost:5000/numbers'

#data = {'numbers': [1, 2, 3, 4, 5]}

data = pd.read_csv

response = requests.post(url, json=data)

if response.status_code == 200:
    try:
        result = response.json()
        print(result)
    except ValueError:
        print('Error: Non-JSON response returned')
else:
    print('Error: API request failed with status code ' + str(response.status_code))























"""
import numpy as np
import requests
import json

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Load data
iris = load_iris()

# Split into train and test sets using the same random state
X_train, X_test, y_train, y_test = \
    train_test_split(iris['data'], iris['target'], random_state=12)


# Serialize the data into json and send the request to the model
headers = {'Content-Type': 'application/json'}
payload = {'data': json.dumps(X_test.tolist())}
print('payload = ' , payload)
response = requests.post('http://127.0.0.1:5000/iris', headers=headers, data=payload)

print(response.content)  # print the response content

y_predict = json.loads(response.content.decode('utf-8'))

# Make array from the list
y_predict = np.array(y_predict)

print(y_predict)


# test_api.py 2
import numpy as np
import requests
import json

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()

X_train, X_test, y_train, y_test = train_test_split(iris['data'], iris['target'], random_state=12)

payload = {'data': X_test.tolist()}
y_predict = requests.post('http://127.0.0.1:5000/iris', json=payload).json()

y_predict = np.array(y_predict)
print(y_predict)

"""
