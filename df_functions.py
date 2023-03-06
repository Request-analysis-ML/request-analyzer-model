import pandas as pd
import re
import numpy as np
from itertools import groupby


#Function to read a csv file
def read_csv_file(csv_file):
    data = pd.read_csv(csv_file)
    data.columns = ['timestamp', 'userID', 'sessionID', 'expiring', 'URL']
    return data


#Returns a list of users
def extract_users(dataframe):
    return list(dataframe['users'])


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


#Removing all non-letter characters from the data and assigning it to new data frame 'df_cleaned'
# 5 and 6: spammers, 7: data scraper
#print(cleaned_logs[7])
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

#Function to calculate the variance of the values in the different columns
#Returns the dataframe with a column with variances added
def calculate_variance(dataframe, list):
    dataframe['var_reqs'] = dataframe[list].apply(lambda row: row.var(), axis=1)
    return dataframe


#Function to calculate unique requests
def count_unique_reqs(dataframe, list):
    dataframe['unique_reqs'] = np.count_nonzero(dataframe[list], axis=1)
    return dataframe


#Function that calculates length of the longest subsequence of consecutive requests DOES NOT WORK
def longestConsecutive(string):
    list = re.split(' ', string) 
    return recursive(list, list[0], 1, 1, 1)


#Function that calculates length of the longest subsequence of consecutive requests DOES NOT WORK
# Need shorter sequences of requests
def recursive(list, last_word, longest_streak, count, i):
    if (list[i] == ''  and i < len(list)):
        return recursive(list, list[i], longest_streak, count, i+1)
    if (list[i] == last_word):
        count = count + 1
    elif (count > longest_streak):
        longest_streak = count 
        count = 1     
    if(i == len(list)):
        return longest_streak
    return recursive(list, list[i], longest_streak, count, i+1)