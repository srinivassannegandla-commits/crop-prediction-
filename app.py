import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("crop_model.pkl")

st.set_page_config(
    page_title="Crop Recommendation System",
    page_icon="🌱",
    layout="centered"
)

st.title("🌱 Crop Recommendation System")
st.write("Enter soil and weather parameters")

N = st.number_input("Nitrogen (N)", 0, 150, 90)
P = st.number_input("Phosphorus (P)", 0, 150, 40)
K = st.number_input("Potassium (K)", 0, 150, 40)

temperature = st.number_input("Temperature (°C)", 0.0, 50.0, 25.0)
humidity = st.number_input("Humidity (%)", 0.0, 100.0, 80.0)
ph = st.number_input("pH Value", 0.0, 14.0, 6.5)
rainfall = st.number_input("Rainfall (mm)", 0.0, 500.0, 200.0)

if st.button("Predict Crop"):

    features = np.array([
        [N, P, K, temperature,
         humidity, ph, rainfall]
    ])

    prediction = model.predict(features)

    st.success(
        f"Recommended Crop: {prediction[0]}"
    )