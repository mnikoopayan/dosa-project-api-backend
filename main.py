"""Main module for FastAPI application managing a Dosa restaurant.
This stage integrates initial database interactions and basic dependency injection.
"""

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import List

from models import Base, Customer, Item, Order  # Assuming we have these models from your SQLAlchemy ORM setup
from schemas import CustomerBase, ItemBase, OrderBase  # Assuming we have these base schemas for validation

app = FastAPI()

# Setup database connection
engine = create_engine('sqlite:///./db.sqlite', echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

def get_db():
    """Dependency that provides a database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Customer endpoints
@app.get("/customers/", response_model=List[CustomerBase])
def read_customers(db: Session = Depends(get_db)):
    """Retrieve all customers."""
    return db.query(Customer).all()

@app.get("/customers/{customer_id}", response_model=CustomerBase)
def read_customer(customer_id: int, db: Session = Depends(get_db)):
    """Retrieve a customer by ID."""
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

# Item endpoints
@app.get("/items/", response_model=List[ItemBase])
def read_items(db: Session = Depends(get_db)):
    """Retrieve all menu items."""
    return db.query(Item).all()

@app.get("/items/{item_id}", response_model=ItemBase)
def read_item(item_id: int, db: Session = Depends(get_db)):
    """Retrieve an item by ID."""
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

# Order endpoints
@app.get("/orders/", response_model=List[OrderBase])
def read_orders(db: Session = Depends(get_db)):
    """Retrieve all orders."""
    return db.query(Order).all()

@app.get("/orders/{order_id}", response_model=OrderBase)
def read_order(order_id: int, db: Session = Depends(get_db)):
    """Retrieve an order by ID."""
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

