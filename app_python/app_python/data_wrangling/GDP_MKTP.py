#!/usr/bin/env python
# coding: utf-8

# # Download CSV from "https://api.worldbank.org/v2/en/indicator/NY.GDP.MKTP.KD.ZG?downloadformat=csv"

# In[1]:

#column_names = ["Country Name", "Country Code", "Column Composition"]

#get_ipython().system('curl "https://api.worldbank.org/v2/en/indicator/NY.GDP.MKTP.KD.ZG?downloadformat=csv" -O -J -L')


# In[ ]:


#get_ipython().system('unzip API_NY.GDP.MKTP.KD.ZG_DS2_en_csv_v2_4770541.zip -d NY.GDP.MKTP.KD.ZG_DS2')


# In[22]:


import os
import pandas as pd
from sqlalchemy import create_engine


# In[23]:

#Country Name","Country Code","Indicator Name","Indicator Code"

path = "/workspaces/app_python/data_wrangling/NY.GDP.MKTP.KD.ZG_DS2/"
filepath = os.path.join(path, "API_NY.GDP.MKTP.KD.ZG_DS2_en_csv_v2_4770541.csv")
gdp = pd.read_csv(filepath_or_buffer=filepath, skiprows=3)
gdp = gdp.rename(columns={'Country Name': 'country_name', 'Country Code': 'country_code', 'Indicator Name':'indicator_name', 'Indicator Code':'indicator_code', 'Column Composition': 'column_composition'}, inplace=False)
print(gdp.head())


# In[24]:


gdp.head(3)


# In[25]:


gdp.drop(columns=["Unnamed: 66"], inplace=True)


# In[26]:


id_vars = gdp.columns[:4]
value_vars = gdp.columns[4:]


# In[27]:


gdp_melted = pd.melt(gdp, id_vars=id_vars, value_vars=value_vars, var_name="Year", value_name="GDP")


# In[28]:


gdp_melted.tail(80)


# In[38]:


gdp_melted.info()


# In[36]:


gdp_melted["country_name"].tolist() == len(gdp_melted["country_name"].unique().tolist())


# In[ ]:

engine = create_engine('postgresql://postgres:postgres@db:5432/postgres')
gdp_melted.to_sql('GDP_MKTP', engine)

