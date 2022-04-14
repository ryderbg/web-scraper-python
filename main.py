from src.products.find_product import find_product
from src.modules.csv.to_csv import to_csv
from src.products.getters.dekada import *
from src.products.price_trigger import *
category = '/мишки-c-178.html'
# category = '/laptopi-i-computri/mrejovi/routers/?limit=100&marka='
# brand = 'asus'

products = get_dekada(category)
print(products)
to_csv(products)
# find_product(products, 'AX')
# print(price_trigger(products))
