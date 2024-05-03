"""Intermediate module for defining database models for a Dosa restaurant management system.
This stage introduces more complex relationships and additional fields for existing models.
"""

from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()

class Customer(Base):
    """Data model for customers, expanding to include optional address details."""
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone = Column(String, unique=True, nullable=False)
    address = Column(String)  # New field for customer address

class Item(Base):
    """Data model for items, now including a description and category for menu items."""
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    description = Column(String)  # New field for item description
    category = Column(String)  # New field to categorize items

class Order(Base):
    """Enhanced data model for orders, including timestamps and optional notes."""
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    timestamp = Column(DateTime)  # Changed from Integer to DateTime for more accurate time tracking
    notes = Column(String)  # Optional field for additional order notes
    customer = relationship("Customer", backref="orders")

class OrderItem(Base):
    """Refined model for order items, including quantity and additional item details."""
    __tablename__ = 'order_items'
    order_id = Column(Integer, ForeignKey('orders.id'), primary_key=True)
    item_id = Column(Integer, ForeignKey('items.id'), primary_key=True)
    quantity = Column(Integer, default=1)
    order = relationship("Order", backref=backref("order_items", cascade="all, delete-orphan"))
    item = relationship("Item", backref=backref("order_items"))

def init_db():
    """Enhances the database initialization to reflect the updated model definitions."""
    engine = create_engine('sqlite:///./db.sqlite', echo=True)
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    init_db()
