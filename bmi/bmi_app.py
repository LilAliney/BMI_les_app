import streamlit as st
import math

# title
st.title("Het BMI calculator")
# tekst
st.write("Welkom! Hier gaan we je BMI berekenen.")
# slider
w = st.slider("Kies je gewigt in kg.", 0,100)
h = st.slider("Kies je lengte in m."0,100)
# variabelen
bmi = (w/(h**2))/10
# output
st.write(f"Je BMI werd als {bmi} berekend")