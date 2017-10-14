'''
This module adds the 'user_id' to a dataframe by joining that dataframe to the
user dataframe using the 'uuid' field. This will also join dataframes on the 'user_id'.
'''

from __future__ import print_function, division
import datetime
import pandas as pd
import numpy as np

def add_user_id(df, df_users):
    '''
    Add the user_id to a dataframe by joining that dataframe with the user dataframe
    on the 'uuid' field.
    '''
    df.copy()
    df = df.join(df_users.set_index('uuid'), on='uuid')
    return df

def join_tables(df1, df2):
    '''
    Join dataframes on the 'user_id' field where the 'user_id' is not set as the index
    on the second dataframe.
    '''
    df1.copy()
    df1 = df1.join(df2.set_index('user_id'), on='user_id')
    return df1

def join_tables_index(df1, df2):
    '''
    Join dataframes on the 'user_id' field where the 'user_id' is set as the index
    on the second dataframe.
    '''
    df1.copy()
    df1 = df1.join(df2, on='user_id')
    return df1
