import streamlit as st

# titel
st.title("BMI calculator")

# tekst
st.write("Welkom! Hier gaan we je BMI berekenen.")

# sliders
w = st.slider("Kies je gewicht in kg", 30, 200)
h = st.slider("Kies je lengte in meter", 1.40, 2.20)

# BMI berekening
bmi = w / (h ** 2)

# output
st.write(f"Je BMI is: **{bmi:.2f}**")
