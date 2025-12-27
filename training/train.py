import pandas as pd
import joblib
from sklearn.metrics.pairwise import cosine_similarity

data = pd.read_csv("../data/user_product_matrix.csv", index_col=0)

similarity = cosine_similarity(data)

model = {
    "similarity": similarity,
    "data": data
}

joblib.dump(model, "../model/recommender.pkl")
