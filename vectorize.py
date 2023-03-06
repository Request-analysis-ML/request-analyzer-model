from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

class vectorizer:

    def __init__(self, vectorizer = {'count', 'tfidf'}):

        if (vectorizer == 'tfid'):
            self.vectorizer = TfidfVectorizer()
        else:
            self.vectorizer = CountVectorizer()            


    def vectorize_data(self, df_col):
        return self.vectorizer.fit_transform(df_col)        

    def get_feature_names(self):
        return self.vectorizer.get_feature_names_out()