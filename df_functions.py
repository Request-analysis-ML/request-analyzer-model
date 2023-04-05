import pandas as pd
import re
import numpy as np
import math


#Function to read a csv file
def read_csv_file(csv_file):
    data = pd.read_csv(csv_file)
    data.columns = ['timestamp', 'userID', 'sessionID', 'expiring', 'URL']
    return data


#Returns a list of users - probably not necessary 
def extract_users(dataframe):
    return list(dataframe['userID'].unique())


#This function will only be used for training data
def split_user_df(dataframe, user):

    #Dataframe containing all requests made by chosen user
    user_data = dataframe.loc[dataframe['userID'] == user]
    number_of_reqs = user_data.shape[0]
   
    partitions = number_of_reqs/15
    partitions = math.ceil(partitions)

    #Splits the data frame into smaller chunks of ~50 requests
    return  np.array_split(user_data, partitions)
  

#Removing all non-letter characters from the data and assigning it to new data frame 'df_cleaned'
def clean_reqlogs(dataframe):

    df = dataframe[['userID','URL']].copy()
    df = df.set_index(['userID']).rename_axis(None)
    df = df.groupby(level=0).agg(','.join)

    request_logs = df['URL']

    cleaned_logs = []

    for i in range(0, len(request_logs)):
        sequence = re.sub('\d', '', request_logs[i])
        sequence = re.sub(',', ' ', sequence)
        sequence = sequence.lower()
        cleaned_logs.append(sequence)

    df['request_logs'] = cleaned_logs
    df = df.drop('URL', axis=1)

    return df  











"""
for all users:
    send all rows into "distributer function" from og dataframe where user = user.
    Group this users information in 5 minute sequences (we define a sequence as 5 minutes) as aggregate(?).
    For all 5min sequences:
        send appropriate date to all analysing functions
        send this information back here (how will this look?)
    4. construct this back into one "long row of features"
    5. send back



Analyse with Isolation Forest



The code below are old methods which are not used

#Returns a dataframe containing only timestamp, URL or timestamp+sessionID column. 
#The data is grouped based on userID
def format_data(dataframe, column = {'timestamp', 'URL', 'sessionID'}):
    new_frame = dataframe
    allUsers = new_frame.set_index(['userID']).rename_axis(None)
    if (column == 'URL'):
        allUsers = allUsers.drop(columns=['timestamp', 'sessionID', 'expiring'])

    elif (column == 'timestamp'):
        allUsers = allUsers.drop(columns=['URL', 'sessionID', 'expiring'])
    elif (column == 'sessionID'):
        allUsers = allUsers.drop(columns=['URL', 'expiring'])    
    df = allUsers.groupby(level=0).agg(','.join)
    df.reset_index(inplace=True)
    df = df.rename(columns={'index': 'users'})    
    return df

#Returns a list of number of requests every 5 minutes
def reqs_per_5mins(dataframe):
    new_df = pd.DataFrame()
    new_df['timestamp'] = pd.to_datetime(dataframe['timestamp'], unit='ms')
    new_df['val'] = 1

    new_df = new_df.set_index('timestamp')
    new_df = new_df.resample('5min').sum()

    return new_df['val'].to_list()


#Function that splits dataframe into smaller chunks, calls format_data on each and then re-assemble the dataframe
def split_and_reformat(dataframe, column = {'timestamp', 'URL', 'sessionID'}):

    new_df = dataframe.sort_values(by=['timestamp'])

    reqs_per_5 = reqs_per_5mins(dataframe)
    lower = 0
    df_concat = pd.DataFrame()

    for i in range(0, len(reqs_per_5)):
        higher = reqs_per_5[i]
        df_split = new_df.iloc[lower:higher]
        df_split = format_data(df_split, column)
        df_concat = pd.concat([df_concat, df_split])
        lower = reqs_per_5[i]

    df_concat.reset_index(inplace=True)
    df_concat = df_concat.drop(columns=['index'])
    return df_concat
"""