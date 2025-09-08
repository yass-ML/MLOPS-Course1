import streamlit as st
import joblib
import pandas as pd

def load_model():
    model = joblib.load("regression.joblib")
    return model

model = load_model()
with st.form("house_form"):
    st.number_input("Size (in square meters)", min_value=10, max_value=1000, value=50, step=1, key="size")
    st.number_input("Number of rooms", min_value=1, max_value=20, value=3, step=1, key="nb_rooms")
    st.selectbox("Garden", options=[0, 1], index=0, key="garden")

    submitted = st.form_submit_button("Predict Price")

if submitted:
    input_data = pd.DataFrame({
        'size': [st.session_state.size],
        'nb_rooms': [st.session_state.nb_rooms],
        'garden': [st.session_state.garden]
    })
    prediction = model.predict(input_data)
    st.write(f"Predicted Price: {prediction[0]:.2f} $")


