#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

names = ['Bob','Jessica','Mary','John','Mel','Sam','Courtney','Jackie']
grades = [76,95,77,77,99,80,32,50]
hoursstudy = [11,5,5,3,0,3,2,1]

GradeList = zip(names,grades,hoursstudy)
df = pd.DataFrame(data = GradeList, columns=['Names','Grades','StudyHours'])
df


# In[18]:


print ('Count:', df['Grades'].count()) # computes the number of values

print ('mean:', df['Grades'].mean())   # computes the arithmetic average of the values 

print ('standard deviation:', df['Grades'].std())    # computes the standard deviation of the values 

print ('min:', df['Grades'].min())    # computes the minimum of the values 
print ('max:', df['Grades'].max())    # computes the maximum of the values 

print ('1st quartile:', df['Grades'].quantile(.25))  # computes the first quartile of the values 
print ('2nd quartile:', df['Grades'].quantile(.5))   # computes the second quartile of the values 
print ('3rd quartile:', df['Grades'].quantile(.75))  # computes the third quartile of the values 


# In[4]:


df.describe()


# In[5]:


df['Grades'].count()


# In[19]:


# computes the arithmetic average of the values in a column
# mean = dividing the sum of all values by the number of values
print ('mean:', df['Grades'].mean()) 

#finds the median of the values in a column
# median = the middle value if they are sorted in order
print ('median:', df['Grades'].median())

# finds the mode of the values in a column
# mode = the most common single values
print ('mode:', df['Grades'].mode())


# In[20]:


# computes the variance of the values in a column
print ('variance:', df['Grades'].var())


# In[21]:


# finds the average value for all of the columns for which an arithmetic average is findable
df.mean()


# In[ ]:




