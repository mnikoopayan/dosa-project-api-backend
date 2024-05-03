"""Main module for FastAPI application managing a Dosa restaurant.
Provides endpoints for CRUD operations on customers, items, and orders.
"""

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Customer, Item, Order
from schemas import CustomerCreate, CustomerResponse, ItemCreate, ItemResponse, OrderCreate, OrderResponse

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

@app.get("/")
def read_root():
    return {"Hello": "World from Dosa API"}

# Customer endpoints
@app.post("/customers/", response_model=CustomerResponse)
def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    """Create a new customer entry in the database."""
    db_customer = Customer(name=customer.name, phone=customer.phone)
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

@app.get("/customers/{customer_id}", response_model=CustomerResponse)
def read_customer(customer_id: int, db: Session = Depends(get_db)):
    """Retrieve a customer by ID."""
    db_customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return db_customer

@app.delete("/customers/{customer_id}", status_code=204)
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    """Delete a customer by ID."""
    db_customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    db.delete(db_customer)
    db.commit()

@app.put("/customers/{customer_id}", response_model=CustomerResponse)
def update_customer(customer_id: int, customer: CustomerCreate, db: Session = Depends(get_db)):
    """Update a customer's information."""
    db_customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if not db_customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    db_customer.name = customer.name
    db_customer.phone = customer.phone
    db.commit()
    return db_customer

# Item endpoints
@app.post("/items/", response_model=ItemResponse)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    """Create a new item entry in the database."""
    db_item = Item(name=item.name, price=item.price)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.get("/items/{item_id}", response_model=ItemResponse)
def read_item(item_id: int, db: Session = Depends(get_db)):
    """Retrieve an item by ID."""
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    """Delete an item by ID."""
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()

@app.put("/items/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, item: ItemCreate, db: Session = Depends(get_db)):
    """Update an item's details."""
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    db_item.name = item.name
    db_item.price = item.price
    db.commit()
    return db_item

# Order endpoints
@app.post("/orders/", response_model=OrderResponse)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    """Create a new order in the database."""
    db_order = Order(customer_id=order.customer_id, timestamp=order.timestamp, notes=order.notes)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

@app.get("/orders/{order_id}", response_model=OrderResponse)
def read_order(order_id: int, db: Session = Depends(get_db)):
    """Retrieve an order by ID."""
    db_order = db.query(Order).filter(Order.id == order_id).first()
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order

@app.delete("/orders/{order_id}", status_code=204)
def delete_order(order_id: int, db: Session = Depends(get_db)):
    """Delete an order by ID."""
    db_order = db.query(Order).filter(Order.id == order_id).first()
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    db.delete(db_order)
    db.commit()

@app.put("/orders/{order_id}", response_model=OrderResponse)
def update_order(order_id: int, order: OrderCreate, db: Session = Depends(get_db)):
    """Update an order's details."""
    db_order = db.query(Order).filter(Order.id == order_id).first()
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    db_order.customer_id = order.customer_id
    db_order.timestamp = order.timestamp
    db_order.notes = order.notes
    db.commit()
    return db_order
