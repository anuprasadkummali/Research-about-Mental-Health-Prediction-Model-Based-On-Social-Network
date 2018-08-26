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
from sklearn.multiclass import OneVsOneClassifier
from sklearn.multiclass import OutputCodeClassifier
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC
from sklearn.neighbors import KNeighborsClassifier

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

##########
# K-Fold #
##########
########################################################################################################################
repeated_times = 10;
kf = RepeatedKFold(n_splits=5, n_repeats=repeated_times, random_state=np.random);
kf.get_n_splits(X);
# print(kf);

# Perform 5-fold cross validation #
svm_score = [0, 0, 0]; # single class score for svm
svm_score2 = [0, 0, 0]; # multi-class score for svm
gnb_score = [0, 0, 0]; # single class score for gnb
gnb_score2 = [0, 0, 0]; # multi-class score for gnb
knn_score = [0, 0, 0]; # single class score for knn
knn_score2 = [0, 0, 0]; # multi-class score for knn
dtree_score = [0, 0, 0]; # single class score for dtree
dtree_score2 = [0, 0, 0]; # multi-class score for dtree

for train_index, test_index in kf.split(X):
    split_training_sets = "TRAIN:" + str(train_index) + "\n" + "TEST:" + str(test_index);
    # print(split_training_sets);

    ##################################
    # Split into train and test sets #
    ##################################
    X_train, X_test = np.array(X)[train_index], np.array(X)[test_index];
    y_train, y_test = np.array(y)[train_index], np.array(y)[test_index];
    X2_train, X2_test = np.array(X)[train_index], np.array(X)[test_index];
    y2_train, y2_test = np.array(y2)[train_index], np.array(y2)[test_index];

    #######
    # SVM #
    #######
    svm = SVC(kernel='rbf', gamma=0.05, C=1);
    svm.fit(X_train, y_train);
    y_pred_svm = svm.predict(X_test);
    # svm2 = SVC(kernel='rbf', gamma=0.1, C=1);
    svm2 = OneVsRestClassifier(LinearSVC(random_state=0));
    svm2.fit(X2_train, y2_train);
    y2_pred_svm = svm2.predict(X2_test);
    # print(confusion_matrix(y_test, y_pred_svm));
    # print(classification_report(y_test, y_pred_svm));
    # print(svm.score(X_test, y_test));  # accuracy
    # print("\tF1: %1.3f\n" % f1_score(y_test, y_pred_svm));
    # print("\tLOSS: %1.3f\n" % brier_score_loss(y_test, y_pred_svm));
    # print("\tPrecision: %1.3f\n" % precision_score(y_test, y_pred_svm));
    # print("\tRecall: %1.3f\n" % recall_score(y_test, y_pred_svm));

    # average=None # include all information of classification report;
    # 'micro' compute the f1-score using the global count of true positives / false negatives, etc.
    # 'macro' makes the average of the f1-score for each class: that's the avg / total result above
    # 'weighted' computes a weighted average of the f1-score. the more elements a class has,
    # the more important the f1-score for this class in the computation.
    score_svm = precision_recall_fscore_support(y_test, y_pred_svm, beta=1.0, labels=None, pos_label=1, average='macro',
                                            warn_for=('precision', 'recall', 'f-score'), sample_weight=None);
    report_svm = classification_report(y_test,y_pred_svm);
    # print(score);
    score2_svm = precision_recall_fscore_support(y2_test, y2_pred_svm, beta=1.0, average='macro', pos_label=None,
                                             warn_for=('precision', 'recall', 'f-score'), sample_weight=None);
    report2_svm = classification_report(y2_test,y2_pred_svm);
    # print(score2);

    # Final score of svm calculate
    svm_score[0] = svm_score[0] + score_svm[0];
    svm_score[1] = svm_score[1] + score_svm[1];
    svm_score[2] = svm_score[2] + score_svm[2];
    svm_score2[0] = svm_score2[0] + score2_svm[0];
    svm_score2[1] = svm_score2[1] + score2_svm[1];
    svm_score2[2] = svm_score2[2] + score2_svm[2];

    # Store scores to database

    ####################################################################################################################
    ###############
    # Naive Bayes #
    ###############
    gnb = GaussianNB().fit(X_train, y_train);
    # Testfrom sklearn.metrics import classification_report, confusion_matrix
    y_pred_gnb = gnb.predict(X_test);

    # Report #
    # print(confusion_matrix(y_test, y_pred_gnb))
    # print(classification_report(y_test, y_pred_gnb))
    # print(gnb.score(X_test, y_test));  # accuracy

    # Naive Bayes multi-class
    gnb2 = GaussianNB().fit(X2_train, y2_train);
    # Testfrom sklearn.metrics import classification_report, confusion_matrix
    y2_pred_gnb = gnb2.predict(X2_test);

    # Score
    score_gnb = precision_recall_fscore_support(y_test, y_pred_gnb, beta=1.0, labels=None, pos_label=1,
                                                average='macro',
                                                warn_for=('precision', 'recall', 'f-score'), sample_weight=None);
    report_gnb = classification_report(y_test, y_pred_gnb);
    # print(score);
    score2_gnb = precision_recall_fscore_support(y2_test, y2_pred_gnb, beta=1.0, average='macro', pos_label=None,
                                                 warn_for=('precision', 'recall', 'f-score'), sample_weight=None);
    report2_gnb = classification_report(y2_test, y2_pred_gnb);

    # Final score of gnb calculate
    gnb_score[0] = gnb_score[0] + score_gnb[0];
    gnb_score[1] = gnb_score[1] + score_gnb[1];
    gnb_score[2] = gnb_score[2] + score_gnb[2];
    gnb_score2[0] = gnb_score2[0] + score2_gnb[0];
    gnb_score2[1] = gnb_score2[1] + score2_gnb[1];
    gnb_score2[2] = gnb_score2[2] + score2_gnb[2];
    ####################################################################################################################
    ###########################
    # KNN k-nearest neighbours#
    ###########################
    knn = KNeighborsClassifier(n_neighbors=7).fit(X_train, y_train);

    # Testfrom sklearn.metrics import classification_report, confusion_matrix
    y_pred_knn = knn.predict(X_test);

    # KNN k-nearest neighbours multi-class
    knn2 = KNeighborsClassifier(n_neighbors=7).fit(X2_train, y2_train);

    # Testfrom sklearn.metrics import classification_report, confusion_matrix
    y2_pred_knn = knn2.predict(X2_test);

    # Score
    score_knn = precision_recall_fscore_support(y_test, y_pred_knn, beta=1.0, labels=None, pos_label=1,
                                                average='macro',
                                                warn_for=('precision', 'recall', 'f-score'), sample_weight=None);
    report_knn = classification_report(y_test, y_pred_knn);
    # print(score);
    score2_knn = precision_recall_fscore_support(y2_test, y2_pred_knn, beta=1.0, average='macro', pos_label=None,
                                                 warn_for=('precision', 'recall', 'f-score'), sample_weight=None);
    report2_knn = classification_report(y2_test, y2_pred_knn);

    # Final score of knn calculate
    knn_score[0] = knn_score[0] + score_knn[0];
    knn_score[1] = knn_score[1] + score_knn[1];
    knn_score[2] = knn_score[2] + score_knn[2];
    knn_score2[0] = knn_score2[0] + score2_knn[0];
    knn_score2[1] = knn_score2[1] + score2_knn[1];
    knn_score2[2] = knn_score2[2] + score2_knn[2];
    ####################################################################################################################
    #################
    # Decision Tree #
    #################
    dtree = DecisionTreeClassifier(max_depth=3).fit(X_train, y_train);

    # Testfrom sklearn.metrics import classification_report, confusion_matrix
    y_pred_dtree = dtree.predict(X_test);

    # Decision Tree multi-class
    dtree2 = DecisionTreeClassifier(max_depth=3).fit(X2_train, y2_train);

    # Testfrom sklearn.metrics import classification_report, confusion_matrix
    y2_pred_dtree = dtree2.predict(X2_test);

    # Score
    score_dtree = precision_recall_fscore_support(y_test, y_pred_dtree, beta=1.0, labels=None, pos_label=1,
                                                average='macro',
                                                warn_for=('precision', 'recall', 'f-score'), sample_weight=None);
    report_dtree = classification_report(y_test, y_pred_dtree);
    # print(score);
    score2_dtree = precision_recall_fscore_support(y2_test, y2_pred_dtree, beta=1.0, average='macro', pos_label=None,
                                                 warn_for=('precision', 'recall', 'f-score'), sample_weight=None);
    report2_dtree = classification_report(y2_test, y2_pred_dtree);

    # Final score of dtree calculate
    dtree_score[0] = dtree_score[0] + score_dtree[0];
    dtree_score[1] = dtree_score[1] + score_dtree[1];
    dtree_score[2] = dtree_score[2] + score_dtree[2];
    dtree_score2[0] = dtree_score2[0] + score2_dtree[0];
    dtree_score2[1] = dtree_score2[1] + score2_dtree[1];
    dtree_score2[2] = dtree_score2[2] + score2_dtree[2];
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

print("\nNaive Bayes");
print("Binary Classifier:");
gnb_score[0] = gnb_score[0]/(5*repeated_times);
print("\tPrecision: %1.4f" % gnb_score[0]);
gnb_score[1] = gnb_score[1]/(5*repeated_times);
print("\tRecall: %1.4f" % gnb_score[1]);
gnb_score[2] = gnb_score[2]/(5*repeated_times);
print("\tF1-score: %1.4f" % gnb_score[2]);
print("Multi-class Classifier:");
gnb_score2[0] = gnb_score2[0]/(5*repeated_times);
print("\tPrecision: %1.4f" % gnb_score2[0]);
gnb_score2[1] = gnb_score2[1]/(5*repeated_times);
print("\tRecall: %1.4f" % gnb_score2[1]);
gnb_score2[2] = gnb_score2[2]/(5*repeated_times);
print("\tF1-score: %1.4f" % gnb_score2[2]);

print("\nK-Nearest Neighbours");
print("Binary Classifier:");
knn_score[0] = knn_score[0]/(5*repeated_times);
print("\tPrecision: %1.4f" % knn_score[0]);
knn_score[1] = knn_score[1]/(5*repeated_times);
print("\tRecall: %1.4f" % knn_score[1]);
knn_score[2] = knn_score[2]/(5*repeated_times);
print("\tF1-score: %1.4f" % knn_score[2]);
print("Multi-class Classifier:");
knn_score2[0] = knn_score2[0]/(5*repeated_times);
print("\tPrecision: %1.4f" % knn_score2[0]);
knn_score2[1] = knn_score2[1]/(5*repeated_times);
print("\tRecall: %1.4f" % knn_score2[1]);
knn_score2[2] = knn_score2[2]/(5*repeated_times);
print("\tF1-score: %1.4f" % knn_score2[2]);


print("\nDesicion Tree");
print("Binary Classifier:");
dtree_score[0] = dtree_score[0]/(5*repeated_times);
print("\tPrecision: %1.4f" % dtree_score[0]);
dtree_score[1] = dtree_score[1]/(5*repeated_times);
print("\tRecall: %1.4f" % dtree_score[1]);
dtree_score[2] = dtree_score[2]/(5*repeated_times);
print("\tF1-score: %1.4f" % dtree_score[2]);
print("Multi-class Classifier:");
dtree_score2[0] = dtree_score2[0]/(5*repeated_times);
print("\tPrecision: %1.4f" % dtree_score2[0]);
dtree_score2[1] = dtree_score2[1]/(5*repeated_times);
print("\tRecall: %1.4f" % dtree_score2[1]);
dtree_score2[2] = dtree_score2[2]/(5*repeated_times);
print("\tF1-score: %1.4f" % dtree_score2[2]);

########################################################################################################################
# End of K-Fold #
########################################################################################################################