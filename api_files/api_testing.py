import requests
import json
import pandas as pd

#host = 'http://127.0.0.1:8080/anomaly'
host = 'http://127.0.0.1:5000/anomaly'

data = pd.read_csv('csv_files/datachunk.csv')
body = data.to_json(orient="records")
body = json.loads(body)

response_code = requests.post(host, json=body)
print(response_code)
response_result = json.dumps(response_code.json())
print(response_result)