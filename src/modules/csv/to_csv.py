import csv
def to_csv(products):
    csv_rowlist = []
    for product in products:   
        csv_rowlist.append(f"[{product}]")
    print(csv_rowlist)
    with open('products.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            # writer.writerow(["SN", "Product", "Price"])
            writer.writerows(csv_rowlist)
            # writer.writerow([2, "Harry Potter", "Harry Potter"])