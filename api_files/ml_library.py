import numpy as np
import pandas as pd
import re
from sklearn.feature_extraction.text import  CountVectorizer
import math



# *** METHODS USED FOR DATAFRAME MANIPULATIONS ***

#Function to read a csv file
def read_csv_file(csv_file):
    data = pd.read_csv(csv_file)
    data.columns = ['timestamp', 'userID', 'sessionID', 'expiring', 'URL']
    return data

#Returns a list of users
def extract_users(dataframe):
    return list(dataframe['userID'].unique())


#This function will only be used for training data
def split_user_df(dataframe, user):

    #Dataframe containing all requests made by chosen user
    user_data = dataframe.loc[dataframe['userID'] == user]
    number_of_reqs = user_data.shape[0]
   
    partitions = number_of_reqs/55
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
Function that returns a fitted CountVectorizer.
The data is cleaned with clean_reqlogs before being fitted.
:param dataframe: the dataframe to fit the vectorizer with
:returns: a CountVectorizer
"""
def create_vectorizer(dataframe):
    df = dataframe.copy()
    cleaned = clean_reqlogs(df)
    vectorizer = CountVectorizer()
    vectorizer = vectorizer.fit(cleaned['request_logs'])
    return vectorizer


# ***FOLLOWING METHODS ARE USED FOR PERFORMING CALCULATIONS ON THE PROVIDED DATA**  

"""
Function that checks the time between the requests in each chunk and calculates the mean.
:param userdata: a chunk of data from a user 
:returns: the average time between requests in seconds
"""
def calc_avg_timediff(userdata):
    #We get a list of all timestamps within the data chunk
    timestamps = userdata['timestamp'].tolist()
    timestamps = np.array(timestamps)
    
    #calculates the avarage in milliseconds
    avg_ms = np.average(np.diff(timestamps))
    
    return avg_ms/1000

"""
Function that calculates the longest streak of consecutive requests.
:param dataframe: the dataframe with a chunk of data from a user to analyze
:returns: the number of longest streak with consecutive requests
"""
def longest_consec(dataframe):
    df = dataframe.copy()
    cleaned = clean_reqlogs(df)
    requests = cleaned['request_logs'].to_list()[0]
    
    list = re.split(' ', requests)
    return recursive_consec(list, list[0], 1, 1, 1)
    

#Function that calculates length of the longest subsequence of consecutive requests 
def recursive_consec(list, last_word, longest_streak, count, i):
    if (list[i] == ''  and i < len(list)):
        return recursive_consec(list, last_word, longest_streak, count, i+1)
    if (list[i] == last_word):
        count = count + 1
    elif (count > longest_streak):
        longest_streak = count 
        count = 1     
    if(i == len(list)-1):
        return float(longest_streak)
    return recursive_consec(list, list[i], longest_streak, count, i+1)


"""
Function that returns the variance of different types of requests.
The CountVectorizer have been applied to the request to perform a BoW operation.

:param dataframe: the dataframe with a chunk of data from a user to analyze
:param vectorizer: the vectorizer to apply to count the different requests
:returns: the variance of the different requests
"""
def get_variance_score(dataframe, vectorizer):
    df = dataframe.copy()
    cleaned = clean_reqlogs(df)

    x = vectorizer.transform(cleaned['request_logs'])

    df_vectorized = pd.DataFrame(x.todense(), columns=vectorizer.get_feature_names_out())
    return df_vectorized.iloc[0].var()

"""
Function that checks the average number of sessionIDs within 5 minute windows.

:param dataframe: the dataframe with a chunk of data from a user to analyze
:returns: the average number of sessionIDs during a 5 min window
"""
def avg_tokens_5mins(dataframe):

    df = dataframe.copy()
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    data_session = pd.DataFrame()
    data_session['sessionID'] = df.set_index('timestamp').resample('5T')["sessionID"].sum()
    sessionIDs = []
    
    for i in range (0, data_session.shape[0]):
        sessionIDs.append(count_sessionIDs(data_session.iloc[i]))
    return np.average(sessionIDs) 


#Calculates time difference between first and last request in a sequence
def sequence_time_length(dataframe):
    timestamps = dataframe['timestamp'].to_list()
    diff = (timestamps[len(timestamps)-1]) - timestamps[0]
    diff = diff / 1000
    return diff

"""
Function that returns the number of unique sessionIDs.

:param dataframe: the dataframe wiht???
:returns: the number of unique sessionIDs 
"""  
#returns number of sessionIDs for a user during time intervall
def count_sessionIDs(dataframe):
    list = dataframe['sessionID']
    if (not isinstance(list, int)):
        timestamp_list = list.split(" ")
        return(len(set(timestamp_list)))
    return 0

#Function to calculate unique requests (might not use)
def count_unique_reqs(dataframe, list):
    dataframe['unique_reqs'] = np.count_nonzero(dataframe[list], axis=1)
    return dataframe

