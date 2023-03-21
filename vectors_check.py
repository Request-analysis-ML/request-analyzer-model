import pandas as pd
import re
import string

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



#this function takes "one row" from the df. This will be an instance irl, i.e. one row
def clean_url_log(dataframe):
   pattern = r"\/\d+"
   urls = dataframe['URL'].split(', ')
   for i, url in enumerate(urls):
     urls[i] = re.sub(pattern, "", url)
   dataframe['URL'] = ', '.join(urls)
   return urls






