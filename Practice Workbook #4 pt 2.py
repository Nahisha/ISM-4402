#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

Location = "Documents/School work/ISM 4402 Business Intelligence/datasets/gradedata.csv"
df = pd.read_csv(Location)

df.head()


# In[3]:


import numpy as np
df ['isFailing'] = np.where(df['grade']<70, 'yes', 'no')
df.tail(10)


# In[4]:


df ['isFailingMale']= np.where((df ['grade']<70) & (df['gender']== 'male'), 'yes', 'no')
df.tail(10)


# In[ ]:




