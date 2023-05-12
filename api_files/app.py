from ml_library import longest_consec, calc_avg_timediff, get_variance_score, avg_tokens_5mins, sequence_time_length
from flask import Flask, request
import pickle
import json
import pandas as pd


app = Flask(__name__)

@app.route('/anomaly', methods=['POST'])
def detect_anomaly():
    req_data = json.loads(request.data)
    df = pd.DataFrame(req_data)

    seq_length = df.shape[0]
    user = df.loc[0,'userID']

    #TODO add error in case too many requests are sent in

    data = {'request_freq': [calc_avg_timediff(df),],
            'avg_tokens': [avg_tokens_5mins(df),],
            'longest_consec': [longest_consec(df),],
            'var_score': [get_variance_score(df, vect),],
            'sequence_time': [sequence_time_length(df),]}
    
    user_df = pd.DataFrame(data) 

    #Short sequences
    if (seq_length < 40):
        model = pickle.load(open('api_files/model30.pickle', 'rb'))
        anomaly_score = model.decision_function(user_df.values)
        if (anomaly_score < 0):
            df_anomaly = pd.DataFrame({'user':[user], 'action':['verify']})

        else:
            df_anomaly = pd.DataFrame({'user':[user], 'action':['OK']})
    #Long sequences
    else:  
        model = pickle.load(open('api_files/model60.pickle', 'rb'))      
        anomaly_score = model.decision_function(user_df.values)
        if (anomaly_score < 0):
            df_anomaly = pd.DataFrame({'user':[user], 'action':['block']})
        else:
            df_anomaly = pd.DataFrame({'user':[user], 'action':['OK']})
    
    return df_anomaly.to_json(orient='records') 


if __name__ == '__main__':    
    with open('api_files/vect.pickle', 'rb') as f:  
        vect = pickle.load(f)

    #Use this only when running api with the composer        
    #app.run(debug=True, host= "172.20.0.41", port=8090,use_reloader=False) 
    
    #Use this when running locally
    app.run(debug=True, host= "0.0.0.0", port=8090,use_reloader=False)