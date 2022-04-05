from src.get_products.get_ozone import *
from src.get_products.price_trigger import *
category = '/laptopi-i-computri/mrejovi/routers/?marka='
brand = 'asus'

products = get_ozone(category, brand)
print(price_trigger(products))