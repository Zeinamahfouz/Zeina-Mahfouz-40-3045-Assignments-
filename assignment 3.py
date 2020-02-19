#!/usr/bin/env python
# coding: utf-8

# In[2]:


#used for manipulating directory paths
import os 
#scintific and vector computation for python 
import numpy as np
#plotting library

from matplotlib import pyplot

import pandas as pd


# In[4]:


data=pd.read_csv("house_data_complete.csv")
data


# In[7]:


train,validate,test=np.split(data.sample(frac=1),[int(.6*len(data)),int(.8*len(data))])


# In[8]:


train


# In[9]:


validate


# In[ ]:


x,y = train[:,2],train[:,3] 

