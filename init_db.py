import sqlite3

def init_db():
    """
    Initialize the database and create tables if they do not exist.
    """
    conn = sqlite3.connect('db.sqlite')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            phone TEXT UNIQUE NOT NULL
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            price REAL NOT NULL
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY,
            customer_id INTEGER NOT NULL,
            timestamp INTEGER NOT NULL,
            notes TEXT,
            FOREIGN KEY (customer_id) REFERENCES customers(id)
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS order_items (
            order_id INTEGER NOT NULL,
            item_id INTEGER NOT NULL,
            FOREIGN KEY (order_id) REFERENCES orders(id),
            FOREIGN KEY (item_id) REFERENCES items(id),
            PRIMARY KEY (order_id, item_id)
        );
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()  # Initialize the database by creating necessary tables.
