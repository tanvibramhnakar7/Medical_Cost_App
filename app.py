import streamlit as st
import pandas as pd
import pickle

# Load the saved model
model = pickle.load(open('best_model.pkl', 'rb'))  # Change filename if needed

st.set_page_config(page_title="Medical Cost Prediction App", layout="centered")

st.title("💰 Medical Cost Prediction App")
st.write("This app predicts the medical insurance cost based on user input.")

# Collect user input
age = st.number_input("Age", min_value=0, max_value=100, value=25)
sex = st.selectbox("Sex", ["male", "female"])
bmi = st.number_input("BMI (Body Mass Index)", min_value=10.0, max_value=50.0, value=25.0)
children = st.number_input("Number of Children", min_value=0, max_value=10, value=0)
smoker = st.selectbox("Smoker", ["yes", "no"])
region = st.selectbox("Region", ["southwest", "southeast", "northwest", "northeast"])

# Encode categorical values (based on how your model was trained)
# Make sure this matches your preprocessing
input_data = pd.DataFrame({
    'age': [age],
    'sex': [sex],
    'bmi': [bmi],
    'children': [children],
    'smoker': [smoker],
    'region': [region]
})

# Predict button
if st.button("Predict Medical Cost"):
    try:
        prediction = model.predict(input_data)[0]
        st.success(f"Estimated Medical Cost: 💵 ${prediction:,.2f}")
    except Exception as e:
        st.error(f"Error: {e}")
