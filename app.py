import streamlit as st
import pickle
import pandas as pd

# Load trained model
with open("student_model.pkl", "rb") as file:
    model = pickle.load(file)

# Page title
st.title("🎓 Student Performance Prediction System")

st.write("Enter the student details to predict academic performance.")

# Input fields
hours = st.number_input(
    "Hours Studied per Day",
    min_value=0.0,
    max_value=24.0,
    value=4.0
)

attendance = st.number_input(
    "Attendance (%)",
    min_value=0.0,
    max_value=100.0,
    value=75.0
)

previous_score = st.number_input(
    "Previous Exam Score",
    min_value=0.0,
    max_value=100.0,
    value=60.0
)

assignments = st.number_input(
    "Assignment Score",
    min_value=0.0,
    max_value=10.0,
    value=7.0
)

# Predict button
if st.button("Predict Performance"):

    input_data = pd.DataFrame({
        "Hours_Studied": [hours],
        "Attendance": [attendance],
        "Previous_Score": [previous_score],
        "Assignments": [assignments]
    })

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0]

    if prediction == 1:
        st.success("✅ Predicted Performance: GOOD")
        st.write(
            f"Good Performance Probability: {probability[1] * 100:.2f}%"
        )
    else:
        st.warning("⚠️ Predicted Performance: LOW")
        st.write(
            f"Low Performance Probability: {probability[0] * 100:.2f}%"
        )