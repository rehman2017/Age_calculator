import datetime
import streamlit as st

def calculate_age(birthdate):
    current_date = datetime.date.today()
    
    # Ensure birthdate is a date object
    if isinstance(birthdate, str):
        try:
            birthdate = datetime.datetime.strptime(birthdate, "%Y-%m-%d").date()
        except ValueError:
            return "Invalid date format. Please use YYYY-MM-DD."
    
    if birthdate > current_date:
        return "Error: Birthdate cannot be in the future."
    
    age = current_date.year - birthdate.year - ((current_date.month, current_date.day) < (birthdate.month, birthdate.day))
    
    return f"Your age is {age} years."

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

# Streamlit UI
# Set background color
set_background()

st.title("🎂 Age Calculator")

birthdate = st.date_input("Select your birthdate:")
if st.button("Calculate Age"):
    result = calculate_age(birthdate)
    st.success(result)

st.markdown("---")
st.markdown("<h3 style='color: red; text-align: center;'>Made by Engr Sir Abdul Rehman Ansari</h3>", unsafe_allow_html=True)
