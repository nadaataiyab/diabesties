from __future__ import print_function, division
import pandas as pd
import numpy as np
import datetime
import join_tables as jt

#FEATURE ENGINEERING FOR USAGE Data

# def a1c_update(row):
#     if row.action == 'a1c_update':
#         return 'a1c_update'
#     else:
#         return row.object_name
#
# def a1c_object_name(df_usage):
#     df_usage = df_usage.copy()
#     df_usage['object_name'] = df_usage.apply(a1c_update, axis=1)
#     return df_usage


def remove_actions(df_usage):
    df_usage = df_usage.copy()
    df_usage = df_usage[df_usage['action'].isin(['page_view', 'a1c_update', 'chat_resume'])]
    return df_usage

def consolidate_actions_helper(row):
    if row.action == 'chat_resume':
        return 'page_view'
    else:
        return row.action

def consolidate_actions(df_usage):
    df_usage = df_usage.copy()
    df_usage['action'] = df_usage.apply(consolidate_actions_helper, axis=1)
    return df_usage

def create_dummies(df_usage):
    df_usage = df_usage.copy()
    df_usage['action'] = df_usage['action'].astype('category')
    df_usage = pd.get_dummies(df_usage, columns=['action'])
    return df_usage


def a1c_w1(df_usage):
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



# def create_pageviews_helper(row):
#     if row.action == 'page_view':
#         return 1
#     else:
#         return 0
#
# def create_pageviews_helper(row):
#     if row.action == 'page_view':
#         return 1
#     else:
#         return 0



# def create_pageviews(df_usage):
#     df_usage['page_views'] =


#
#
#
# def entries_one_week (df_usage):
#     '''
#     ADD DOCUMENTATION
#     '''
#    (df_usage['in_one_week'] = df_entries.entry_time.dt.date < df_entries['one_week']
#     return df_entries
#
# def entries_two_weeks (df_entries):
#     '''
#     ADD DOCUMENTATION
#     '''
#     df_entries['in_two_weeks'] = df_entries.entry_time.dt.date < df_entries['two_weeks']
#     return df_entries
#
# def entries_post_one_week(df_entries):
#     df_entries['post_one_week'] = df_entries.entry_time.dt.date >= df_entries['one_week']
#     return df_entries
#
# def entries_post_two_weeks(df_entries):
#     df_entries['post_two_weeks'] = df_entries.entry_time.dt.date >= df_entries['two_weeks']
#     return df_entries
#
# def moods_one_week(df_entries):
#     df_entries['moods_one_week'] = (df_entries.entry_time.dt.date < df_entries['one_week']) \
#                                     & (df_entries.mood.notnull())
#     return df_entries
#
# def moods_two_weeks(df_entries):
#     pass
#
# def moods_total(df_entries):
#     pass
#
# def notes_one_week(df_entries):
#     pass
#
# def notes_two_weeks(df_entries):
#     pass
#
#
#
# def add_entrytime_features(df_entries):
#     pipeline = [entries_one_week, entries_two_weeks, \
#                 entries_post_one_week, entries_post_two_weeks, \
#                 moods_one_week]
#
#     for step in pipeline:
#         step(df_entries)
#
#     return df_entries
#
# def user_entry_counts(df_entries):
#     '''
#     add docs
#     '''
#     groupby_entries = df_entries.groupby('user_id')
#     user_entry_counts = groupby_entries.aggregate(np.count_nonzero) \
#                         [['id', 'in_one_week', 'in_two_weeks','post_one_week', \
#                           'post_two_weeks', 'moods_one_week']]
#     user_entry_counts.rename(columns={'id' : 'total_entries', \
#                                       'in_one_week' : 'entries_w1', \
#                                       'in_two_weeks' : 'entries_w1w2', \
#                                       'post_one_week' : 'entries_post_w1', \
#                                       'post_two_weeks' : 'entries_post_w2', \
#                                       'moods_one_week' : 'moods_w1'},
#                              inplace=True)
#     return user_entry_counts
