from calculations import longest_consec, calc_avg_timediff, get_variance_score, avg_tokens_5mins, sequence_time_length
from flask import Flask, request
import pickle
import json
import pandas as pd


app = Flask(__name__)


#data  = pd.read_csv('csv_files/datachunk.csv')
data = pd.read_csv('api_files/datachunk.csv')
data = data.to_json(orient="records")


@app.route('/', methods=['GET'])
def welcome():
    return 'Hello!' 


@app.route('/anomaly', methods=['GET'])
def get_anomaly():
    dict = json.loads(data)
    df = pd.DataFrame(dict)
    return df.to_json(orient="records")
    #pred = model.predict(df)
    #return jsonify(pred.tolist())
  

@app.route('/anomaly', methods=['POST'])
def detect_anomaly():
    req_data = json.loads(request.data)
    df = pd.DataFrame(req_data)

    data = {'request_freq': [calc_avg_timediff(df),],
            'avg_tokens': [avg_tokens_5mins(df),],
            'longest_consec': [longest_consec(df),],
            'var_score': [get_variance_score(df, vect),],
            'sequence_time': [sequence_time_length(df),]}
    user_df = pd.DataFrame(data)

    df_anomaly = pd.DataFrame()
    df_anomaly['anomaly_score'] = model.decision_function(user_df)
    df_anomaly['anomaly'] = model.predict(user_df)
    df_anomaly['user'] = df['userID'].iloc[0]

    return df_anomaly.to_json(orient='index')
  

if __name__ == '__main__':
    with open('model.pickle', 'rb') as f:  
        model = pickle.load(f)
    with open('vect.pickle', 'rb') as f:  
        vect = pickle.load(f)    
    app.run(debug=True ,port=8080,use_reloader=False)
