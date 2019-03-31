#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
TODO:

1. Split the text variable into a list of the individual fruits.

2. For all the names in the list that don't start with 'a', 
   use an f-string to print the string:

    Yes, we have no [fruit name] today.
'''

text = 'apples,oranges,kiwis,bananas'


# In[4]:


fruit_list = text.split(',')
print(fruit_list)


# In[6]:


for item in fruit_list:
    if item[0].lower() != 'a':
        print(f'Yes, we have no {item} today')
        


# In[ ]:




