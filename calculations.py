import numpy as np
from df_functions import clean_reqlogs
import re

#Function to check the time between the requests in each chunk and calculate the mean
def calc_avg_timediff(userdata):
    #We get a list of all timestamps within the data chunk
    timestamps = userdata['timestamp'].tolist()
    timestamps = np.array(timestamps)
    
    #calculates the avarage in milliseconds
    avg_ms = np.average(np.diff(timestamps))
    
    return avg_ms/1000

#
def longest_consec(dataframe):
    df = dataframe[['userID','URL']].copy()
    df = df.set_index(['userID']).rename_axis(None)
    df = df.groupby(level=0).agg(','.join)

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

