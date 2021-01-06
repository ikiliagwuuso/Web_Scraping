#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import dependencies
import requests
from bs4 import BeautifulSoup as bs


# In[2]:


url = "https://ng.indeed.com/jobs?q=python&l="


# In[7]:


job=input('Job Location?')


# In[8]:


response = requests.get(url + job)
# soup = bs(response.content)
# results = soup.find(id='resultsCol')
# jobs = results.find_all('div', class_='result')
# jobs = results.find_all('div', class_='row')
# job_titles = [job.find('h2').find('a').text.strip() for job in jobs]
# print(job_titles)


# In[9]:


soup = bs(response.content)


# In[10]:


soup


# In[ ]:




