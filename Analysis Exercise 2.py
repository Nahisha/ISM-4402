#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

Location = "Documents/School work/ISM 4402 Business Intelligence/datasets/axisdata.csv"
df = pd.read_csv(Location)
df.head()


# In[2]:


df['Cars Sold'].mean()


# In[3]:


df['Cars Sold'].max()


# In[4]:


df['Cars Sold'].min()


# In[5]:


pd.pivot_table(df, values=['Cars Sold'], index=['Gender'])


# In[6]:


df[df['Cars Sold']>3]['Hours Worked'].mean()


# In[7]:


df['Years Experience'].mean()


# In[8]:


df[df['Cars Sold']>3]['Years Experience'].mean()


# In[9]:


pd.pivot_table(df, values=['Cars Sold'], index=['SalesTraining'])


# In[16]:


import matplotlib.pyplot as plt
import pandas as pd

names = ['Jada','Nicole','Tonya','Ronelle','Brad']
yearsexperience = [3,3,4,5,4]
carssold = [2,6,6,3,2]
ExperienceList = zip(carssold,yearsexperience)
df = pd.DataFrame(data = ExperienceList, columns=['CarsSold', 'YearsExperience'])

get_ipython().run_line_magic('matplotlib', 'inline')
df.plot(kind='bar')


# In[18]:


import pandas as pd

names = ['Jada','Nicole','Tonya','Ronelle','Brad']
hoursworked = [39,46,42,38,32]
carssold = [2,6,6,3,2]
HoursWorkedList = zip(names,carssold,hoursworked)
df = pd.DataFrame(data = HoursWorkedList, columns=['Names', 'CarsSold', 'HoursWorked'])

get_ipython().run_line_magic('matplotlib', 'inline')
df.plot()


# In[ ]:




