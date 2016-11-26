
# coding: utf-8

# In[4]:


get_ipython().magic(u'matplotlib inline')

import seaborn


# In[5]:

import seaborn as sns

# Load one of the data sets that come with seaborn
tips = sns.load_dataset("tips")

sns.jointplot("total_bill", "tip", tips, kind='reg');


# In[12]:

tips.head()


# In[11]:

print len(tips), 
print len(tips)


# In[ ]:



