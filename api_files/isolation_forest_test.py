import numpy as np
import pandas as pd
import requests
import json

train_data = pd.read_csv('csv_files/train.csv')
test_data = pd.read_csv('csv_files/test.csv')

#anomaly_inputs = ['request_freq', 'avg_tokens', 'longest_consec', 'var_score']
anomaly_inputs = ['avg_tokens', 'var_score']
test_data = test_data[anomaly_inputs].iloc[0].tolist()

payload = {'data':json.dumps(test_data)}
pred = requests.post('http://127.0.0.1:5000/spam_detect', headers={'Content-Type': 'application/json'}, data=payload).json()

# Make array from the list
pred = np.array(pred)
print(pred)

print('Creating branch to test api stuff with')