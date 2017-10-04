from __future__ import print_function, division
import pandas as pd
import numpy as np
import datetime

def add_user_id(df, df_users):
    '''
    '''
    df.copy()
    df = df.join(df_users.set_index('uuid'), on='uuid')
    return df

def join_tables(df1, df2):
    '''
    '''
    df1.copy()
    df1 = df1.join(df2.set_index('user_id'), on='user_id')
    return df1

def join_tables_index(df1, df2):
    '''
    '''
    df1.copy()
    df1 = df1.join(df2, on='user_id')
    return df1
