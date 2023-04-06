#import pandas as pd

#df = pd.read_csv('blää/Iris.csv')
#print(df.head())
#x = df[["SepalWidhtCm", "PetalLengthCm", "PetalWidthCm"]]

import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

iris = load_iris()
x, y= iris.data, iris.target

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=123)

sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

classifier = RandomForestClassifier()

# fit model
classifier.fit(x_train, y_train)

# make pickle file of the classifier model
pickle.dump(classifier, open("classifier_model.pkl", "wb"))