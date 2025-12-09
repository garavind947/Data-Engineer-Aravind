import os
import pandas as pd
from helpers import get_connection

def run_sql():
    conn = get_connection()

    # Ensure output folder exists
    os.makedirs("output", exist_ok=True)

    query = """
        SELECT 
            c.customer_id AS Customer,
            c.age AS Age,
            oi.item_name AS Item,
            SUM(COALESCE(oi.quantity, 0)) AS Quantity
        FROM customers c
        JOIN orders o ON c.customer_id = o.customer_id
        JOIN order_items oi ON o.order_id = oi.order_id
        WHERE c.age BETWEEN 18 AND 35
        GROUP BY c.customer_id, oi.item_name
        HAVING Quantity > 0
        ORDER BY c.customer_id, oi.item_name;
    """

    df = pd.read_sql_query(query, conn)
    df.to_csv("output/results_sql.csv", sep=";", index=False)

    print("SQL results saved → output/results_sql.csv")

if __name__ == "__main__":
    run_sql()
