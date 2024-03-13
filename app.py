import streamlit as st
import pandas as pd
import numpy as np
from joblib import load

# Load your water quality prediction model
model = load('MyModel.joblib')


st.title('Water Quality Prediction Interface :droplet:')

# pH
pH = st.slider("Choose pH", 0, 14)

# Nitrate
Nitrate = st.text_input("Input Nitrate", '1.0')

# Chloride
Chloride = st.text_input("Input Chloride", '1.0')

# Zinc
Zinc = st.text_input("Input Zinc", '1.0')

# Color
color_options = ['Colorless', 'Faint Yellow', 'Light Yellow', 'Near Colorless']
Color = st.selectbox("Select Color", color_options)

# Turbidity
Turbidity = st.text_input("Input Turbidity", '1.0')

# Fluoride
Fluoride = st.text_input("Input Fluoride", '1.0')

# Copper
Copper = st.text_input("Input Copper", '1.0')

# Odor
Odor = st.text_input("Input Odor", '1.0')

# Sulfate
Sulfate = st.text_input("Input Sulfate", '1.0')

# Conductivity
Conductivity = st.text_input("Input Conductivity", '1.0')

# Chlorine
Chlorine = st.text_input("Input Chlorine", '1.0')

# Make prediction
def predict(): 
    # Create a DataFrame for prediction
    columns = ['pH', 'Nitrate', 'Chloride', 'Zinc', 'Turbidity', 'Fluoride', 'Copper', 'Odor', 'Sulfate', 'Conductivity', 'Chlorine'] 
    #row = np.array([pH, Nitrate, Chloride, Zinc, Turbidity, Fluoride, Copper, Odor, Sulfate, Conductivity, Chlorine]) 
    row = np.array([6.688009,5.356380,166.717667,0.205945,0.004755,1.232307,0.008460,2.125127,84.560102,490.677175,3.416104]) 
    X = pd.DataFrame([row], columns=columns)
    
    # Make prediction
    prediction = model.predict(X)
    
    # Display prediction result
    if prediction[0] == 1: 
        st.success('The water quality is predicted to be good :+1:')
    else: 
        st.error('The water quality is predicted to be poor :-1:') 

trigger = st.button('Predict :crystal_ball:', on_click=predict)
