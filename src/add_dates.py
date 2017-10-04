from __future__ import print_function, division
import pandas as pd
import numpy as np
import datetime
import join_tables as jt

def first_use(df_usage):
    '''
    ADD DOCUMENTATION
    '''
    first_use = df_usage.groupby('user_id').time.first()
    first_use = first_use.dt.date
    first_use.rename('first_use', inplace=True)
    return first_use

def last_use(df_usage):
    '''
    ADD DOCUMENTATION
    '''
    last_use = df_usage.groupby('user_id').time.last()
    last_use = last_use.dt.date
    last_use.rename('last_use', inplace=True)
    return last_use

def add_weeks(df_dates):
    '''
    ADD DOCUMENTATION
    '''
    df_dates = df_dates.copy()
    df_dates['one_week'] = df_dates.first_use + datetime.timedelta(days=7)
    df_dates['two_weeks'] = df_dates.first_use + datetime.timedelta(days = 14)
    return df_dates

def create_dates(df_usage):
    '''
    ADD DOCUMENTATION
    '''
    first_date = first_use(df_usage=df_usage)
    last_date = last_use(df_usage=df_usage)
    df_dates = pd.concat([first_date, last_date], axis=1)
    df_dates = add_weeks(df_dates)
    return df_dates

def add_dates(df, df_dates):
    '''
    '''
    df = df.join(df_dates, on='user_id')
    return df
