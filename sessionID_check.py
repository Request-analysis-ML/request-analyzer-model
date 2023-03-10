import pandas as pd

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
    list = dataframe['timestamp']
    timestamp_list = list.split(", ")
    return(len(set(timestamp_list)))
