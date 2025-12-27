import joblib
import numpy as np

model = joblib.load("../model/recommender.pkl")

similarity = model["similarity"]

print("Similarity matrix shape:", similarity.shape)
print("Sample similarity score:", similarity[0][1])



# Offline metrics are limited

# Real evaluation happens via A/B testing