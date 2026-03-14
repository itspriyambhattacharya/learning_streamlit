import streamlit as st
import pandas as pd

st.title("File Uploader")

file = st.file_uploader(
    "Upload a csv file",
    type=['csv']
)
