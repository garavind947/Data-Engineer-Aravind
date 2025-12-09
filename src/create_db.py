import sqlite3
import os

DB_PATH = os.path.join("data", "xyz_sales.db")

def create_database():
    os.makedirs("data", exist_ok=True)

    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE customers (
            customer_id INTEGER PRIMARY KEY,
            age INTEGER
        );
    """)

    cur.execute("""
        CREATE TABLE orders (
            order_id INTEGER PRIMARY KEY,
            customer_id INTEGER,
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
        );
    """)

    cur.execute("""
        CREATE TABLE order_items (
            order_id INTEGER,
            item_name TEXT,
            quantity INTEGER,
            FOREIGN KEY (order_id) REFERENCES orders(order_id)
        );
    """)

    customers = [
        (1, 21),
        (2, 23),
        (3, 35),
    ]
    cur.executemany("INSERT INTO customers VALUES (?, ?);", customers)

    orders = [
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 3),
    ]
    cur.executemany("INSERT INTO orders VALUES (?, ?);", orders)

    order_items = [
        (1, "x", 4),
        (1, "y", None),
        (1, "z", None),

        (2, "x", 6),
        (2, "y", None),
        (2, "z", None),

        (3, "x", 1),
        (3, "y", 1),
        (3, "z", 1),

        (4, "x", None),
        (4, "y", None),
        (4, "z", 1),

        (5, "x", None),
        (5, "y", None),
        (5, "z", 1),
    ]
    cur.executemany("INSERT INTO order_items VALUES (?, ?, ?);", order_items)

    conn.commit()
    conn.close()
    print("Database created successfully!")

if __name__ == "__main__":
    create_database()
