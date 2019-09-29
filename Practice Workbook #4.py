#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd

Location = "Documents/School work/ISM 4402 Business Intelligence/datasets/gradedata.csv"
df = pd.read_csv(Location)

df.head()


# In[11]:


#Create bin dividers
bins = [0, 60, 70, 80, 90, 100]

#Create names for the four groups
group_names = ['F','D','C','B','A']


# In[12]:


df['lettergrade']= pd.cut(df['grade'], bins, labels=group_names)
df


# In[14]:


# View counts by bin
pd.value_counts(df['lettergrade'])


# In[ ]:




