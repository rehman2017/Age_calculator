import streamlit as st
from datetime import datetime

def calculate_age(birthdate_str):
    try:
        birthdate = datetime.strptime(birthdate_str, "%d/%m/%Y")
        current_date = datetime(2025, 1, 1)  # Assuming the current year is 2025
        age = (current_date - birthdate).days // 365

        if birthdate.year > 2025:
            return "Invalid input! Birth year cannot be in the future."

        years_to_100 = 100 - age
        message = f"You are {age} years old. 🎉\n"
        if years_to_100 > 0:
            message += f"You will turn 100 in {years_to_100} years."
        else:
            message += "You have already turned 100 or more!"
        return message
    except ValueError:
        return "Invalid format! Please enter your birthdate in DD/MM/YYYY format."

# Function to set background color to cyan blue
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

st.title("Age Calculator 🕰️")
birthdate_str = st.text_input("Enter your birthdate (DD/MM/YYYY):")
if st.button("Calculate Age"):
    result = calculate_age(birthdate_str)
    st.write(result)

st.markdown("---")
st.markdown("<h3 style='color: red; text-align: center;'>Made by Engr Sir Abdul Rehman Ansari</h3>", unsafe_allow_html=True)