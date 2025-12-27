from fastapi import FastAPI
import joblib
import numpy as np
from pathlib import Path

# create app
app = FastAPI(title="Sales Recommendation API")

#load model

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "model" / "recommender.pkl"
model = joblib.load(MODEL_PATH)

data = model["data"]
similarity = model["similarity"]

@app.get("/")
def health():
    return {"status": "running"}

@app.get("/recommend/{user_id}")
def recommend(user_id: str, top_n: int = 5):
    if user_id not in data.index:
        return {"error": "User not found"}

    idx = data.index.tolist().index(user_id)
    scores = similarity[idx]
    similar_user = np.argsort(scores)[-2]

    recommendations = data.iloc[similar_user]
    top_products = recommendations.sort_values(ascending=False).head(top_n)

    return {"recommendations": top_products.index.tolist()}
