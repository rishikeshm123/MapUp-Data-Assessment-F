#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[4]:


df1 = pd.read_csv("dataset-1.csv")
df1


# In[5]:


def generate_car_matrix(df)->pd.DataFrame:
    df = df.pivot(index='id_1', columns='id_2', values=['car']).fillna(0)
    return df


# In[6]:


def get_type_count(df)->dict:
    """
    Categorizes 'car' values into types and returns a dictionary of counts.

    Args:
        df (pandas.DataFrame)

    Returns:
        dict: A dictionary with car types as keys and their counts as values.
    """
    # Write your logic here
    
    df['car_type'] = pd.cut(df['car'], bins=[0, 15, 25, float('Inf')], labels=['low', 'medium', 'high'])
    
    return df1['car_type'].value_counts().to_dict()


# In[7]:


def get_bus_indexes(df)->list:
    """
    Returns the indexes where the 'bus' values are greater than twice the mean.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of indexes where 'bus' values exceed twice the mean.
    """
    # Write your logic here
    mean  = df['bus'].mean()
    
    filtered_indices = df1[df1['bus'] > 2 * mean].index.tolist()

    return sorted(filtered_indices)


# In[8]:


def filter_routes(df)->list:
    """
    Filters and returns routes with average 'truck' values greater than 7.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of route names with average 'truck' values greater than 7.
    """
    # Write your logic here
    route_avg_truck = df.groupby('route')['truck'].mean()
    filtered_routes = route_avg_truck[route_avg_truck > 7].index.tolist()
    return  sorted(filtered_routes)


# In[9]:


def multiply_matrix(matrix)->pd.DataFrame:
    """
    Multiplies matrix values with custom conditions.

    Args:
        matrix (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Modified matrix with values multiplied based on custom conditions.
    """
    # Write your logic here
    df = matrix.applymap(lambda x: x * 0.75 if x > 20 else x * 1.25)
    
    return df


# In[10]:


def time_check(df):
    df['start_timestamp'] = pd.to_datetime(df['startDay'] + ' ' + df['startTime'])
    df['end_timestamp'] = pd.to_datetime(df['endDay'] + ' ' + df['endTime'])

    df['time_diff'] = (df['end_timestamp'] - df['start_timestamp']).dt.total_seconds()

    result_series = df.groupby(['id', 'id_2']).apply(lambda group: check_timestamps(group)).reset_index(level=[0, 1], drop=True)

    return result_series


# In[ ]:




