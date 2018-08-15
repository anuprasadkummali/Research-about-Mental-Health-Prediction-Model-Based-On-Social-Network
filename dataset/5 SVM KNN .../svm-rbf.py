# Import Library
import numpy
import sklearn
import scipy
import pandas
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix


# Read data from csv file
data = pandas.read_csv("data6.csv"); # switch for data.csv or data6.csv
# print(data.head());

# Divide data into training data and ground truth
X = data.drop('QN', axis=1).drop('ground_truth', axis=1).drop('ground_truth_binary', axis=1);
Y2 = data['ground_truth']; # full categorical ground truth
Y = data['ground_truth_binary']; # binary ground truth

# print(X.head());
# print(Y);
# print(Y2);

# Split dataset into training set and testing set
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.3);
x_train2, x_test2, y_train2, y_test2 = train_test_split(X, Y2, test_size = 0.3);

# SVM kernel
# svm = SVC(kernel='linear', C=100);
#svm = SVC(kernel='rbf',gamma=0.05, C=1); # best for data.csv
svm = SVC(kernel='rbf',gamma=10, C=1);
# svm = SVC(kernel='poly', degree=6, C=80);
svm.fit(x_train, y_train);

# Testfrom sklearn.metrics import classification_report, confusion_matrix
y_pred = svm.predict(x_test);

# Report
print('Binary Classifier');
print(confusion_matrix(y_test,y_pred));
print(classification_report(y_test,y_pred));
print(svm.score(x_test, y_test));# accuracy


# SVM kernel multi-class
# svm2 = SVC(kernel='linear', C=100);
#svm2 = SVC(kernel='rbf',gamma=0.05, C=1); # best for data.csv
svm2 = SVC(kernel='rbf',gamma=10, C=1);
# svm2 = SVC(kernel='poly', degree=6, C=80);
svm2.fit(x_train2, y_train2);

# Testfrom sklearn.metrics import classification_report, confusion_matrix
y_pred2 = svm2.predict(x_test2);

# Report
print('\n\nMulti-class Classifier');
print(confusion_matrix(y_test2,y_pred2));
print(classification_report(y_test2,y_pred2));
print(svm2.score(x_test2, y_test2));# accuracy
