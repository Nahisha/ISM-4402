#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

Location = "Documents/School work/ISM 4402 Business Intelligence/datasets/gradedata.csv"
df = pd.read_csv(Location)

df.head()


# In[2]:


bins = [0,80,100]
status_names = ['Fail','Pass']
df['status'] = pd.cut(df['grade'], bins, labels=status_names)
df


# In[3]:


pd.value_counts(df['status'])


# In[ ]:




