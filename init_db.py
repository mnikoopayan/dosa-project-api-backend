import sqlite3

def init_db():
    """
    Further refine the database structure, enhancing data integrity and detail in preparation for final functionalities.
    """
    conn = sqlite3.connect('db.sqlite')
    cursor = conn.cursor()

    # Enhance the customers table with additional data integrity constraints
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE  -- Adding an email field for future contact management
    );
    ''')

    # Enhance the items table by adding a category field
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL CHECK (price >= 0),  -- Ensure no negative prices
        description TEXT,
        category TEXT DEFAULT 'General'  -- New field to categorize menu items
    );
    ''')

    # Add a status field to orders to track order progress
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER NOT NULL,
        timestamp INTEGER NOT NULL DEFAULT (strftime('%s', 'now')),
        status TEXT NOT NULL DEFAULT 'Pending',  -- New field to track the status of the order
        notes TEXT,
        FOREIGN KEY (customer_id) REFERENCES customers(id)
    );
    ''')

    # Include a unit price in order_items to preserve the price at the time of the order
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS order_items (
        order_id INTEGER NOT NULL,
        item_id INTEGER NOT NULL,
        quantity INTEGER DEFAULT 1,
        unit_price REAL,  -- Capture price at the time of the order
        PRIMARY KEY (order_id, item_id),
        FOREIGN KEY (order_id) REFERENCES orders(id),
        FOREIGN KEY (item_id) REFERENCES items(id)
    );
    ''')

    # Commit the changes to the database and close the connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()  # Initialize the database by enhancing the tables.
