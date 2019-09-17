#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

all_data = pd.dataframe()

df = pd.read_excel("Documents/School work/ISM 4402 Business Intelligence/datasets/data1.xlsx")
all_data  = all_data.append(df,ignore_index=True)

df = pd.read_excel("Documents/School work/ISM 4402 Business Intelligence/datasets/data2.xlsx")
all_data  = all_data.append(df,ignore_index=True)

df = pd.read_excel("Documents/School work/ISM 4402 Business Intelligence/datasets/data3.xlsx")
all_data  = all_data.append(df,ignore_index=True)

all_data.describe()


# In[2]:


import glob 

all_data = pd.dataframe()
for f in glob.glob("Documents/School work/ISM 4402 Business Intelligence/datasets/weekly_call_data/weekdata*.xlsx"):
    df = pd.read_excel(f)
    all_data = all_data.append(df,ignore_index=True)
    
all_data.describe()


# In[ ]:




