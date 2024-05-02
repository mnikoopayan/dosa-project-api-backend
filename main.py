"""Main module for FastAPI application managing a Dosa restaurant.
This stage introduces basic endpoints for customers, items, and orders.
"""

from fastapi import FastAPI, HTTPException
from typing import List

app = FastAPI()

# Mock data to simulate database interaction
customers = [{"id": 1, "name": "John Doe", "phone": "123-456-7890"}]
items = [{"id": 1, "name": "Masala Dosa", "price": 5.99}]
orders = [{"id": 1, "customer_id": 1, "items": [{"item_id": 1, "quantity": 2}]}]

# Root endpoint
@app.get("/")
def read_root():
    return {"Hello": "World"}

# Customer endpoints
@app.get("/customers/", response_model=List[dict])
def read_customers():
    """Retrieve all customers."""
    return customers

@app.get("/customers/{customer_id}")
def read_customer(customer_id: int):
    """Retrieve a customer by ID."""
    customer = next((cust for cust in customers if cust["id"] == customer_id), None)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

# Item endpoints
@app.get("/items/", response_model=List[dict])
def read_items():
    """Retrieve all menu items."""
    return items

@app.get("/items/{item_id}")
def read_item(item_id: int):
    """Retrieve an item by ID."""
    item = next((itm for itm in items if itm["id"] == item_id), None)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

# Order endpoints
@app.get("/orders/", response_model=List[dict])
def read_orders():
    """Retrieve all orders."""
    return orders

@app.get("/orders/{order_id}")
def read_order(order_id: int):
    """Retrieve an order by ID."""
    order = next((ord for ord in orders if ord["id"] == order_id), None)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

