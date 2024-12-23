#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
import module1 as m1


# In[ ]:


def drop_columns():
    ds = m1.rename_columns()
    # Method to drop unnecessary columns from the DataFrame.
    # Returns: DataFrame with specified columns dropped.
    dropped_columns = ['PatientId', 'AppointmentID', 'Neighbourhood']
    ds.drop(columns=dropped_columns, inplace=True)
    
    return ds


# In[ ]:


def create_bin():
    ds = drop_columns()
    #First Drop rows with Age == 0
    ds = ds[ds['Age'] != 0]
    # Generating labels for age intervals (e.g., '1 - 20', '21 - 40', etc.)
    labels = ["{0} - {1}".format(i, i + 20) for i in range(1, 118, 20)]

    # Using the pd.cut() function to categorize ages into groups(use bins = range(1, 130, 20) ,right=False and use the given labels)
    ds['Age_group'] = pd.cut(ds['Age'], bins=range(1, 130, 20), labels=labels, right=False)

    # Returning the modified dataset with assigned age groups
    return ds


# In[ ]:


def drop():
    ds = create_bin()
    # Method to drop the original 'Age' column from the DataFrame.
    # Returns: DataFrame with the 'Age' column dropped.
    ds.drop(columns=['Age'], inplace=True)
    
    return ds


# In[ ]:


def convert():
    ds = drop()
    # Method to convert 'NoShow' values into binary values (1 for 'Yes' and 0 for 'No').
    # Returns: DataFrame with 'NoShow' column values converted to 1s and 0s.
    binary_map = {'No': 0, 'Yes': 1}
    ds['NoShow'] = ds['NoShow'].map(binary_map)

    return ds


# In[ ]:


def export_the_dataset():
    df = convert()
    # Export the cleaned dataset and set the index=false and return the same as 'df'
    df.to_csv("Hospital_patients_datasets_cleaned.csv", index=False)
    
    return df


# In[ ]:


drop_columns()
create_bin()
drop()
convert()
export_the_dataset()


# In[ ]:




