import pandas as pd
from sklearn.ensemble import IsolationForest
from ml_library import create_vectorizer, read_csv_file
import pickle
from sklearn.feature_extraction.text import HashingVectorizer

vect_hash = HashingVectorizer(norm=None, alternate_sign=False)

#Creating train data
train_data30 = pd.read_csv('csv_files/train30.csv')
train_data60 = pd.read_csv('csv_files/train60.csv')

test_data = pd.read_csv('csv_files/test.csv')

anomaly_inputs = ['request_freq', 'avg_tokens', 'longest_consec', 'var_score', 'sequence_time']
#anomaly_inputs = ['avg_tokens', 'var_score']

#Training two models
model30 = IsolationForest(contamination=0.002, random_state=42)
model30.fit(train_data30[anomaly_inputs].values)

model60 = IsolationForest(contamination=0.002, random_state=42)
model60.fit(train_data60[anomaly_inputs].values)

""""
df_anomaly = pd.DataFrame()
df_anomaly['anomaly_score'] = model.decision_function(test_data[anomaly_inputs].values)
df_anomaly['anomaly'] = model.predict(test_data[anomaly_inputs].values)
df_anomaly['user'] = test_data['user']

#Only for visualizing
df_a = df_anomaly.loc[df_anomaly['anomaly']==-1] 
print(df_a)
"""

# Save models
with open('api_files/model30.pickle', 'wb') as f:
    pickle.dump(model30, f)
with open('api_files/model60.pickle', 'wb') as f:
    pickle.dump(model60, f)    

# Save vectorizer
with open('api_files/vect.pickle', 'wb') as f:
    pickle.dump(vect_hash, f)    
    


