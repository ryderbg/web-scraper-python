import requests
from bs4 import BeautifulSoup

base_url = 'https://ozone.bg'
category = '/laptopi-i-computri/mrejovi/routers/?marka='
brand = 'asus'
url = base_url+category+brand

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

top_items = []
products = soup.select('span.title-option-wrapper')

#WIP
for product in products:
    title = product.select('span.title')[0].text
    price = product.select('span.price')[0].text
    info = {
        "title": title.strip(),
        "price": price.strip()
    }
    # print(title)

    top_items.append(info)

print(top_items)

