# Import Library
import numpy
import sklearn
import scipy
import pandas
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.svm import LinearSVC
from sklearn.multiclass import OneVsOneClassifier
from sklearn.multiclass import OutputCodeClassifier
from sklearn.multiclass import OneVsRestClassifier


# Read data from csv file
data = pandas.read_csv("data.csv");
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
# svm = OneVsOneClassifier(LinearSVC(random_state=0));
svm = OneVsRestClassifier(LinearSVC(random_state=0));
# svm = OutputCodeClassifier(LinearSVC(random_state=0), code_size=2, random_state=0)

svm.fit(x_train, y_train);

# Testfrom sklearn.metrics import classification_report, confusion_matrix
y_pred = svm.predict(x_test);

# Report
print('Binary Classifier');
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
print(svm.score(x_test, y_test));# accuracy


# SVM kernel multi-class
# svm2 = OneVsOneClassifier(LinearSVC(random_state=0));
svm2 = OneVsRestClassifier(LinearSVC(random_state=0));
# svm2 = OutputCodeClassifier(LinearSVC(random_state=0), code_size=2, random_state=0)

svm2.fit(x_train2, y_train2);

# Testfrom sklearn.metrics import classification_report, confusion_matrix
y_pred2 = svm2.predict(x_test2);

# Report
print('\n\nMulti-class Classifier');
print(confusion_matrix(y_test2,y_pred2))
print(classification_report(y_test2,y_pred2))
print(svm2.score(x_test2, y_test2));# accuracy