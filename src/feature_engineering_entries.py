'''
This module is used to create new features in the entries dataframe.
'''

from __future__ import print_function, division
import datetime
import pandas as pd
import numpy as np

def entries_one_week(df_entries):
    '''
    Create new column in dataframe with a boolean returning as True if entry
    was created within the first week from the date of first use for that user.
    '''
    df_entries['entries_w1'] = df_entries.entry_time.dt.date < df_entries['one_week']
    return df_entries

def entries_two_weeks(df_entries):
    '''
    Create new column in dataframe with a boolean returning as True if entry
    was created within two weeks from the date of first use for that user.
    '''
    df_entries['entries_w1w2'] = df_entries.entry_time.dt.date < df_entries['two_weeks']
    return df_entries

def entries_post_one_week(df_entries):
    '''
    Create new column in dataframe with a boolean returning as True if entry
    was created after one week from the date of first use for that user.
    '''
    df_entries['entries_post_w1'] = df_entries.entry_time.dt.date >= df_entries['one_week']
    return df_entries

def entries_post_two_weeks(df_entries):
    '''
    Create new column in dataframe with a boolean returning as True if entry
    was created after one two weeks from the date of first use for that user.
    '''

    df_entries['entries_post_w2'] = df_entries.entry_time.dt.date >= df_entries['two_weeks']
    return df_entries

def moods_w1(df_entries):
    '''
    Create new column in dataframe with a boolean returning as True if mood entry
    was created withn one week from the date of first use for that user.
    '''
    df_entries['moods_w1'] = (df_entries.entry_time.dt.date < df_entries['one_week']) \
                                    & (df_entries.mood.notnull())
    return df_entries

def moods_w1w2(df_entries):
    '''
    Create new column in dataframe with a boolean returning as True if mood entry
    was created within two weeks from the date of first use for that user.
    '''
    df_entries['moods_w1w2'] = (df_entries.entry_time.dt.date < df_entries['two_weeks']) \
                                    & (df_entries.mood.notnull())
    return df_entries

def moods_total(df_entries):
    '''
    Create new column in dataframe with a boolean returning as True if mood was included
    in entry.
    '''
    df_entries['moods_total'] = df_entries.mood.notnull()

    return df_entries

def notes_w1(df_entries):
    '''
    Create new column in dataframe with a boolean returning as True if note entry
    was created withn one week from the date of first use for that user.
    '''
    df_entries['notes_w1'] = (df_entries.entry_time.dt.date < df_entries['one_week']) \
                                    & (df_entries.note.notnull())
    return df_entries

def notes_w1w2(df_entries):
    '''
    Create new column in dataframe with a boolean returning as True if note entry
    was created within two weeks from the date of first use for that user.
    '''
    df_entries['notes_w1w2'] = (df_entries.entry_time.dt.date < df_entries['two_weeks']) \
                                    & (df_entries.note.notnull())
    return df_entries

def notes_total(df_entries):
    '''
    Create new column in dataframe with a boolean returning as True if note was included
    in entry.
    '''
    df_entries['notes_total'] = df_entries.note.notnull()

    return df_entries

def add_entrytime_features(df_entries):
    '''
    Add new features to entries data frame using helper functions in this module.
    '''
    pipeline = [entries_one_week, entries_two_weeks, \
                entries_post_one_week, entries_post_two_weeks, \
                moods_w1, moods_w1w2, moods_total, \
                notes_w1, notes_w1w2, notes_total]

    for step in pipeline:
        step(df_entries)

    return df_entries

def user_entry_counts(df_entries):
    '''
    Create groupby object summarizing entry data by user_id.
    '''
    groupby_entries = df_entries.groupby('user_id')
    user_entry_counts = groupby_entries.aggregate(np.count_nonzero) \
                        [['id', 'entries_w1', 'entries_post_w1', 'entries_w1w2', \
                          'entries_post_w2', 'moods_w1', 'moods_w1w2', 'moods_total', \
                          'notes_w1', 'notes_w1w2', 'notes_total']]
    user_entry_counts.rename(columns={'id' : 'total_entries'}, inplace=True)
    return user_entry_counts
