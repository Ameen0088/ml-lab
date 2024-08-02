#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#question-1


# In[1]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# In[2]:


fig=plt.figure()
ax=fig.add_axes([0,0,1,1])
x1=[0,20,40,60,80,100]
y1=[0,50,100,150,200]
ax.set_title("title")
ax.set_xlim(0,100)
ax.set_ylim(0,200)
plt.yticks(y1)
plt.plot([0,100],[0,200])
#fig.show()


# In[3]:


#question-2


# In[4]:


fig=plt.figure()
ax1=fig.add_axes([0,0,1,1])
ax2=fig.add_axes([0.2,0.5,.2,.2])
ax1.plot([0,100],[0,200])
ax2.plot([0,100],[0,200])

fig.show()


# In[5]:


#question-3


# In[7]:


df=pd.read_csv('company_sales_data.csv')
# df['total_profit'].plot()
plt.plot(df['month_number'],df['total_profit'])
plt.xlabel('Month Number')
plt.ylabel('Total Profit')
plt.xticks(df['month_number']) 
plt.show()


# In[8]:


#question-4


# In[9]:


df=pd.read_csv('company_sales_data.csv')
plt.plot(df['month_number'],df['total_units'],linestyle = 'dotted',color='r',label='line',marker='o',mfc='r',linewidth='3')
plt.xlabel('Month Number')
plt.ylabel('Sold units number')
plt.xticks(df['month_number']) 
plt.legend(loc="lower right")
plt.show()


# In[10]:


#question-6


# In[11]:


for column in df.columns[1:7]:
    plt.plot(df['month_number'], df[column], label=column)
plt.legend()


# In[12]:


#question-7


# In[13]:


plt.pie(df[df.columns[1:7]].sum(),labels=df.columns[1:7],autopct='%1.1f%%', startangle=140)
plt.show()


# In[ ]:




