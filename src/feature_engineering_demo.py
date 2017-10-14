'''
This module is used for feature engineering specifically in the Demographics
dataframe.  The functions in this module will do the following: create a feature
for age of user, consolidate the college types into fewer categories, create
dummy variables for logistic regression (where one dummy must be left out)
and for decision trees (where all dummy variables are kept).
'''

from __future__ import print_function, division
import datetime
import pandas as pd
import numpy as np
import src.join_tables as jt

def create_age(df_demo):
    '''
    Create a feature for age of user.

    Parameters
    ----------
    df_demo: Dataframe
        Dataframe with demographic data.

    Returns
    -------
    df_demo: Dataframe
        Dataframe with a feature for age of user added to it.

    '''
    df_demo['age'] = pd.to_datetime(df_demo.first_use).dt.year - df_demo.birthdate.dt.year
    return df_demo

def consolidate_college_type(df_demo):
    '''
    Consolidate the college types by renaming the category 'University' to
    'College'.

    Parameters
    ----------
    df_demo: Dataframe
        Dataframe with demographic data.

    Returns
    -------
    df_demo: Dataframe
        Dataframe with altered 'college_type' feature.

    '''
    df_demo['college_type'] = df_demo.college_type.map(lambda x: 'College' \
                                                         if x == 'University' else x)
    return df_demo

def dummies_logistic(df_demo):
    '''
    Create dummy variables for logistic regression wherein one dummy is dropped.

    Parameters
    ----------
    df_demo: Dataframe
        Dataframe with demographic data.

    Returns
    -------
    df_demo: Dataframe
        Dataframe with dummy variables.
    '''
    df_demo = df_demo.copy()
    df_demo = pd.get_dummies(df_demo, columns=['college_type', 'diabetes_type',\
                                                'ethnicity', 'gender'], drop_first=True)
    return df_demo

def dummies_other(df_demo):
    '''
    Create dummy variables for logistic regression wherein one dummy is dropped.

    Parameters
    ----------
    df_demo: Dataframe
        Dataframe with demographic data.

    Returns
    -------
    df_demo: Dataframe
        Dataframe with dummy variables.
    '''

    df_demo = df_demo.copy()
    df_demo = pd.get_dummies(df_demo, columns=['college_type', 'diabetes_type',\
                                                'ethnicity', 'gender'])
    return df_demo
