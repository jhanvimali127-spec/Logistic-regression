
import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load('diabetes_model.pkl')

st.title("Diabetes Prediction System")

st.write("Enter the following details:")

Pregnancies = st.number_input("Pregnancies", 0, 20)
Glucose = st.number_input("Glucose", 0, 250)
BloodPressure = st.number_input("Blood Pressure", 0, 150)
SkinThickness = st.number_input("Skin Thickness", 0, 100)
Insulin = st.number_input("Insulin", 0, 900)
BMI = st.number_input("BMI", 0.0, 70.0)
DiabetesPedigreeFunction = st.number_input(
    "Diabetes Pedigree Function", 0.0, 3.0
)
Age = st.number_input("Age", 1, 100)

if st.button("Predict"):

    new_data = pd.DataFrame([{
        'Pregnancies': Pregnancies,
        'Glucose': Glucose,
        'BloodPressure': BloodPressure,
        'SkinThickness': SkinThickness,
        'Insulin': Insulin,
        'BMI': BMI,
        'DiabetesPedigreeFunction': DiabetesPedigreeFunction,
        'Age': Age
    }])

    prediction = model.predict(new_data)

    if prediction[0] == 1:
        st.error("Diabetes predicted")
    else:
        st.success("No diabetes predicted")
