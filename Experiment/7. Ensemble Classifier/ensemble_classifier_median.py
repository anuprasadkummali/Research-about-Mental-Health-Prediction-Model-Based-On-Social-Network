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
from sklearn.metrics import accuracy_score
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
svm_score = [0, 0, 0, 0]; # single class score for svm
gnb_score = [0, 0, 0, 0]; # single class score for gnb
knn_score = [0, 0, 0, 0]; # single class score for knn
dtree_score = [0, 0, 0, 0]; # single class score for dtree
en_score = [0, 0, 0, 0]; # single class score for ensemble

en_median = np.zeros((4,5*repeated_times));
k = 0;

for train_index, test_index in kf.split(X):
    split_training_sets = "TRAIN:" + str(train_index) + "\n" + "TEST:" + str(test_index);
    # print(split_training_sets);
    ##################################
    # Split into train and test sets #
    ##################################
    X_train, X_test = np.array(X)[train_index], np.array(X)[test_index];
    y_train, y_test = np.array(y)[train_index], np.array(y)[test_index];

    #######
    # SVM #
    #######
    svm = SVC(kernel='rbf', gamma=0.1, C=1);
    svm.fit(X_train, y_train);
    y_pred_svm = svm.predict(X_test);

    score_svm = precision_recall_fscore_support(y_test, y_pred_svm, beta=1.0, labels=None, pos_label=1, average='binary',
                                            warn_for=('precision', 'recall', 'f-score'), sample_weight=None);
    # report_svm = classification_report(y_test,y_pred_svm);
    accuracy_svm = accuracy_score(y_test, y_pred_svm, normalize=True, sample_weight=None);

    # Final score of svm calculate
    svm_score[0] = svm_score[0] + score_svm[0];
    svm_score[1] = svm_score[1] + score_svm[1];
    svm_score[2] = svm_score[2] + score_svm[2];
    svm_score[3] = svm_score[3] + accuracy_svm;

    # Store scores to database

    ####################################################################################################################
    ###############
    # Naive Bayes #
    ###############
    gnb = GaussianNB().fit(X_train, y_train);
    # Testfrom sklearn.metrics import classification_report, confusion_matrix
    y_pred_gnb = gnb.predict(X_test);

    # Score
    score_gnb = precision_recall_fscore_support(y_test, y_pred_gnb, beta=1.0, labels=None, pos_label=1,
                                                average='binary',
                                                warn_for=('precision', 'recall', 'f-score'), sample_weight=None);
    # report_gnb = classification_report(y_test, y_pred_gnb);
    accuracy_gnb = accuracy_score(y_test, y_pred_gnb, normalize=True, sample_weight=None);

     # Final score of gnb calculate
    gnb_score[0] = gnb_score[0] + score_gnb[0];
    gnb_score[1] = gnb_score[1] + score_gnb[1];
    gnb_score[2] = gnb_score[2] + score_gnb[2];
    gnb_score[3] = gnb_score[3] + accuracy_gnb;
    ####################################################################################################################
    ###########################
    # KNN k-nearest neighbours#
    ###########################
    knn = KNeighborsClassifier(n_neighbors=5).fit(X_train, y_train);

    # Testfrom sklearn.metrics import classification_report, confusion_matrix
    y_pred_knn = knn.predict(X_test);

    # Score
    score_knn = precision_recall_fscore_support(y_test, y_pred_knn, beta=1.0, labels=None, pos_label=1,
                                                average='binary',
                                                warn_for=('precision', 'recall', 'f-score'), sample_weight=None);
    # report_knn = classification_report(y_test, y_pred_knn);
    accuracy_knn = accuracy_score(y_test, y_pred_knn, normalize=True, sample_weight=None);

    # Final score of knn calculate
    knn_score[0] = knn_score[0] + score_knn[0];
    knn_score[1] = knn_score[1] + score_knn[1];
    knn_score[2] = knn_score[2] + score_knn[2];
    knn_score[3] = knn_score[3] + accuracy_knn;
    ####################################################################################################################
    #################
    # Decision Tree #
    #################
    dtree = DecisionTreeClassifier(max_depth=3).fit(X_train, y_train);

    # Testfrom sklearn.metrics import classification_report, confusion_matrix
    y_pred_dtree = dtree.predict(X_test);

    # Score
    score_dtree = precision_recall_fscore_support(y_test, y_pred_dtree, beta=1.0, labels=None, pos_label=1,
                                                average='binary',
                                                warn_for=('precision', 'recall', 'f-score'), sample_weight=None);
    # report_dtree = classification_report(y_test, y_pred_dtree);
    accuracy_dtree = accuracy_score(y_test, y_pred_dtree, normalize=True, sample_weight=None);

    # Final score of dtree calculate
    dtree_score[0] = dtree_score[0] + score_dtree[0];
    dtree_score[1] = dtree_score[1] + score_dtree[1];
    dtree_score[2] = dtree_score[2] + score_dtree[2];
    dtree_score[3] = dtree_score[3] + accuracy_dtree;
    ####################################################################################################################
    ############
    # Ensemble #
    ############

    # Testing
    y_pred_en = 0.176*y_pred_svm + 0.448*y_pred_gnb +0.205*y_pred_knn + 0.171*y_pred_dtree; # shape (1080,)
    for i in range(0, y_pred_en.shape[0]):
        #print(y_pred_en[i]);
        if y_pred_en[i]>0.5:
            y_pred_en[i] = 1;
        else:
            y_pred_en[i] = 0;
    # print(y_pred_en);


    # y_pred_en =  y_pred_dtree;  # shape (1080,) +y_pred_knn[i]  y_pred_gnb[i]+   y_pred_dtree[i]+  y_pred_svm[i]+
    # for i in range(0, y_pred_en.shape[0]):
    #     if (y_pred_gnb[i] + y_pred_dtree[i] + y_pred_svm[i] + y_pred_knn[i]) >=3:
    #         y_pred_en[i] = 1;
    #     else:
    #         y_pred_en[i] = 0;
    # print(y_pred_en);


     # Score
    score_en = precision_recall_fscore_support(y_test, y_pred_en, beta=1.0, labels=None, pos_label=1,
                                                  average='binary',
                                                  warn_for=('precision', 'recall', 'f-score'), sample_weight=None);
    # report_en = classification_report(y_test, y_pred_en);
    accuracy_en = accuracy_score(y_test, y_pred_en, normalize=True, sample_weight=None);

    # Final score calculation
    en_score[0] = en_score[0] + score_en[0];
    en_score[1] = en_score[1] + score_en[1];
    en_score[2] = en_score[2] + score_en[2];
    en_score[3] = en_score[3] + accuracy_en;

    en_median[0][k] = score_en[0];
    en_median[1][k] = score_en[1];
    en_median[2][k] = score_en[2];
    en_median[3][k] = accuracy_en;
    print(k);
    # print(en_median);
    k = k + 1;
    ####################################################################################################################

print("\nEnsemble");
print("Binary Classifier:");
en_score[0] = en_score[0]/(5*repeated_times);
print("\tPrecision: %1.4f" % en_score[0]);
en_score[1] = en_score[1]/(5*repeated_times);
print("\tRecall: %1.4f" % en_score[1]);
en_score[2] = en_score[2]/(5*repeated_times);
print("\tF1-score: %1.4f" % en_score[2]);
en_score[3] = en_score[3]/(5*repeated_times);
print("\tAccuracy: %1.4f" % en_score[3]);


print("Median:");
en0 = en_median[0];
en1 = en_median[1];
en2 = en_median[2];
en3 = en_median[3];
print("\tPrecision: %1.4f" % np.median(en0,axis=0));
print("\tRecall: %1.4f" % np.median(en1,axis=0));
print("\tF1-score: %1.4f" % np.median(en2,axis=0));
print("\tAccuracy: %1.4f" % np.median(en3,axis=0));



print("\nSVM");
print("Binary Classifier:");
svm_score[0] = svm_score[0]/(5*repeated_times);
print("\tPrecision: %1.4f" % svm_score[0]);
svm_score[1] = svm_score[1]/(5*repeated_times);
print("\tRecall: %1.4f" % svm_score[1]);
svm_score[2] = svm_score[2]/(5*repeated_times);
print("\tF1-score: %1.4f" % svm_score[2]);
svm_score[3] = svm_score[3]/(5*repeated_times);
print("\tAccuracy: %1.4f" % svm_score[3]);


print("\nNaive Bayes");
print("Binary Classifier:");
gnb_score[0] = gnb_score[0]/(5*repeated_times);
print("\tPrecision: %1.4f" % gnb_score[0]);
gnb_score[1] = gnb_score[1]/(5*repeated_times);
print("\tRecall: %1.4f" % gnb_score[1]);
gnb_score[2] = gnb_score[2]/(5*repeated_times);
print("\tF1-score: %1.4f" % gnb_score[2]);
gnb_score[3] = gnb_score[3]/(5*repeated_times);
print("\tAccuracy: %1.4f" % gnb_score[3]);


print("\nK-Nearest Neighbours");
print("Binary Classifier:");
knn_score[0] = knn_score[0]/(5*repeated_times);
print("\tPrecision: %1.4f" % knn_score[0]);
knn_score[1] = knn_score[1]/(5*repeated_times);
print("\tRecall: %1.4f" % knn_score[1]);
knn_score[2] = knn_score[2]/(5*repeated_times);
print("\tF1-score: %1.4f" % knn_score[2]);
knn_score[3] = knn_score[3]/(5*repeated_times);
print("\tAccuracy: %1.4f" % knn_score[3]);


print("\nDesicion Tree");
print("Binary Classifier:");
dtree_score[0] = dtree_score[0]/(5*repeated_times);
print("\tPrecision: %1.4f" % dtree_score[0]);
dtree_score[1] = dtree_score[1]/(5*repeated_times);
print("\tRecall: %1.4f" % dtree_score[1]);
dtree_score[2] = dtree_score[2]/(5*repeated_times);
print("\tF1-score: %1.4f" % dtree_score[2]);
dtree_score[3] = dtree_score[3]/(5*repeated_times);
print("\tAccuracy: %1.4f" % dtree_score[3]);

########################################################################################################################
# End of K-Fold #
########################################################################################################################