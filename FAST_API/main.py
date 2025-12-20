from fastapi import FastAPI, HTTPException
from model import product

app = FastAPI()

@app.get("/")
def greet():
    return {"message": "hello world"}

products = [
    product(id=1, name="laptop", description="simple laptop", price=699.99, quantity=100),
    product(id=2, name="phone", description="simple phone", price=199.99, quantity=100),
    product(id=3, name="ps5", description="simple ps5", price=499.99, quantity=100),
    product(id=4, name="headphones", description="simple headphones", price=99.99, quantity=100),
    product(id=5, name="charger", description="simple charger", price=29.99, quantity=100),
]

@app.get("/products")
def get_all_products():
    return products

@app.get("/product/{id}")
def get_product_by_id(id: int):
    for p in products:
        if p.id == id:
            return p
    raise HTTPException(status_code=404, detail="Product not found")

@app.post("/product")
def add_product(new_product: product):
    if any(p.id == new_product.id for p in products):
        raise HTTPException(status_code=400, detail="Product ID already exists")
    products.append(new_product)
    return new_product

@app.put("/product/{id}")
def update_product(id: int, updated_product: product):
    if id != updated_product.id:
        raise HTTPException(status_code=400, detail="Path ID and body ID must match")

    for i in range(len(products)):
        if products[i].id == id:
            products[i] = updated_product
            return updated_product

    raise HTTPException(status_code=404, detail="Product not found")
@app.delete("/product/{id}")
def delete_product(id:int):
    for i in range (len(products)):
        if products[i].id==id:
            del products[i]
            return "product deleted"
    return "mot found"    
    