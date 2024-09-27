import streamlit as st
from datetime import datetime
import pandas as pd


def app():
    year = st.number_input("Enter Year:", min_value=2024, max_value=2100, step=1)
    month = st.number_input("Enter Month (1-12):", min_value=1, max_value=12, step=1)
    day = st.number_input("Enter Day (1-31):", min_value=1, max_value=31, step=1)


    if st.button("Predict Weather"):
        input_date = datetime(year, month, day)
        st.write(f"Selected Date: {input_date}")
    
    


