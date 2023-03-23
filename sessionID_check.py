import pandas as pd
import numpy as np

#the two functions is just to assemble and simulate a batch of request from one user
def read_csv_file(csv_file):
    data = pd.read_csv(csv_file)
    data.columns = ['timestamp', 'userID', 'sessionID', 'expiring', 'URL']
    return data

#group all column values based on userID
def group_data(dataframe):
    data_grouped = dataframe.groupby('userID').agg(lambda x: ', '.join(x.astype(str))).reset_index()
    return data_grouped

#returns number of sessionIDs for a user during time intervall
def count_sessionIDs(dataframe):
    list = dataframe['sessionID']
    if (not isinstance(list, int)):
        timestamp_list = list.split(" ")
        return(len(set(timestamp_list)))
    return 0

#Function that checks the average number of sessionIDs within 5 minute windows for the given dataframe  
def avg_tokens_5mins(dataframe):

    df = dataframe.copy()
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    data_session = pd.DataFrame()
    data_session['sessionID'] = df.set_index('timestamp').resample('5T')["sessionID"].sum()
    sessionIDs = []
    
    for i in range (0, data_session.shape[0]):
        sessionIDs.append(count_sessionIDs(data_session.iloc[i]))
    return np.average(sessionIDs) 

    #return np.average(token_recursion(sessionIDs, data_session, 0))

#recursive function?
def token_recursion(list, dataframe, i):
    if (i <= dataframe.shape[0]-1):
        list.append(count_sessionIDs(dataframe.iloc[i]))
        return token_recursion(list, dataframe, i+1)
    return list
