from fastapi import FastAPI
from models import Product

app = FastAPI()

products = [
    Product(id= 1, name= "Samosa", price= 10),
    Product(id= 2, name= "Pakora", price= 15),
    Product(id= 3, name= "Lassi", price= 20)
]

@app.get("/")
def greet():
    return "Hello, World"

@app.get("/products")
def get_products():
    return products

@app.get("/products/{product_id}")
def get_product(product_id: int):
    for i in range(len(products)):
        if products[i].id == product_id:
            return products[product_id-1]
    
    return "No Products Found"

@app.post("/products")
def add_product(product: Product):
    products.append(product)
    return "Product Added"

@app.put("/products/{product_id}")
def update_product(product_id: int, new_product: Product):
    for i in range(len(products)):
        if products[i].id == product_id:
            products[i].name = new_product.name
            products[i].price = new_product.price
        return "Updated Sucessfully"
    return "No Product Found"

@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for i in range(len(products)):
        if products[i].id == product_id:
            products.pop(i)
            return "Deleted Sucessfully"
    return "No Product Found"