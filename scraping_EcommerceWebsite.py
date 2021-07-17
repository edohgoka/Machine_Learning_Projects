# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 16:06:38 2020

@author: goka 
"""


"""
Scrap E-Commerce website

Extract the Price, Name, and Rating, which are contained in the “div” tag, respectively and store them


"""

from bs4 import BeautifulSoup
import requests 
import pandas as pd 

# Creating lists to store scrap data 

product_name = list()
product_price = list()
product_rating = list()

url = "https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
data = requests.get(url)
soup = BeautifulSoup(data.content, "html.parser")
print(soup.title.text)

containers = soup.find_all('a', class_ = "_1fQZEK")
print(type(containers))
print(containers[0])


for container in containers:
	name = container.find('div',class_ = '_4rR01T')
	product_name.append(name.text)
 
	price = container.find('div',class_ = '_3tbKJL')
	product_price.append(price.text)
 
	rating = container.find('div', class_ = '_3LWZlK')
	product_rating.append(rating.text)
    
print(len(product_name))
print(len(product_price))
print(len(product_rating))


# Creating a dataframe 
product_dict = {
        'Name' : product_name,
        'Price' : product_price,
        'Rating' : product_rating
        }

df = pd.DataFrame(product_dict)
#print(df)
try:
	df.to_csv('flipkart_data.csv', index=False)
except Exception as e:
	print(e)
