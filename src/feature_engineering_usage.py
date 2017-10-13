'''
This module is used to create new features in the app usage dataframe. 
'''

from __future__ import print_function, division
import datetime
import pandas as pd
import numpy as np

def remove_actions(df_usage):
    '''
    Remove any rows from the app usage dataframe with actions called 'chat_pause' and
    'chat_online'.
    '''
    df_usage = df_usage.copy()
    df_usage = df_usage[df_usage['action'].isin(['page_view', 'a1c_update', 'chat_resume'])]
    return df_usage

def consolidate_actions_helper(row):
    '''
    Rename the action 'chat_resume' to 'page_view' for ease of analysis. 
    '''
    if row.action == 'chat_resume':
        return 'page_view'
    else:
        return row.action

def consolidate_actions(df_usage):
    '''
    Run the helper function 'consolidate_actions_helper' on the app usage dataframe.
    '''
    df_usage = df_usage.copy()
    df_usage['action'] = df_usage.apply(consolidate_actions_helper, axis=1)
    return df_usage

def create_dummies(df_usage):
    '''
    Create dummy variables for the actions.
    '''

    df_usage = df_usage.copy()
    df_usage['action'] = df_usage['action'].astype('category')
    df_usage = pd.get_dummies(df_usage, columns=['action'])
    return df_usage


def a1c_w1(df_usage):
    '''
    Create a dummy variable in the app usage dataframe to 
    '''
    df_usage['a1c_w1'] = (df_usage.time.dt.date < df_usage['one_week']) \
                                    & (df_usage.action_a1c_update > 0)
    return df_usage

def a1c_w1w2(df_usage):
    df_usage['a1c_w1w2'] = (df_usage.time.dt.date < df_usage['two_weeks']) \
                                    & (df_usage.action_a1c_update > 0)
    return df_usage

def a1c_total(df_usage):
    df_usage['a1c_total'] = df_usage.action_a1c_update > 0
    return df_usage


def page_view_w1(df_usage):
    df_usage['page_view_w1'] = (df_usage.time.dt.date < df_usage['one_week']) \
                                    & (df_usage.action_page_view > 0)
    return df_usage

def page_view_w1w2(df_usage):
    df_usage['page_view_w1w2'] = (df_usage.time.dt.date < df_usage['two_weeks']) \
                                    & (df_usage.action_page_view > 0)
    return df_usage

def page_view_total(df_usage):
    df_usage['page_view_total'] = df_usage.action_page_view > 0
    return df_usage

def add_usage_time_features(df_usage):
    df_usage = df_usage.copy()
    pipeline = [a1c_w1, a1c_w1w2, a1c_total, \
                page_view_w1, page_view_w1w2, page_view_total]

    for step in pipeline:
        step(df_usage)

    return df_usage

def user_usage_counts(df_usage):
    '''
    add docs
    '''
    groupby_entries = df_usage.groupby('user_id')
    usage_counts = groupby_entries.aggregate(np.count_nonzero) \
                        [['id', 'a1c_w1', 'a1c_w1w2', 'a1c_total', \
                        'page_view_w1', 'page_view_w1w2', 'page_view_total']]
    usage_counts.rename(columns={'id' : 'total_usage_counts'}, inplace=True)
    return usage_counts
