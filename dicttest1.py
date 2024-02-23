products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Smartphone", "price": 800},
    {"name": "Tablet", "price": 500},
    {"name": "Headphones", "price": 120},
]

for product in products:
    for k,v in product.items():
        new_prod={k:v for k,v in product.items()} 
        if v==800:
            print (new_prod)
    
   