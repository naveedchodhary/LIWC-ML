
import streamlit as st
import numpy as np
import joblib

# Load trained model
rf_model = joblib.load("random_forest_LIWC_model.pkl")

st.title("Sentiment Prediction Using LIWC & Random Forest")

# Create input sliders for sample features
