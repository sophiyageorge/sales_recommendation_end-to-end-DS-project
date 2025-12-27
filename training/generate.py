import pandas as pd
import random

users = [f"user_{i}" for i in range(1, 101)]
products = [f"product_{i}" for i in range(1, 21)]

data = []

for _ in range(1000):
    data.append({
        "user_id": random.choice(users),
        "product_id": random.choice(products),
        "quantity": random.randint(1, 5)
    })

df = pd.DataFrame(data)
df.to_csv("../data/sales_data.csv", index=False)
