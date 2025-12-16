
from bs4 import BeautifulSoup
import requests

url = "https://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html"

html_text = requests.get(url)
parsed = BeautifulSoup(html_text.text, "html.parser")

print(parsed)
books = parsed.find_all('li', class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")

for book in books:
    h3_tag = book.find("h3")
    a_tag = h3_tag.find('a')
    book_title = a_tag.get('title')
    book_price=book.find('p', class_='price_color')
    stock_available=book.find('p', class_='instock availability')
    print(f'''Book name is {book_title}, 
          Book price is {book_price.text},
          Book is {stock_available.text.strip()}
    ''')
    print('')