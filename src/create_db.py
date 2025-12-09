import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_DIR = BASE_DIR / "data"
DB_PATH = DB_DIR / "xyz_sales.db"


def create_database():
    DB_DIR.mkdir(parents=True, exist_ok=True)

    if DB_PATH.exists():
        DB_PATH.unlink()

    conn = sqlite3.connect(DB_PATH.as_posix())
    cur = conn.cursor()

    cur.execute("""
                CREATE TABLE customers
                (
                    customer_id INTEGER PRIMARY KEY,
                    age         INTEGER
                );
                """)

    cur.execute("""
                CREATE TABLE orders
                (
                    order_id    INTEGER PRIMARY KEY,
                    customer_id INTEGER,
                    FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
                );
                """)

    cur.execute("""
                CREATE TABLE order_items
                (
                    order_id  INTEGER,
                    item_name TEXT,
                    quantity  INTEGER,
                    FOREIGN KEY (order_id) REFERENCES orders (order_id)
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
    print("Database created successfully! Path:", DB_PATH)


if __name__ == "__main__":
    create_database()
