from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome()
products = []
prices = []
ratings = []
description = []
driver.get("https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
content = driver.page_source
soup = BeautifulSoup(content,features="html.parser")
for a in soup.findAll('a',href=True, attrs={'class':'_1YokD2 _3Mn1Gg'}):
	products = a.find('div', attrs={'class':'_4rR01T'})
	ratings = a.find('div', attrs={'class':'gUuXy-'})
	description = a.find('div', attrs={'class':'fMghEO'})
	prices = a.find('div', attrs={'class':'_3tbKJL'})
	products.append(names.text)
	ratings.append(ratings.text)
	description.append(descriptions.text)
	prices.append(prices.text)
df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings, 'Description':description}) 
df.to_csv('products.csv', index=False, encoding='utf-8')


