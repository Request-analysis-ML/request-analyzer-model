from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load Iris data
iris = load_iris()

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(iris['data'], iris['target'], random_state=12)

# Train the model
clf = RandomForestClassifier(random_state=12)
clf.fit(X_train, y_train)

# Make prediction on the test set
y_predict = clf.predict(X_test)
print(y_predict)

# Save model
with open('classifier_model.pkl', 'wb') as f:
    pickle.dump(clf, f)


















"""
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

iris = load_iris()
#print(iris)
x, y= iris.data, iris.target

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=123)

sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

classifier = RandomForestClassifier()

# fit model
classifier.fit(x_train, y_train)


# make prediction on test set
y_predict = classifier.predict(x_test)
print(y_predict)

# make pickle file of the classifier model
pickle.dump(classifier, open("classifier_model.pkl", "wb"))
"""