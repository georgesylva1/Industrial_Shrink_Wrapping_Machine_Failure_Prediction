import streamlit as st
import pandas as pd
import joblib

# Load the saved KNN model
knn_model = joblib.load('knn_model.joblib')

# Create the Streamlit app
st.title("Shrink Wrapper Failure prediction")

# Create input fields for the feature values
input_values = []
for col in knn_model.feature_names_in_:
    input_value = st.number_input(col, step=0.1)
    input_values.append(input_value)

# Create a button to make predictions
if st.button("Make Prediction"):
    new_data = pd.DataFrame([input_values], columns=knn_model.feature_names_in_)
    prediction = knn_model.predict(new_data)[0]
    st.write(f"Predicted failure likelihood: {prediction}")