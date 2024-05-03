"""Module for defining database models for a Dosa restaurant management system."""

from sqlalchemy import Column, ForeignKey, Integer, String, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Customer(Base):
    """Data model for customers, storing customer details such as name and phone number."""
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone = Column(String, unique=True, nullable=False)

class Item(Base):
    """Data model for items, representing menu items in the restaurant with name and price."""
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    orders = relationship("OrderItem", back_populates="item")

class Order(Base):
    """Data model for orders, storing details about customer orders including the customer and items ordered."""
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    timestamp = Column(Integer, nullable=False)
    notes = Column(String, nullable=True)
    customer = relationship("Customer")
    items = relationship("OrderItem", back_populates="order")

class OrderItem(Base):
    """Data model for order items, representing the many-to-many relationship between orders and items with quantity tracking."""
    __tablename__ = 'order_items'
    order_id = Column(Integer, ForeignKey('orders.id'), primary_key=True)
    item_id = Column(Integer, ForeignKey('items.id'), primary_key=True)
    quantity = Column(Integer, default=1)
    order = relationship("Order", back_populates="items")
    item = relationship("Item", back_populates="orders")

def init_db():
    """Initializes the database by creating all tables based on the defined models."""
    engine = create_engine('sqlite:///./db.sqlite', echo=True)
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    init_db()
