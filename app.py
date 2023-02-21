import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle
import sklearn
pickle_in = open('logreg.pkl', 'rb')
classifier = pickle.load(pickle_in)

st.title("Diabetes Prediction mainly for women")
    
st.write("Developed by: Oduyebo oluwatobi victor")
name = st.text_input("Name:")
pregnancy = st.number_input("No. of times pregnant:")
glucose = st.number_input("Plasma Glucose Concentration :")
bp =  st.number_input("Diastolic blood pressure (mm Hg):")
skin = st.number_input("Triceps skin fold thickness (mm):")
insulin = st.number_input("2-Hour serum insulin (mu U/ml):")
bmi = st.number_input("Body mass index (weight in kg/(height in m)^2):")
dpf = st.number_input("Diabetes Pedigree Function:")
age = st.number_input("Age:")
submit = st.button('Predict')
if submit:
        prediction = classifier.predict([[pregnancy, glucose, bp, skin, insulin, bmi, dpf, age]])
        if prediction == 0:
            st.write('Congratulation',name,'You are not diabetic')
        else:
            st.write(name," we are really sorry to say but it seems like you are Diabetic.")
