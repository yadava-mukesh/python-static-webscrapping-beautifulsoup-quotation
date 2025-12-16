from bs4 import BeautifulSoup
import requests
import pandas as pd

response = requests.get('http://quotes.toscrape.com/')

#print(response.text)

quotes = BeautifulSoup(response.text, 'html.parser')

#print(quotes)
quotation=[]
author=[]
for quote in quotes.find_all('div', class_='quote'):
    actual_quote=quote.find('span', class_="text")
    #print(actual_quote.text)
    quotation.append(actual_quote.text)
    said_by= quote.find('small', class_='author')
    #print(said_by.text)
    author.append(said_by.text)
    #print(' ')

df=pd.DataFrame({'quote':quotation,'author':author})

#print(df)
df.to_csv('quotes.csv',index=False)