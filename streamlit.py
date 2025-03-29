import streamlit as st
from datetime import datetime
from dateutil.relativedelta import relativedelta

def calculate_age(birthdate):
    current_date = datetime.today()
    
    if birthdate > current_date:
        return "Invalid input! Birthdate cannot be in the future."
    
    age = relativedelta(current_date, birthdate).years
    years_to_100 = 100 - age
    
    message = f"You are {age} years old. 🎉\n"
    if years_to_100 > 0:
        message += f"You will turn 100 in {years_to_100} years."
    else:
        message += "You have already turned 100 or more!"
    
    return message

def set_background():
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #00bcd4; /* Cyan Blue */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Set background color
set_background()

st.title("🎂 Age Calculator")

birthdate = st.date_input("Select your birthdate:")
if st.button("Calculate Age"):
    result = calculate_age(birthdate)
    st.success(result)

st.markdown("---")
st.markdown("<h3 style='color: red; text-align: center;'>Made by Engr Sir Abdul Rehman Ansari</h3>", unsafe_allow_html=True)
