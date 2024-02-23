# list of dictionaries
products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Smartphone", "price": 800},
    {"name": "Tablet", "price": 500},
    {"name": "Headphones", "price": 120},
]

# setting default value for max price
max_price=0

# checking the maximum price in the dictionary
for product in products:
    if (max_price<product["price"]):
        max_price=product["price"]
    for item in product:
        if product["price"]==max_price: 
            print (product)
