import requests
from bs4 import BeautifulSoup

def get_ozone(category, brand):
  base_url = 'https://ozone.bg'
  url = base_url+category+brand
  top_items = []
  page = requests.get(url)
  soup = BeautifulSoup(page.content, 'html.parser')
  products = soup.select('span.title-option-wrapper')
  
  for product in products:
      title = product.select('span.title')[0].text
      price = product.select('span.price')[0].text
      info = {
          "title": title.strip(),
          "price": price.strip()
      }
  
      top_items.append(info)
  return top_items

