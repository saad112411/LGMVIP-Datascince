#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[15]:


pd.read_csv('D:/TEA67/ics/DSv/oceania_covid.csv')


# In[20]:


var = pd.read_csv('D:/TEA67/ics/DSv/oceania_covid.csv')


# In[21]:


var.isnull().any()


# In[22]:


var.notnull()


# In[23]:


df = pd.DataFrame(var)
print(df)


# In[24]:


df = pd.DataFrame(var)
print(df.describe())


# In[25]:


df.head(5)


# In[26]:


df.tail()


# In[28]:


df.index


# In[29]:


df.columns


# In[33]:


df.shape


# In[36]:


df.dtypes


# In[39]:


df.columns.values


# In[41]:


df.describe()


# In[43]:


df['Total Cases']


# In[44]:


df.sort_index(axis=1,ascending=False)


# In[45]:


df.sort_values(by='Country/Other')


# In[46]:


df.iloc[5]


# In[47]:


df[0:3]


# In[48]:


df.loc[:, ["Country/Other","Total Cases"]]


# In[54]:


df.info()


# In[51]:


df['Active Cases'] = df['Active Cases']/df['Active Cases'].max()
df['Total Tests'] = df['Total Tests']/df['Total Tests'].max()


# In[53]:


df['Total Recovered'] = df['Total Recovered']/df['Total Recovered'].max()
df[["Active Cases","Total Tests","Total Recovered"]].head()


# In[ ]:




