def price_trigger(products):
  items = []
  for product in products:
      price = product["price"].split("\xa0лв.")[0].replace(',', '.')
      if float(price) < 100:
        print(product["title"])
      items.append(product)
  return items
