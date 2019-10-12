#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

Location = "Documents/School work/ISM 4402 Business Intelligence/datasets/gradedata.csv"
df= pd.read_csv(Location)

df.head()


# In[ ]:


df = df.sort_values(by=['fname', 'age', 'grade'], ascec)

