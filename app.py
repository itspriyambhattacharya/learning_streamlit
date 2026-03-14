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
