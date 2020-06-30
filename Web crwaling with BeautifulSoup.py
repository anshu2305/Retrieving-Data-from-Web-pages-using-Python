#!/usr/bin/env python
# coding: utf-8

# In[1]:


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl


#ssl gives us permissions to access data of ssl certified sites

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup(input("Which tag do you want to retrieve? :"))
for tag in tags:
    print(tag)


# In[ ]:





# In[ ]:




