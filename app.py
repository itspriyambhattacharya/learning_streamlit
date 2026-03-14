import streamlit as st

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
    value=21
)
st.write(f"The age is: {age}")
