from __future__ import print_function, division
import pandas as pd
import numpy as np
import datetime
import join_tables as jt

def entries_one_week (df_entries):
    '''
    ADD DOCUMENTATION
    '''
    df_entries['in_one_week'] = df_entries.entry_time.dt.date < df_entries['one_week']
    return df_entries

def entries_two_weeks (df_entries):
    '''
    ADD DOCUMENTATION
    '''
    df_entries['in_two_weeks'] = df_entries.entry_time.dt.date < df_entries['two_weeks']
    return df_entries

def entries_post_one_week(df_entries):
    df_entries['post_one_week'] = df_entries.entry_time.dt.date >= df_entries['one_week']
    return df_entries

def entries_post_two_weeks(df_entries):
    df_entries['post_two_weeks'] = df_entries.entry_time.dt.date >= df_entries['two_weeks']
    return df_entries

def moods_one_week(df_entries):
    df_entries['moods_one_week'] = (df_entries.entry_time.dt.date < df_entries['one_week']) \
                                    & (df_entries.mood.notnull())
    return df_entries

def moods_two_weeks(df_entries):
    pass

def moods_total(df_entries):
    pass

def notes_one_week(df_entries):
    pass

def notes_two_weeks(df_entries):
    pass



def add_entrytime_features(df_entries):
    pipeline = [entries_one_week, entries_two_weeks, \
                entries_post_one_week, entries_post_two_weeks, \
                moods_one_week]

    for step in pipeline:
        step(df_entries)

    return df_entries

def user_entry_counts(df_entries):
    '''
    add docs
    '''
    groupby_entries = df_entries.groupby('user_id')
    user_entry_counts = groupby_entries.aggregate(np.count_nonzero) \
                        [['id', 'in_one_week', 'in_two_weeks','post_one_week', \
                          'post_two_weeks', 'moods_one_week']]
    user_entry_counts.rename(columns={'id' : 'total_entries', \
                                      'in_one_week' : 'entries_w1', \
                                      'in_two_weeks' : 'entries_w1w2', \
                                      'post_one_week' : 'entries_post_w1', \
                                      'post_two_weeks' : 'entries_post_w2', \
                                      'moods_one_week' : 'moods_w1'},
                             inplace=True)
    return user_entry_counts
