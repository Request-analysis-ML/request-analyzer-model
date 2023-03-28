import numpy as np
import pandas as pd
from df_functions import clean_reqlogs
import re
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

#Function that returns a fitted CountVectorizer
def create_vectorizer(dataframe):
    df = dataframe.copy()
    cleaned = clean_reqlogs(df)
    vectorizer = CountVectorizer()
    vectorizer = vectorizer.fit(cleaned['request_logs'])
    return vectorizer

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
    #df = dataframe[['userID','URL']].copy()
    #df = df.set_index(['userID']).rename_axis(None)
    #df = df.groupby(level=0).agg(','.join)

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


# This function selects vectorizer (count or tfidf), apply it to the column 'column_name' (request_logs).
# Then it calls the fun 'test_var_instance' which returns a list with count vectorized scores.
# It then returns the variance on the list
# Params; vectorizer: count or tfidf. dataframe: what df? column_name: name of the col to count (will be request_logs)
def get_variance_score(dataframe, vectorizer):
    df = dataframe.copy()
    cleaned = clean_reqlogs(df)

    x = vectorizer.transform(cleaned['request_logs'])

    df_vectorized = pd.DataFrame(x.todense(), columns=vectorizer.get_feature_names_out())
    #return df_vectorized.sort_values(by=["vect_scores"], ascending=False)
    #list = df_vectorized.sort_values(by=["vect_scores"], ascending=False)
    return df_vectorized.iloc[0].var()


#This function is used to test an instance in the df. This resturn the list with count vectorized scores.
def test_var_instance(vectorizer, int, idk):
    vector_instance= idk[int] 
    df_vectorized = pd.DataFrame(vector_instance.T.todense(), index=vectorizer.get_feature_names_out(), columns=["vect_scores"])
    #return df_vectorized.sort_values(by=["vect_scores"], ascending=False)
    list = df_vectorized.sort_values(by=["vect_scores"], ascending=False)
    return list.var()



#OLD FUNCTION
def get_variance_score_old(dataframe, vectorizer = {'count', 'tfidf'}):
    df = dataframe.copy()
    cleaned = clean_reqlogs(df)

    if(vectorizer == 'count'):
        vectorizer = CountVectorizer()
        x = vectorizer.fit_transform(cleaned['request_logs'])
        #return x
        #return test_var_instance(vectorizer=vectorizer, int=i, idk=x)

    elif(vectorizer == 'tfidf'):
        vectorizer = TfidfVectorizer(stop_words = 'english')            #probably don't need stopwords
        x = vectorizer.fit_transform(cleaned['request_logs'])
        #return test_var_instance(vectorizer=vectorizer, int=i, idk=x)

    else:
        print('something fishy')
        return 0

    df_vectorized = pd.DataFrame(x.todense(), columns= vectorizer.get_feature_names_out() )
    #return df_vectorized.sort_values(by=["vect_scores"], ascending=False)
    #list = df_vectorized.sort_values(by=["vect_scores"], ascending=False)
    return df_vectorized.var()