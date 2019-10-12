#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd

Location = "Documents/School work/ISM 4402 Business Intelligence/datasets/gradedata.csv"
df = pd.read_csv(Location)

df.head()


# In[8]:


def gen_to_num(x):
    if x == 'female':
        return 1
    if x == 'male':
        return 0


# In[9]:


df['gender_val'] = df['gender'].apply(gen_to_num)
df.tail()


# In[10]:


import statsmodels.formula.api as sm
result = sm.ols(formula='gender ~ age + exercise + hours + gender_val', data=df).fit()
print (result.summary())


# In[11]:


import statsmodels.formula.api as sm
result = sm.ols(formula='gender ~ exercise + hours + gender_val', data=df).fit()
print (result.summary())


# In[ ]:




