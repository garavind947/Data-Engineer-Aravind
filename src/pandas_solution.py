import pandas as pd
from helpers import get_connection

def run_pandas():
    conn = get_connection()

    customers = pd.read_sql("SELECT * FROM customers", conn)
    orders = pd.read_sql("SELECT * FROM orders", conn)
    order_items = pd.read_sql("SELECT * FROM order_items", conn)

    df = orders.merge(customers, on="customer_id") \
               .merge(order_items, on="order_id")

    df = df[(df["age"] >= 18) & (df["age"] <= 35)]
    df["quantity"] = df["quantity"].fillna(0)

    grouped = (
        df.groupby(["customer_id", "age", "item_name"])["quantity"]
          .sum()
          .reset_index()
    )

    grouped = grouped[grouped["quantity"] > 0]

    grouped.columns = ["Customer", "Age", "Item", "Quantity"]
    grouped.to_csv("output/results_pandas.csv", sep=";", index=False)

    print("Pandas results saved → output/results_pandas.csv")

if __name__ == "__main__":
    run_pandas()
