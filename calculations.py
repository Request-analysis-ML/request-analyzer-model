import numpy as np
import pandas as pd
from df_functions import clean_reqlogs
import re
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer



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
        return longest_streak
    return recursive_consec(list, list[i], longest_streak, count, i+1)





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






