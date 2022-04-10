from src.modules.csv.to_csv import to_csv
from src.products.getters.ozone import *
from src.products.price_trigger import *
category = '/laptopi-i-computri/mrejovi/routers/?limit=100&marka='
brand = 'asus'

products = get_ozone(category, brand)
to_csv(products)
print(price_trigger(products))
