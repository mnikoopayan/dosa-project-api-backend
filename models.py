"""Module for defining preliminary database models for a Dosa restaurant management system.
This stage introduces basic relationships between models.
"""

from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()

class Customer(Base):
    """Data model for customers, storing basic customer details."""
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone = Column(String, unique=True, nullable=False)

class Item(Base):
    """Data model for items, representing basic details of menu items."""
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)

class Order(Base):
    """Preliminary data model for orders."""
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    timestamp = Column(Integer, nullable=False)
    
    # Basic relationship to demonstrate linkage to the Customer model
    customer = relationship("Customer", backref=backref("orders", uselist=True))

class OrderItem(Base):
    """Intermediate model to link Orders and Items with basic relationship details."""
    __tablename__ = 'order_items'
    order_id = Column(Integer, ForeignKey('orders.id'), primary_key=True)
    item_id = Column(Integer, ForeignKey('items.id'), primary_key=True)
    quantity = Column(Integer, default=1)
    
    # Basic relationships to connect Order and Item models
    order = relationship("Order", backref=backref("order_items", cascade="all, delete-orphan"))
    item = relationship("Item", backref=backref("order_items"))

def init_db():
    """Creates the database tables based on the above model definitions."""
    engine = create_engine('sqlite:///./db.sqlite', echo=True)
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    init_db()
