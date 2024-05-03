"""Module defining Pydantic models for data validation and serialization of API responses for a Dosa restaurant system."""

from pydantic import BaseModel
from typing import List, Optional

class CustomerBase(BaseModel):
    """Base model for customer data, includes fields shared by creation and reading operations."""
    name: str
    phone: str

class CustomerCreate(CustomerBase):
    """Model for creating a new customer, inherits base customer fields."""
    pass

class CustomerResponse(CustomerBase):
    """Model for returning customer data, includes the customer ID."""
    id: int

    class Config:
        from_attributes = True

class ItemBase(BaseModel):
    """Base model for item data, includes fields shared by creation and reading operations."""
    name: str
    price: float

class ItemCreate(ItemBase):
    """Model for creating a new item, inherits base item fields."""
    pass

class ItemResponse(ItemBase):
    """Model for returning item data, includes the item ID."""
    id: int

    class Config:
        from_attributes = True

class OrderItemBase(BaseModel):
    """Base model for order item data, used for linking items and orders."""
    item_id: int
    quantity: int

class OrderItemCreate(OrderItemBase):
    """Model for creating a new order item, inherits base order item fields."""
    pass

class OrderItemResponse(OrderItemBase):
    """Model for returning order item data, includes detailed item information."""
    id: int
    item: ItemResponse  # Ensure that `ItemResponse` is correctly defined or imported

    class Config:
        from_attributes = True

class OrderBase(BaseModel):
    """Base model for order data, includes fields shared by creation and reading operations."""
    customer_id: int
    timestamp: int
    notes: Optional[str] = None

class OrderCreate(OrderBase):
    """Model for creating a new order, includes details about items in the order."""
    items: List[OrderItemCreate] = []

class OrderResponse(OrderBase):
    """Model for returning order data, includes detailed list of order items."""
    id: int
    items: List[OrderItemResponse] = []

    class Config:
        from_attributes = True
