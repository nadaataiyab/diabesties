from __future__ import print_function, division
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
from sqlalchemy import create_engine
import MySQLdb
import src.data_processing as dp
import src.join_tables as jt
import src.add_dates as ad
import src.feature_engineering_entries as fee
import src.feature_engineering_usage as feu
import src.feature_engineering_demo as fed
import src.data_cleaning as dc

from statsmodels.discrete.discrete_model import Logit
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import roc_curve, auc, confusion_matrix, precision_score, recall_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier
from sklearn.linear_model import RidgeClassifier
from sklearn.preprocessing import StandardScaler, MinMaxScaler

def run_logistic(X_train, X_test, y_train, y_test):
    lr = LogisticRegression()
    lr.fit(X_train, y_train)
    y_score = lr.predict_proba(X_test)[:, 1]
    y_true = y_test
    fpr, tpr, thresholds = roc_curve(y_true, y_score)
    y_pred = lr.predict(X_test)
    accuracy = lr.score(X_test, y_test)
    precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)
    auc_score = auc(fpr, tpr)
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

    print_out_scores = "Logistic Regression Scores \n\
                    Accuracy:   {:0.2f} \n\
                    Precision:  {:0.2f} \n\
                    Recall:     {:0.2f} \n\
                    AUC:        {:0.2f}".format(accuracy, precision, recall, auc_score)
    print_out_confusion_matrix = "  Confusion Matrix: \n\
                    True Negatives:   {} \n\
                    False Negatives:  {} \n\
                    True Positives:   {} \n\
                    False Positives:   {}".format(tn, fn, tp, fp)

    print(print_out_scores)
    print(print_out_confusion_matrix)

    plt.figure(figsize=(15,10))
    plt.ylabel('True Positive Rate (Sensitivity)', fontsize=20)
    plt.xlabel('False Positive Rate (1-Specificity)', fontsize=20)
    plt.plot(fpr, tpr, label="Logistic Regression: {:0.2f}".format(auc_score), linewidth=5)
    plt.legend(fontsize=24, loc=4)
    plt.title("ROC Curves of Churn Models", fontsize=30)




def run_classifiers(X_train, X_test, y_train, y_test, classifiers):
    '''
    ADD DOCUMENTATION
    '''
    for c in classifiers:
        model = c
        model.fit(X_train, y_train)
        y_score = model.predict_proba(X_test)[:, 1]
        y_true = y_test
        fpr, tpr, thresholds = roc_curve(y_true, y_score)
        y_pred = model.predict(X_test)
        accuracy = model.score(X_test, y_test)
        precision = precision_score(y_true, y_pred)
        recall = recall_score(y_true, y_pred)
        auc_score = auc(fpr, tpr)
        tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

        model_name = (str(model).split('(')[0]) + ": {:0.2f}".format(auc_score)

        print_out_scores = "{} \n\
                        Accuracy:   {:0.2f} \n\
                        Precision:  {:0.2f} \n\
                        Recall:     {:0.2f} \n\
                        AUC:        {:0.2f}".format(model_name, accuracy,
                                                    precision, recall, auc_score)
        print_out_confusion_matrix = "  Confusion Matrix: \n\
                        True Negatives:   {} \n\
                        False Negatives:  {} \n\
                        True Positives:   {} \n\
                        False Positives:   {}".format(tn, fn, tp, fp)

        print(print_out_scores)
        print(print_out_confusion_matrix)

        plt.plot(fpr, tpr, label=model_name, linewidth=5)
        plt.legend(fontsize=24, loc=4)
        plt.plot([0,1], [0,1],'--', color='black')
        sns.plt.annotate("Area Under the Curve (AUC)", (0.6, 0.3), fontsize='xx-large', color='grey')

#create a list of dictionaries of the model results
