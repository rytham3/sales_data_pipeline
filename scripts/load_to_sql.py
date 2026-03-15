import pandas as pd
import sqlite3

df = pd.read_csv("../data/clean_sales_data.csv")

conn = sqlite3.connect("sales.db")

df.to_sql("sales", conn, if_exists="replace", index=False)

print("Data loaded into SQL database")

query = "SELECT category, SUM(total_value) as revenue FROM sales GROUP BY category"

result = pd.read_sql(query, conn)

print(result)

conn.close()
