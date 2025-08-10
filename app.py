# app.py
import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("nfl_real_model.pkl")

st.title("🏈 NFL Home Score Predictor")

st.markdown("Predict the home team's final score based on Vegas odds.")

spread = st.number_input("Vegas Spread (favorite):", value=-6.5)
ou = st.number_input("Over/Under Line:", value=45.5)
fav_is_home = st.selectbox("Is the favorite the home team?", ['Yes', 'No'])

fav_is_home = 1 if fav_is_home == 'Yes' else 0

if st.button("Predict Score"):
    input_df = pd.DataFrame([{
        'spread_favorite': spread,
        'over_under_line': ou,
        'fav_is_home': fav_is_home
    }])

    score = model.predict(input_df)[0]
    st.success(f"🏆 Predicted Final Home Team Score: {score:.1f}")
