"""Python file containing methods for splitting the data into train and test data sets. """

import pandas as pd

#Function that extracts spammers and scrapers from original data set
def extract_spammers_scrapers(dataframe):
    return dataframe.loc[(dataframe['user'] == ' user-1003') | 
                         (dataframe['user'] == ' user-1004') | 
                         (dataframe['user'] == ' user-1005')]

#Function that returns all normal users (used after extracting spammers and scrapers)
def extract_normal(dataframe, df_spam):
    return dataframe.drop(df_spam.index)



def split_train_test(df_normal, df_spam):

    #Divide normal users in train and test data
    df_train_normal = df_normal.sample(frac = 0.8)
    df_test_normal = df_normal.drop(df_train_normal.index)

    #Divide spammers and webscrapers in train and test data
    df_train_spammers = df_spam.sample(frac = 0.002)
    df_test_spammers = df_spam.drop(df_train_spammers.index)

    #Merge all data into one training and one testing data set
    df_train = pd.concat([df_train_spammers, df_train_normal])
    df_test = pd.concat([df_test_spammers, df_test_normal])

    df_train.to_csv('csv_files/train.csv', index=False) 
    df_test.to_csv('csv_files/test.csv', index=False)