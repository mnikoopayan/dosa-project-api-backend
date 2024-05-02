import sqlite3

def init_db():
    """
    Initialize the database and create tables with relational integrity.
    """
    # Establish a connection to the SQLite database. If it doesn't exist, it will be created.
    conn = sqlite3.connect('db.sqlite')
    cursor = conn.cursor()

    # Create a table for customers
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT UNIQUE NOT NULL
    );
    ''')

    # Create a table for items (menu items in the restaurant)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        description TEXT
    );
    ''')

    # Create a table for orders
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER NOT NULL,
        timestamp INTEGER NOT NULL,
        notes TEXT,
        FOREIGN KEY (customer_id) REFERENCES customers(id)
    );
    ''')

    # Create a table for order_items to handle the many-to-many relationship between orders and items
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS order_items (
        order_id INTEGER NOT NULL,
        item_id INTEGER NOT NULL,
        quantity INTEGER DEFAULT 1,
        PRIMARY KEY (order_id, item_id),
        FOREIGN KEY (order_id) REFERENCES orders(id),
        FOREIGN KEY (item_id) REFERENCES items(id)
    );
    ''')

    # Commit the changes to the database and close the connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()  # Initialize the database by creating necessary tables.
