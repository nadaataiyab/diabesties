from __future__ import print_function, division
import pandas as pd
import numpy as np
import datetime
import join_tables as jt

def remove_test_users(df):
    df = df.copy()
    df = df[df['user_id'] > 5]
    return df

def srub_age(df_demo):
    median_age = df_demo['age'].median()
    df_demo['age2'] = df_demo.age.map(lambda x: median_age if x > 100 \
                                          or x < 13 else x)
    df_demo.age2.fillna(median_age, inplace=True)
    return df_demo

def convert_null_time_entries(df_demo):
    features = ['total_entries', 'entries_w1', 'entries_post_w1', 'entries_w1w2', \
                'entries_post_w2', 'moods_w1', 'moods_w1w2', 'moods_total', \
                'notes_w1', 'notes_w1w2', 'notes_total', 'total_usage_counts', \
                'a1c_w1', 'a1c_w1w2', 'a1c_total', 'page_view_w1', 'page_view_w1w2', \
                'page_view_total']
    for feature in features:
        df_demo[feature].fillna(0, inplace=True)

    return df_demo
