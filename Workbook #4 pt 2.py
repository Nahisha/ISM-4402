#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

Location = "Documents/School work/ISM 4402 Business Intelligence/datasets/gradedata.csv"
df = pd.read_csv(Location)

df.head()


# In[8]:


import numpy as np
df['timemgmt'] = np.where((df['exercise']>3) & (df['hours']>17), 'busy', 'normal')
df.tail(10)


# In[ ]:




