#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#BASIC STATISTICS : FREQUENCY TABLE

# extracted from report genered by 1st Agency for Home Health Care when assessing expansion to other counties.
# imported spreadsheet data represents the number of home health care agencies in 60 different counties. 
# a fequency table is represented to organize the data in a readable manner.


# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[24]:


# import excel spreadsheett (raw data)
rawDataHHC = pd.read_excel('rowDataHHC.xlsx')


# In[34]:


rawDataHHC.head()


# In[27]:


# basic frequency table for data
frequencyTable = pd.crosstab(index=rawDataHHC['Number of Agency'], columns='count')


# In[33]:


frequencyTable.head()


# In[41]:


# frequency for class limit 0-21
GroupFreq021 = frequencyTable.iloc[0:13].sum()


# In[42]:


GroupFreq021


# In[37]:


# frequency for class limit 22-43
GroupFreq2243 = frequencyTable.iloc[13:21].sum()


# In[38]:


GroupFreq2243


# In[39]:


# frequency for class limit 44-65
GroupFreq4465 = frequencyTable.iloc[21:22].sum()


# In[40]:


GroupFreq4465


# In[31]:


# final readable frequency table
Freqtabl = pd.DataFrame({'# Agency': ['0-21', '22-43', '22-65','66-87', '88-109', '100-131','176-197','264-285','374-395'],'Tally':['////////// ////////// ////////// ///////', '////////// /','//', '/','///','/','/','//','/' ], 
                        'Frequency': [37, 11, 2, 1, 3, 1,  1, 2, 1]})


# In[32]:


Freqtabl


# In[ ]:


# the frequenct distribution shows most counties have less than 22 home health agencies. 
# assuming other factors being hold, these areas could have more opportunity for expansion.
# Avoid saturated areas.

