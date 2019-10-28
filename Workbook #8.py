#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
Location = "Documents/School work/ISM 4402 Business Intelligence/datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[2]:


df.hist()


# In[3]:


df.hist(column="age")


# In[4]:


df.hist(column="age", by="gender")


# In[ ]:




