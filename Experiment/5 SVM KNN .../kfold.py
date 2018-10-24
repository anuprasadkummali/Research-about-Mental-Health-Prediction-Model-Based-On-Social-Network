# Import Library
import numpy as np
import sklearn
import scipy
import pandas
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import KFold, RepeatedKFold
from sklearn import metrics
from sklearn.model_selection import cross_val_score, cross_val_predict
from sklearn.metrics import (brier_score_loss, precision_score, recall_score, f1_score)
from sklearn.metrics import precision_recall_fscore_support

# Read data from csv file #
data = pandas.read_csv("data.csv");
# print(data.head());

# Divide data into training data and ground truth #
X = data.drop('QN', axis=1).drop('ground_truth', axis=1).drop('ground_truth_binary', axis=1);
y2 = data['ground_truth']; # full categorical ground truth
y = data['ground_truth_binary']; # binary ground truth
# print(X.head());
# print(Y);ß
# print(Y2);

# K-Fold #
########################################################################################################################
repeated_times = 1;
kf = RepeatedKFold(n_splits=5, n_repeats=repeated_times, random_state=np.random);
kf.get_n_splits(X);
# print(kf);

# Perform 5-fold cross validation #
svm_score = [0, 0, 0]; # single class score for svm
svm_score2 = [0, 0, 0]; # multi-class score for svm

for train_index, test_index in kf.split(X):
    split_training_sets = "TRAIN:" + str(train_index) + "\n" + "TEST:" + str(test_index);
    # print(split_training_sets);

    # Split into train and test sets #
    X_train, X_test = np.array(X)[train_index], np.array(X)[test_index];
    y_train, y_test = np.array(y)[train_index], np.array(y)[test_index];
    X2_train, X2_test = np.array(X)[train_index], np.array(X)[test_index];
    y2_train, y2_test = np.array(y2)[train_index], np.array(y2)[test_index];

    # SVM #
    ####################################################################################################################
    svm = SVC(kernel='rbf', gamma=0.05, C=1);
    svm.fit(X_train, y_train);
    y_pred = svm.predict(X_test);
    svm2 = SVC(kernel='rbf', gamma=0.1, C=1);
    svm2.fit(X2_train, y2_train);
    y2_pred = svm2.predict(X2_test);
    # print(confusion_matrix(y_test, y_pred));
    # print(classification_report(y_test, y_pred));
    # print(svm.score(X_test, y_test));  # accuracy
    # print("\tF1: %1.3f\n" % f1_score(y_test, y_pred));
    # print("\tLOSS: %1.3f\n" % brier_score_loss(y_test, y_pred));
    # print("\tPrecision: %1.3f\n" % precision_score(y_test, y_pred));
    # print("\tRecall: %1.3f\n" % recall_score(y_test, y_pred));

    # average=None # include all information of classification report;
    # 'micro' compute the f1-score using the global count of true positives / false negatives, etc.
    # 'macro' makes the average of the f1-score for each class: that's the avg / total result above
    # 'weighted' computes a weighted average of the f1-score. the more elements a class has,
    # the more important the f1-score for this class in the computation.
    score = precision_recall_fscore_support(y_test, y_pred, beta=1.0, labels=None, pos_label=1, average='weighted',
                                            warn_for=('precision', 'recall', 'f-score'), sample_weight=None);
    report = classification_report(y_test,y_pred);
    # print(score);
    score2 = precision_recall_fscore_support(y2_test, y2_pred, beta=1.0, average='weighted', pos_label=None,
                                             warn_for=('precision', 'recall', 'f-score'), sample_weight=None);
    report2 = classification_report(y2_test,y2_pred);
    # print(score2);

    # Final score calculate
    svm_score[0] = svm_score[0] + score[0];
    svm_score[1] = svm_score[1] + score[1];
    svm_score[2] = svm_score[2] + score[2];
    svm_score2[0] = svm_score2[0] + score2[0];
    svm_score2[1] = svm_score2[1] + score2[1];
    svm_score2[2] = svm_score2[2] + score2[2];

    # Store scores to database


    # End of SVM #
    ####################################################################################################################
print("\nSVM");
print("Binary Classifier:");
svm_score[0] = svm_score[0]/(5*repeated_times);
print("\tPrecision: %1.4f" % svm_score[0]);
svm_score[1] = svm_score[1]/(5*repeated_times);
print("\tRecall: %1.4f" % svm_score[1]);
svm_score[2] = svm_score[2]/(5*repeated_times);
print("\tF1-score: %1.4f" % svm_score[2]);
print("Multi-class Classifier:");
svm_score2[0] = svm_score2[0]/(5*repeated_times);
print("\tPrecision: %1.4f" % svm_score2[0]);
svm_score2[1] = svm_score2[1]/(5*repeated_times);
print("\tRecall: %1.4f" % svm_score2[1]);
svm_score2[2] = svm_score2[2]/(5*repeated_times);
print("\tF1-score: %1.4f" % svm_score2[2]);


# End of K-Fold #
########################################################################################################################