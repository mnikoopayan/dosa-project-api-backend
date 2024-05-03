# Dosa Restaurant API Backend

## Overview
This project is a FastAPI backend designed to manage a Dosa restaurant's operations. It supports complete CRUD operations on customers, items, and orders, implemented in Python using SQLAlchemy and SQLite. The API is designed to support restaurant operations by providing a robust digital ordering system.

## Technologies Used
- **FastAPI**: A modern, fast web framework for building APIs with Python 3.7+ based on standard Python type hints.
- **SQLAlchemy**: SQL toolkit and Object-Relational Mapping (ORM) for Python.
- **SQLite**: A lightweight disk-based database that doesn't require a separate server process.
- **Uvicorn**: A lightning-fast ASGI server implementation, using uvloop and httptools.

## Project Structure
- `/database`: Contains the database initialization script (`init_db.py`) for creating tables using SQLAlchemy ORM.
- `/app`: Contains the main FastAPI application (`main.py`) responsible for handling HTTP requests and responses.
  - `/models`: Contains SQLAlchemy ORM models (`models.py`) defining database tables.
  - `/schemas`: Contains Pydantic models (`schemas.py`) for request validation and response objects.
- `/utils`: Contains utility functions and configurations.

## Getting Started
To get a local copy up and running follow these simple steps.

### Prerequisites
- **Python 3.7+**: Ensure you have Python 3.7 or higher installed.
- **pip**: Make sure Python's package installer is available.

### Installation
1. **Clone the repo**: `git clone https://github.com/mnikoopayan/dosa-project-api-backend.git`
2. **Set up a virtual environment** (optional but recommended):
python -m venv venv
source venv/bin/activate # On Windows use venv\Scripts\activate
3. **Install the requirements**:
pip install -r requirements.txt
4. **Run the application**:
uvicorn main:app --reload
This command starts the server on `http://127.0.0.1:8000` where you can access the API.

## Features
- **Order Management**: Create, read, update, and delete orders.
- **Customer Management**: Maintain a database of customers with unique phone numbers.
- **Menu Management**: Manage a dynamic list of menu items, including prices and descriptions.

## How to Use
- **Add a Customer**: `POST /customers/`
- **Get Customer Info**: `GET /customers/{customer_id}`
- **Update Customer Info**: `PUT /customers/{customer_id}`
- **Delete a Customer**: `DELETE /customers/{customer_id}`
- **Add an Item to the Menu**: `POST /items/`
- **Get Item Info**: `GET /items/{item_id}`
- **Update Item Info**: `PUT /items/{item_id}`
- **Delete an Item**: `DELETE /items/{item_id}`
- **Place an Order**: `POST /orders/`
- **Get Order Details**: `GET /orders/{order_id}`
- **Update an Order**: `PUT /orders/{order_id}`
- **Cancel an Order**: `DELETE /orders/{order_id}`

Feel free to explore and test other endpoints as described in the API documentation available at `http://127.0.0.1:8000/docs` once your server is running.


