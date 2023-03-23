import pandas as pd
import re
import string
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer


"""
This code contains methods which will clean a string of URLs and perform
vectorizing operations.

NOTE: the two first methods 'read_csv_file' and 'group_data' is only for testing purposes. will be deleted.

We have two different vectorizers:

    - tf-idf: we vectorize the URLs with the tf-idf vectorizer. The scores
              will be used for calculating the variance. A high variance means that
              the data points are very spread out from the mean, and from one another.
              (Might want to look at standard deviation instead?)

    - count: we vectorize the URLs with the count vectorizer. This counts how many times
             a url path is used. Url 'words' with high scores indicate they are used a lot.



"""


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



# This function selects vectorizer (count or tfidf), apply it to the column 'column_name' (request_logs).
# Then it calls the fun 'test_var_instance' which returns a list with count vectorized scores.
# It then returns the variance on the list
# Params; vectorizer: count or tfidf. dataframe: what df? column_name: name of the col to count (will be request_logs)
def get_variance_score(vectorizer, dataframe, column_name, i):
    
    if(vectorizer == 'count'):
        vectorizer = CountVectorizer()
        x = vectorizer.fit_transform(dataframe[column_name])
        #return x
        return test_var_instance(vectorizer=vectorizer, int=i, idk=x)

    if(vectorizer == 'tfidf'):
        vectorizer = TfidfVectorizer(stop_words = 'english')            #probably don't need stopwords
        x = vectorizer.fit_transform(dataframe[column_name])
        return test_var_instance(vectorizer=vectorizer, int=i, idk=x)

    else:
        print('something fishy')


#This function is used to test an instance in the df. This resturn the list with count vectorized scores.
def test_var_instance(vectorizer, int, idk):
    vector_instance= idk[int] 
    df_vectorized = pd.DataFrame(vector_instance.T.todense(), index=vectorizer.get_feature_names_out(), columns=["vect_scores"])
    #return df_vectorized.sort_values(by=["vect_scores"], ascending=False)
    list = df_vectorized.sort_values(by=["vect_scores"], ascending=False)
    return list.var()

