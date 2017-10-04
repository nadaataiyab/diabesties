from __future__ import print_function, division
import pandas as pd
import numpy as np
import datetime
import join_tables as jt

def create_age(df_demo):
    df_demo['age'] = pd.to_datetime(df_demo.first_use).dt.year - df_demo.birthdate.dt.year
    return df_demo

def consolidate_college_type(df_demo):
    df_demo['college_type'] = df_demo.college_type.map(lambda x: 'College' \
                                                         if x == 'University' else x)
    return df_demo

def dummies_logistic(df_demo):
    df_demo = df_demo.copy()
    df_demo = pd.get_dummies(df_demo, columns=['college_type', 'diabetes_type',\
                                                'ethnicity', 'gender'],
                                                drop_first=True)
    return df_demo

def dummies_other(df_demo):
    df_demo = df_demo.copy()
    df_demo = pd.get_dummies(df_demo, columns=['college_type', 'diabetes_type',\
                                                'ethnicity', 'gender'])
    return df_demo
