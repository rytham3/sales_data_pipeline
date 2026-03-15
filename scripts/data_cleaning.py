import pandas as pd

# load dataset
df = pd.read_csv("../data/sales_data.csv")

# basic cleaning
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

# create new column
df["total_value"] = df["sales"] * df["quantity"]

print("Cleaned Data:")
print(df.head())

# save cleaned data
df.to_csv("../data/clean_sales_data.csv", index=False)
