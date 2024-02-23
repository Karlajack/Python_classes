products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Smartphone", "price": 1800},
    {"name": "Tablet", "price": 500},
    {"name": "Headphones", "price": 120},
]

max_price=0
for product in products:
    for k,v in product.items():
        if (max_price<product.items["price"]):
            max_price=product["price"]
        if v in  product.items()==max_price:
            new_prod={k:v for k,v in product.items()}
            print (new_prod)
        print(v)

            