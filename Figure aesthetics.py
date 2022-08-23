#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import seaborn as sns


# In[3]:


import matplotlib.pyplot as plt


# In[4]:


def sinplot(flip=1):
    x = np.linspace(0, 14, 100)
    for i in range(1, 7):
        plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)


# In[5]:


sinplot()


# In[6]:


sns.set_theme()
sinplot()


# In[7]:


sns.set_style("whitegrid")
data = np.random.normal(size=(20, 6)) + np.arange(6) / 2
sns.boxplot(data=data);


# In[8]:


sns.set_style("dark")
sinplot()


# In[9]:


sns.set_style("white")
sinplot()


# In[10]:


sns.set_style("ticks")
sinplot()


# In[11]:


sinplot()
sns.despine()


# In[12]:


f, ax = plt.subplots()
sns.violinplot(data=data)
sns.despine(offset=10, trim=True);


# In[13]:


sns.set_style("whitegrid")
sns.boxplot(data=data, palette="deep")
sns.despine(left=True)


# In[14]:


f = plt.figure(figsize=(6, 6))
gs = f.add_gridspec(2, 2)

with sns.axes_style("darkgrid"):
    ax = f.add_subplot(gs[0, 0])
    sinplot()

with sns.axes_style("white"):
    ax = f.add_subplot(gs[0, 1])
    sinplot()

with sns.axes_style("ticks"):
    ax = f.add_subplot(gs[1, 0])
    sinplot()

with sns.axes_style("whitegrid"):
    ax = f.add_subplot(gs[1, 1])
    sinplot()

f.tight_layout()


# In[17]:


sns.axes_style()
sns.set_style("darkgrid", {"axes.facecolor": ".9"})
sinplot()


# In[18]:


sns.set_theme()
sns.set_context("paper")
sinplot()


# In[19]:


sns.set_context("talk")
sinplot()


# In[20]:


sns.set_context("poster")
sinplot()


# In[21]:


sns.set_context("notebook", font_scale=1.5, rc={"lines.linewidth": 2.5})
sinplot()


# In[ ]:




