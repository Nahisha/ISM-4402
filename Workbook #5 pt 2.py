#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
 
names = ['Bob','Jessica','Mary','John','Mel','Sam','Cathy','Henry','Lloyd']
grades = [76,95,77,78,99,84,79,100,73]
bsdegrees = [1,1,0,0,1,1,1,0,1]
msdegrees = [2,1,0,0,0,1,1,0,0]
phddegrees = [0,1,0,0,0,2,1,0,0]
 
GradeList = zip(names,grades,bsdegrees,msdegrees,phddegrees)
df = pd.DataFrame(data = GradeList, columns=['Names','Grades','BS','MS','PhD'])
df


# In[2]:


df.loc[df['MS']==1]['Grades'].mean()


# In[3]:


df.loc[df['MS']>0]['Grades'].mean()


# In[ ]:




