import csv


def to_csv(products):
    with open('price_list.csv', 'w', newline='') as file:
        fieldnames = ['title', 'price', 'availability']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(products)
