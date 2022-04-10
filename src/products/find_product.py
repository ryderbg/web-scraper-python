def find_product(products, name):
    items = []
    for product in products:
        title = product["title"]
        if name in title:
            # price = product["price"].split("\xa0лв.")[0].replace(',', '.')
            # if float(price) < 100:
            print(title)

        items.append(product)
    return items
