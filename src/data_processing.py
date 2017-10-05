from __future__ import print_function, division
import pandas as pd
import numpy as np
import datetime

#This module executes a set of preprocessing steps including dropping columns,
#converting data to datetime objects, booleans, categories, and numerical
#data. The functions use a dataframe with two features: the names of the
#columns in the dataframe to be processed and actions to take on each
#of those columns.

def col_names(df_col_names, value, filter_col='action'):
    '''
    Generate a list of column names that have been assigned to an
    action.

    Parameters
    ----------
    df_col_names: dataframe
        The dataframe has column names and actions to taken on each column
    filter_col: string, default 'action'
        with column name to filter by
    value: string
        String with value to filter on eg. 'drop', 'categorical', 'numerical'

    Returns
    -------
    col_names: list of strings
        List of strings containing names of columns.

    '''
    #generate list of columns to drop
    col_names = list(df_col_names.iloc[:, 0]\
                        [df_col_names[filter_col] == value])

    #convert items in list to a string
    for i in range(len(col_names)):
        col_names[i] = str(col_names[i])

    return col_names

def drop_cols(df, df_col_names):
    '''
    Drop columns from the dataframe by referencing a second dataframe with
    instructions on which columns to drop.

    Parameters
    ----------
    df: dataframe
    df_col_names: dataframe
        Dataframe with column names and actions to take on each column.

    Returns
    -------
    Dataframe with columns dropped as specified.

    '''
    cols_to_drop = col_names(df_col_names, value='drop')
    df = df.copy()
    for col in cols_to_drop:
        df.drop(col, axis=1, inplace=True)
    return df

def convert_datetime(df, df_col_names):
    '''
    Convert data to datetime objects.

    Parameters
    ----------
    df: dataframe
    df_col_names: dataframe
        Dataframe with column names and actions to take on each column.

    Returns
    -------
    Dataframe with specified datetime features changed to datetime objects.

    '''

    cols_datetime = col_names(df_col_names, value='date')
    df = df.copy()
    for col in cols_datetime:
        df[col] = pd.to_datetime(df[col], unit='s')
    return df

def convert_categories(df, df_col_names):
    '''
    Convert categorical data into data type 'category'.

    Parameters
    ----------
    df: dataframe
    df_col_names: dataframe
        Dataframe with column names and actions to take on each column.

    Returns
    -------
    Dataframe with specified features changed to categories.

    '''
    cols_categorical = col_names(df_col_names, value='categorical')
    df = df.copy()
    for col in cols_categorical:
        df[col] = df[col].astype('category')
    return df

def convert_numerical(df, df_col_names):
    '''
    Convert numerical data into integers and floats.

    Parameters
    ----------
    df: dataframe
    df_col_names: dataframe
        Dataframe with column names and actions to take on each column.

    Returns
    -------
    Dataframe with specified features changed to integers and floats.

    '''
    cols_numerical = col_names(df_col_names, value='numerical')
    df = df.copy()
    for col in cols_numerical:
        df[col] = pd.to_numeric(df[col], errors='force')
    return df

def convert_boolean(df, df_col_names):
    '''
    Parameters
    ----------
    df: dataframe
    df_col_names: dataframe
        Dataframe with column names and actions to take on each column.

    Returns
    -------
    Dataframe with specified features converted to booleans.

    '''

    cols_boolean = col_names(df_col_names, value='boolean')

    df = df.copy()
    for col in cols_boolean:
        df[col] = df[col].astype('bool')
        df[col] = df[col].map(lambda x: 1 if x == True else 0)
    return df



def process_data(df, df_col_names):
    df = df.copy()
    pipeline = [drop_cols, convert_datetime, convert_categories,
                convert_numerical, convert_boolean]

    for step in pipeline:
        df = step(df, df_col_names)

    return df
