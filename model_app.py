import streamlit as st
import joblib
import pandas as pd

st.set_page_config(page_title="House Price Predictor", layout="wide")

st.title("🏡 House Price Predictor")
st.write("Estimate your house price based on its size, number of rooms, and whether it has a garden.")

@st.cache_resource
def load_model():
    model = joblib.load("regression.joblib")
    return model

model = load_model()

with st.form("house_form"):
    col1, col2, col3 = st.columns(3)
    
    with col1:
        size = st.number_input(
            "Size (square meters)", min_value=10, max_value=1000, value=50, step=1,
            help="Enter the total living area"
        )
    with col2:
        nb_rooms = st.number_input(
            "Number of rooms", min_value=1, max_value=20, value=3, step=1,
            help="Include bedrooms, living rooms, etc."
        )
    with col3:
        garden = st.selectbox(
            "Garden", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No",
            help="Does the house have a garden?"
        )
    
    st.markdown("---")
    submitted = st.form_submit_button("🌟 Predict Price")

if submitted:
    input_data = pd.DataFrame({
        'size': [size],
        'nb_rooms': [nb_rooms],
        'garden': [garden]
    })
    prediction = model.predict(input_data)
    st.success(f"Predicted Price: {prediction[0]:,.2f} $")



