"""Module for defining intermediate Pydantic models for data validation and serialization of API responses for a Dosa restaurant system.
This stage introduces models that begin to define relationships between entities.
"""

from pydantic import BaseModel
from typing import Optional

class CustomerBase(BaseModel):
    """Base model for customer data."""
    name: str
    phone: str

class CustomerCreate(CustomerBase):
    """Model for creating a new customer, inherits base customer fields."""
    pass

class CustomerResponse(CustomerBase):
    """Response model for returning customer data, includes the customer ID."""
    id: int

class ItemBase(BaseModel):
    """Base model for item data."""
    name: str
    price: float

class ItemCreate(ItemBase):
    """Model for creating a new item, inherits base item fields."""
    pass

class ItemResponse(ItemBase):
    """Response model for returning item data, includes the item ID."""
    id: int

class OrderItemBase(BaseModel):
    """Base model for order item data, used for linking items and orders."""
    item_id: int
    quantity: int

class OrderItemCreate(OrderItemBase):
    """Model for creating a new order item, includes base order item fields."""
    pass

class OrderItemResponse(OrderItemBase):
    """Intermediate response model for order items."""
    id: int
    item: Optional[ItemResponse] = None  # Optional detailed item response

class OrderBase(BaseModel):
    """Base model for order data, includes fields shared by creation and reading operations."""
    customer_id: int
    timestamp: int

class OrderCreate(OrderBase):
    """Model for creating a new order, starts to include items."""
    items: Optional[list[OrderItemCreate]] = []

class OrderResponse(OrderBase):
    """Response model for returning order data, includes list of order items."""
    id: int
    items: Optional[list[OrderItemResponse]] = []

