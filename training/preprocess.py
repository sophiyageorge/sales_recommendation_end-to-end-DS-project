import pandas as pd

df = pd.read_csv("../data/sales_data.csv")

pivot = df.pivot_table(
    index="user_id",
    columns="product_id",
    values="quantity",
    aggfunc="sum",
    fill_value=0
)

pivot.to_csv("../data/user_product_matrix.csv")
