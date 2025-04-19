#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np 


# In[6]:


df = pd.DataFrame({"user_id": [1,2,3,4,5,6,7,8,9,10,11],
                   "acessos_app": [9,34, None,None,727, None,1,22,None,None,None],
                  "acesso_web": [None, 9834,1,19,99,102,None,None,21,87,None]})


# In[7]:


df


# In[8]:


df['tem_app'] = np.where(df.acessos_app > 0, 
                        True,
                        False)


# In[9]:


df


# In[11]:


df['tem_web'] = np.where(df.acesso_web > 0,
                        True,
                        False)


# In[12]:


df


# In[13]:


df['app_e_web'] = np.where((df.tem_app == True) & (df.tem_web == True),
                          True,
                          False)


# In[14]:


df


# In[17]:


df['app_ou_web'] = np.where( (df.tem_web == True) | (df.tem_app == True),
                            True,
                            False)


# In[18]:


df


# In[ ]:




