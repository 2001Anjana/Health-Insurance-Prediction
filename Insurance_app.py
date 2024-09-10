import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the model
with open('insurance_prediction.pkl', 'rb') as f:
    model = pickle.load(f)

# Set page config
st.set_page_config(page_title='Insurance Cost Predictor', page_icon=':moneybag:', layout='wide')

# Using CSS to inject custom styles
st.markdown("""
<style>
.big-font {
    font-size:30px !important;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# Header Section
st.title('Insurance Cost Prediction', anchor=None)
st.image('ins.jpg', width=800)
#use_column_width=True
st.markdown('This app predicts the medical insurance cost based on user inputs.', unsafe_allow_html=True)

# Sidebar for inputs
with st.sidebar:
    st.header('User Inputs')
    age = st.slider('Age', 18, 70)
    sex = st.selectbox('Sex', options=['Male', 'Female'])
    bmi = st.number_input('BMI', min_value=10.0, max_value=50.0)
    children = st.slider('Number of Children', 0, 5)
    smoker = st.selectbox('Smoker', options=['Yes', 'No'])
    region = st.selectbox('Region', options=['Southeast', 'Southwest', 'Northeast', 'Northwest'])

# Encode inputs
sex = 0 if sex == 'Male' else 1
smoker = 0 if smoker == 'Yes' else 1
region_dict = {'southeast': 0, 'southwest': 1, 'northeast': 2, 'northwest': 3}
region = region_dict[region.lower()]

# Prediction on button click
col1, col2 = st.columns([1, 3])
with col1:
    if st.button('Predict'):
        input_data = np.array([[age, sex, bmi, children, smoker, region]])
        prediction = model.predict(input_data)
        st.success(f'Estimated Insurance Cost: ${float(prediction[0]):.2f}')
