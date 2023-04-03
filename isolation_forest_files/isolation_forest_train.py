import pandas as pd
from sklearn.ensemble import IsolationForest
import pickle

train_data = pd.read_csv('csv_files/train.csv')
test_data = pd.read_csv('csv_files/test.csv')

#anomaly_inputs = ['request_freq', 'avg_tokens', 'longest_consec', 'var_score']
anomaly_inputs = ['avg_tokens', 'var_score']


model = IsolationForest(contamination=0.002, random_state=42)
model.fit(train_data[anomaly_inputs])

df_anomaly = pd.DataFrame()
df_anomaly['anomaly_score'] = model.decision_function(test_data[anomaly_inputs])
df_anomaly['anomaly'] = model.predict(test_data[anomaly_inputs])
df_anomaly['user'] = test_data['user']

#Only for visualizing
df_a = df_anomaly.loc[df_anomaly['anomaly']==-1] 
print(df_a)

# Save model
with open('model.pickle', 'wb') as f:
    pickle.dump(model, f)


