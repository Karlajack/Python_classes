products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Smartphone", "price": 800},
    {"name": "Tablet", "price": 500},
    {"name": "Headphones", "price": 120},
]

max_price=0
for product in products:
    if (max_price<product["price"]):
        max_price=product["price"]

   

print(f" {max_price} ")





#print(f"(product["name"],product["price"],sep=",")
    
