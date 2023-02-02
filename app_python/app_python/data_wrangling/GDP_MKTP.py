import os
import pandas as pd
from sqlalchemy import create_engine


path = "/workspaces/app_python/data_wrangling/NY.GDP.MKTP.KD.ZG_DS2/"
filepath = os.path.join(path, "API_NY.GDP.MKTP.KD.ZG_DS2_en_csv_v2_4770541.csv")
gdp = pd.read_csv(filepath_or_buffer=filepath, skiprows=3)
gdp = gdp.rename(columns={'Country Name': 'country_name', 'Country Code': 'country_code', 'Indicator Name':'indicator_name', 'Indicator Code':'indicator_code', 'Column Composition': 'column_composition'}, inplace=False)
print(gdp.head())


gdp.drop(columns=["Unnamed: 66"], inplace=True)

id_vars = gdp.columns[:4]
value_vars = gdp.columns[4:]


# In[27]:


gdp_melted = pd.melt(gdp, id_vars=id_vars, value_vars=value_vars, var_name="Year", value_name="GDP")

gdp_melted.tail(80)


gdp_melted.info()

["country_name"].tolist() == len(gdp_melted["country_name"].unique().tolist())


engine = create_engine('postgresql://postgres:postgres@db:5432/postgres')
gdp_melted.to_sql('GDP_MKTP', engine)

