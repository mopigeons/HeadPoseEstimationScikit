__author__ = 'Simon'

from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor

#establish training data points (X) and their labels (Y)
#--------------------------------------------------------
# The current data is dummy data and needs to be replaced
#--------------------------------------------------------
X = [[0,1,0,0,0],[1,1,0,0,1], [0,0,1,1,1], [1,0,1,1,0], [0,1,0,0,1], [1,0,1,0,0], [1,1,1,0,1], [0,1,1,0,1]]
Y = [0,1,1,0,1,0,1,1]

#build the classification forest
clf = RandomForestClassifier(n_estimators=1000)
clf = clf.fit(X, Y)

#build the regression forest
reg = RandomForestRegressor(n_estimators=1000)
reg = reg.fit(X,Y)

#get classification and regression predictions for some new test data point
#---------------------------------------------------------
# Need to import new data point and translate it from
# image to matrix or array
#---------------------------------------------------------
prediction = clf.predict_proba([1,1,1,1,1])
predict2 = reg.predict([1,1,1,1,1])

#print the results on the screen
print("\nclassification")
print(prediction)
print("\nregression")
print(predict2)
