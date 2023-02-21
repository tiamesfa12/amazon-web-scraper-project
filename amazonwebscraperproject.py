#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# import libraries

from bs4 import BeautifulSoup
import requests
import time
import datetime

import smtplib


# In[ ]:


# Connect to the website

URL = 'https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_5?keywords=data%2Banalyst%2Bshirt&qid=1676944054&sprefix=data%2Banalyst%2B%2Caps%2C114&sr=8-5'

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:105.0) Gecko/20100101 Firefox/105.0", "Accept-Encoding": "gzip, deflate, br", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find(id='productTitle').get_text()

price = soup2.find(id='priceblock_ourprice').get_text()



#print(title)
#print(price)


# In[ ]:


price = price.strip()[1:] # removes the dollar sign from the price
title = title.strip() #cleans up the title and makes it look better

print(title)
print(price)


# In[ ]:


import datetime
today = datetime.date.today()

print(today) # will print todays date


# In[ ]:


import csv

header = ['Title', 'Price', 'Date']
data = [title, price, date]

with open('AmazonWebScraperDataset.csv', 'w', newline='', encoding='UTF8') as f: # run this one time, once run you can comment it out
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)


# In[ ]:


import pandas as pd

df = pd.read_csv(r'C:\Users\tiame\AmazonWebScraperDataset.csv')

print(df)


# In[ ]:


#now we start to append or add data to the csv

with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)


# In[ ]:



def check_price():
    URL = 'https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_5?keywords=data%2Banalyst%2Bshirt&qid=1676944054&sprefix=data%2Banalyst%2B%2Caps%2C114&sr=8-5'

    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:105.0) Gecko/20100101 Firefox/105.0", "Accept-Encoding": "gzip, deflate, br", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"}

    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id='productTitle').get_text()

    price = soup2.find(id='priceblock_ourprice').get_text()

    
    price = price.strip()[1:] 
    title = title.strip()
    
    import datetime
    today = datetime.date.today()

    print(today)
    
    import csv

    header = ['Title', 'Price', 'Date']
    data = [title, price, date]

    with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)
    


# In[ ]:


while(True):
    check_price()
    time.sleep(86400) # every 10 seconds it will run the entire process


# In[ ]:


import pandas as pd

df = pd.read_csv(r'C:\Users\tiame\AmazonWebScraperDataset.csv')

print(df)


# In[ ]:




