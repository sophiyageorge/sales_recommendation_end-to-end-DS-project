import streamlit as st
import requests

st.title("🛒 Sales Recommendation System")

user_id = st.text_input("Enter User ID (e.g. user_1)")

if st.button("Get Recommendations"):
    response = requests.get(f"http://localhost:8000/recommend/{user_id}")
    if response.status_code == 200:
        st.write(response.json())
    else:
        st.error("User not found")
