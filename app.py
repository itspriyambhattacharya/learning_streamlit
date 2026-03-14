import streamlit as st
import datetime

# Chapter 1 starts
st.title("Hello World")
st.subheader("This is sub-heading")
st.text("This is writte using text command")
st.write("This is written using write command")


cls = st.selectbox(
    "Class",
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
)

st.write(f"You're in class {cls}")

st.success("Passed")
st.error("Repeating")

# chapter 1 ends

# chapter 2 starts

if st.button("Clicked"):
    st.success(f"Button Clicked")


radio_btn = st.radio(
    "Class",
    [1, 2, 3, 4]
)

st.write(f"Class: {radio_btn}")

st.write("Vehicle owned")
car = st.checkbox(
    "Car"
)
bike = st.checkbox(
    "Bike"
)

if car:
    st.success("Owns Car")
    st.error("No Bike")

if bike:
    st.success("No Bike")
    st.error("Owns Car")

age = st.slider(
    "Age",
    min_value=6,
    max_value=50,
    value=20,
    step=2
)
st.write(f"The age is: {age}")

marks = st.number_input(
    "Marks"
)
st.write(f"Makrs obtained: {marks}")

name = st.text_input("Enter your name:")
if name:
    st.success(f"Welcome: {name}")

dob = st.date_input(
    "Date of Birth"
)

if dob:
    st.success(f"DOB: {dob}")

today = st.date_input("Totay's Date", disabled=True)
dob2 = st.date_input(
    " Your Date of Birth for prediction",
    min_value=datetime.date(1996, 5, 7),
    max_value=datetime.date.today()
)

st.write(f"Today's date: {datetime.date.today()}")
st.write(f"Today's year: {datetime.date.today().year}")

if st.button("Predict age"):
    yr = datetime.date.today().year - dob2.year
    st.success(f"Age is  {yr}")

# chapter 2 ends

# chapter 3 starts
