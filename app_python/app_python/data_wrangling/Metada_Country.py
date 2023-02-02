#!/usr/bin/env python
# coding: utf-8

# In[4]:


import os
import pandas as pd
from sqlalchemy import create_engine


# In[2]:
path = "/workspaces/app_python/data_wrangling/NY.GDP.MKTP.KD.ZG_DS2/Metadata_Country_API_NY.GDP.MKTP.KD.ZG_DS2_en_csv_v2_4770541.csv"
metadata = pd.read_csv(path)
metadata = metadata.rename(columns={'Country Code':'country_code', 'Region': 'region', 'IncomeGroup':'incomegroup', 'SpecialNotes':'special_notes', 'TableName':'table_name'}, inplace = False)
print(metadata.head())


# In[3]:


metadata.drop(columns=["special_notes", "Unnamed: 5"], inplace=True)


# In[ ]:


engine = create_engine('postgresql://postgres:postgres@db:5432/postgres')
metadata.to_sql('Metadata_Country', engine)

