"""Module defining enhanced Pydantic models for data validation and serialization for a Dosa restaurant system.
This stage refines relationships and introduces optional fields for more complex data handling.
"""

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
    """Response model for returning customer data, includes the customer ID."""
    id: int

class ItemBase(BaseModel):
    """Base model for item data, includes fields shared by creation and reading operations."""
    name: str
    price: float
    description: Optional[str] = None  # Optional field for item description

class ItemCreate(ItemBase):
    """Model for creating a new item, inherits base item fields."""
    pass

class ItemResponse(ItemBase):
    """Response model for returning item data, includes the item ID and optional description."""
    id: int
    description: Optional[str] = None

class OrderItemBase(BaseModel):
    """Base model for order item data, used for linking items and orders."""
    item_id: int
    quantity: int

class OrderItemCreate(OrderItemBase):
    """Model for creating a new order item, inherits base order item fields."""
    pass

class OrderItemResponse(OrderItemBase):
    """Intermediate response model for order items, includes an optional link to the detailed item response."""
    id: int
    item: Optional[ItemResponse] = None

class OrderBase(BaseModel):
    """Base model for order data, includes fields shared by creation and reading operations."""
    customer_id: int
    timestamp: int
    notes: Optional[str] = None  # Optional field for additional notes on the order

class OrderCreate(OrderBase):
    """Model for creating a new order, includes details about items in the order and optional notes."""
    items: List[OrderItemCreate] = []

class OrderResponse(OrderBase):
    """Response model for returning order data, includes a detailed list of order items and optional notes."""
    id: int
    items: List[OrderItemResponse] = []
    notes: Optional[str] = None

