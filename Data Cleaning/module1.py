#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd


# In[ ]:


def read_csv():
    # Method to read the CSV file "Hospital_patients_datasets.csv" using pandas.
    # Returns: Pandas DataFrame containing the data from the CSV file.
    ds = pd.read_csv("Hospital_patients_datasets.csv")
    
    return ds


# In[ ]:


def check_duplicates():
    ds = read_csv()
    # Method to check for duplicate rows in the DataFrame.
    # Returns: The number of duplicated rows found in the DataFrame.
    ds = ds.duplicated().sum()
    
    return ds


# In[ ]:


def check_null_values():
    ds = read_csv()
    # Method to check for null (missing) values in the DataFrame.
    # Returns: A pandas Series indicating the count of null values for each column in the DataFrame.
    ds = ds.isnull().sum()

    return ds


# In[ ]:


def converting_dtype():
    ds = read_csv()
    # Method to convert 'ScheduledDay' and 'AppointmentDay' columns to datetime objects.
    # Returns: DataFrame with 'ScheduledDay' and 'AppointmentDay' columns converted to datetime objects.
    ds['ScheduledDay'] = pd.to_datetime(ds['ScheduledDay']).dt.tz_localize(None)
    ds['AppointmentDay'] = pd.to_datetime(ds['AppointmentDay']).dt.tz_localize(None)
    
    ds['ScheduledDay'] = ds['ScheduledDay'].dt.date
    ds['AppointmentDay'] = ds['AppointmentDay'].dt.date
    
    ds['ScheduledDay'] = pd.to_datetime(ds['ScheduledDay'])
    ds['AppointmentDay'] = pd.to_datetime(ds['AppointmentDay'])
    
    return ds


# In[ ]:


def rename_columns():
    ds = converting_dtype()
    # Method to rename some columns in the DataFrame.
    # Returns: DataFrame with certain column names changed to new names.
    new_column_names = {'SMS_received': 'SMSReceived', 'Hipertension': 'Hypertension', 'Handcap': 'Handicap', 'No-show': 'NoShow'}
    ds.rename(columns=new_column_names, inplace=True)
    
    return ds


# In[ ]:


read_csv()
check_duplicates()
check_null_values()
converting_dtype()
rename_columns()

