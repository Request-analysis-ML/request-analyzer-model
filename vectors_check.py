import pandas as pd
import re

#the two functions below are just to assemble and simulate a batch of request from one user
def read_csv_file(csv_file):
    data = pd.read_csv(csv_file)
    data.columns = ['timestamp', 'userID', 'sessionID', 'expiring', 'URL']
    return data


def group_data(dataframe):
    data_grouped = dataframe.groupby('userID').agg(lambda x: ', '.join(x.astype(str))).reset_index()
    return data_grouped

def format_for_url(dataframe):
    return dataframe.drop(columns = ['timestamp', 'sessionID', 'expiring'])

def clean_reqlogs(dataframe):

    df_cleaned = dataframe
    request_logs = df_cleaned['URL']
    cleaned_logs = []

    for i in range(0, len(request_logs)):
        sequence = re.sub('\d', '', request_logs[i])
        sequence = re.sub(',', ' ', sequence)
        sequence = sequence.lower()
        cleaned_logs.append(sequence)

    df_cleaned ['request_logs'] = cleaned_logs
    df_cleaned = df_cleaned.drop('URL', axis=1)

    return df_cleaned  


