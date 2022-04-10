# beautifulsoup4 4.10.0 - https://pypi.org/project/beautifulsoup4/
import requests
from bs4 import BeautifulSoup
from soupsieve import select


def get_ozone(category, brand):
    base_url = 'https://ozone.bg'
    url = base_url+category+brand
    top_items = []
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    products = soup.select('span.title-option-wrapper')

    for product in products:
        title = product.select('span.title')[0].text
        # price = abc(product)
        price = product.select('span.price')[0].text
        # print(price)
        info = {
            "title": title.strip(),
            "price": price.strip()
        }

        top_items.append(info)
    return top_items


# def abc(product):
#     if product.select('p.special-price')[0]:
#         return product.select('p.special-price')[0].select('span.price')[0].text
#     else:
#         return product.select('span.price')[0].text
