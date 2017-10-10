'''
Module to add features for each user specifying the date of their first log entry, one week after the first entry, 
two weeks after the first entry, and their final log entry.
'''

from __future__ import print_function, division
import pandas as pd
import numpy as np
import datetime
import join_tables as jt


def first_use(df_usage):
    '''
    Create a series with the date that each user in the usage table
    first used the app.

    Parameters
    ----------
    df_usage: dataframe
        Dataframe with data from app usage table.

    Returns
    -------
    first_usage: Pandas series
        Pandas series which lists the date that each user first used the app.
    '''
    first_use = df_usage.groupby('user_id').time.first()
    first_use = first_use.dt.date
    first_use.rename('first_use', inplace=True)
    return first_use

def last_use(df_usage):
    '''
    Create a series with the date that each user in the usage table
    last used the app.

    Parameters
    ----------
    df_usage: dataframe
        Dataframe with data from app usage table.

    Returns
    -------
    last_usage: Pandas series
        Pandas series which lists the date that each user last used the app.
    '''
    last_use = df_usage.groupby('user_id').time.last()
    last_use = last_use.dt.date
    last_use.rename('last_use', inplace=True)
    return last_use

def add_weeks(df_dates):
    '''
    Create a new column with the date one week after the first use and a column
    with the date two weeks after the first use.

    Parameters
    ----------
    df_dates: dataframe
    
    Returns
    -------
    df_dates: dataframe
        Dataframe with new columns created with dates for one week and two weeks after
        first use.
    '''
    df_dates = df_dates.copy()
    df_dates['one_week'] = df_dates.first_use + datetime.timedelta(days=7)
    df_dates['two_weeks'] = df_dates.first_use + datetime.timedelta(days = 14)
    return df_dates

def create_dates(df_usage):
    '''
    Create a dataframe that lists date of first use, last use, one week anniversary
    and two week anniversary for each user.   

    Parameters
    ----------
    df_usage: dataframe
    
    Returns
    -------
    df_dates: dataframe
    
    '''
    first_date = first_use(df_usage=df_usage)
    last_date = last_use(df_usage=df_usage)
    df_dates = pd.concat([first_date, last_date], axis=1)
    df_dates = add_weeks(df_dates)
    return df_dates

def add_dates(df, df_dates):
    '''
    Join dataframe with dates to demographics dataframe.   

    Parameters
    ----------
    df: dataframe
        Demographics dataframe.
    
    df_dates: dataframe
        Dates dataframe.
    
    Returns
    -------
    df: dataframe
        Demographics dataframe with dates dataframe joined to it. 

    '''
    df = df.join(df_dates, on='user_id')
    return df
