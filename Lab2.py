#!/usr/bin/env python
# coding: utf-8

# In[9]:


import matplotlib.pyplot as plt

#a) Create a figure object called fig using plt.figure()
fig=plt.figure()

#b) Use add_axes to add an axis to the figure canvas at [0,0,1,1]. Call this new axis ax.
ax=fig.add_axes([0,0,1,1])

#c) Plot (x,y) on that axes and set the labels and titlesx = [0,20,40,60,80,100]
x=[0,20,40,60,80,100]
y=[0,40,80,120,160,200]

ax.plot(x, y)
ax.set_yticks([0, 50, 100, 150, 200])
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('title')

plt.show()


# In[17]:


import matplotlib.pyplot as plt

fig=plt.figure()

ax1=fig.add_axes([0,0,1,1])
ax2=fig.add_axes([0.2,0.5,.2,.2])

ax1.plot(x,y)
ax1.set_title('Axis-1')
ax2.plot(x,y)
ax2.set_title('Axis-2')
plt.show()



# In[26]:


import pandas as pd
import matplotlib.pyplot as plt  

df = pd.read_csv("/home/ustudent/Downloads/company_sales_data.csv")
profitList = df ['total_profit'].tolist()
monthList  = df ['month_number'].tolist()
plt.plot(monthList, profitList, label = 'Month-wise Profit data of last year')
plt.xlabel('Month Number')
plt.ylabel('Total profit')
plt.xticks(monthList)
plt.title('Company profit per month')
plt.yticks([100000, 200000, 300000, 400000, 500000])
plt.show()


# In[39]:


import pandas as pd
import matplotlib.pyplot as plt  

df = pd.read_csv("/home/ustudent/Downloads/company_sales_data.csv")
profitList = df ['total_profit'].tolist()
monthList  = df ['month_number'].tolist()

plt.plot(monthList, profitList, label = 'Profit data of last year', 
      color='r', marker='o', markerfacecolor='k', 
      linestyle='--', linewidth=3)
      
plt.xlabel('Month Number')
plt.ylabel('Sold units number')
plt.legend(loc='lower right')
plt.title('Total profit per month')
plt.xticks(monthList)
plt.yticks([100000, 200000, 300000, 400000, 500000])
plt.show()


# In[42]:


import pandas as pd
import matplotlib.pyplot as plt  

df = pd.read_csv("/home/ustudent/Downloads/company_sales_data.csv")
monthList  = df ['month_number'].tolist()
faceCremSalesData   = df ['facecream'].tolist()
faceWashSalesData   = df ['facewash'].tolist()
toothPasteSalesData = df ['toothpaste'].tolist()
bathingsoapSalesData   = df ['bathingsoap'].tolist()
shampooSalesData   = df ['shampoo'].tolist()
moisturizerSalesData = df ['moisturizer'].tolist()

plt.plot(monthList, faceCremSalesData,   label = 'Face cream Sales Data', marker='o', linewidth=3)
plt.plot(monthList, faceWashSalesData,   label = 'Face Wash Sales Data',  marker='o', linewidth=3)
plt.plot(monthList, toothPasteSalesData, label = 'ToothPaste Sales Data', marker='o', linewidth=3)
plt.plot(monthList, bathingsoapSalesData, label = 'ToothPaste Sales Data', marker='o', linewidth=3)
plt.plot(monthList, shampooSalesData, label = 'ToothPaste Sales Data', marker='o', linewidth=3)
plt.plot(monthList, moisturizerSalesData, label = 'ToothPaste Sales Data', marker='o', linewidth=3)

plt.xlabel('Month Number')
plt.ylabel('Number of units sold')
plt.legend(loc='upper left')
plt.xticks(monthList)
plt.yticks([1000, 2000, 4000, 6000, 8000, 10000, 12000, 15000, 18000])
plt.title('Sales graph')
plt.show()


# In[41]:


import pandas as pd
import matplotlib.pyplot as plt  


df = pd.read_csv("/home/ustudent/Downloads/company_sales_data.csv")


labels = ['FaceCream', 'FaceWash', 'ToothPaste', 'Bathing soap', 'Shampoo', 'Moisturizer']
salesData = [df['facecream'].sum(), df['facewash'].sum(), df['toothpaste'].sum(), 
             df['bathingsoap'].sum(), df['shampoo'].sum(), df['moisturizer'].sum()]

colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6']


plt.figure(figsize=(10, 8)) 
plt.pie(salesData, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140)

# Add a legend and title
plt.legend(loc='lower right')
plt.title('Sales pie chart')


plt.axis('equal')

plt.show()


# In[ ]:




