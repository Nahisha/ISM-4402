#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd

names = ['Bob','Jessica','Mary','John','Mel']
status = ['Senior','Freshman','Sophomore','Senior','Junior']
grades = [76,95,77,78,99]
GradeList = zip(names,status,grades)
df = pd.DataFrame(data = GradeList, columns=['Names','Status','Grades'])

get_ipython().run_line_magic('matplotlib', 'inline')
df.plot(kind='bar')


# In[2]:


df2 = df.set_index(df['Status'])
df2.plot(kind="bar")


# In[ ]:




