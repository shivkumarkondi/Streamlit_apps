import streamlit as st
import pandas as pd
import numpy as np

st.title('Weather Forecast of Next Days')
place = st.text_input("Place : ")
days = st.slider("Forecast Days", min_value = 1, max_value=5 
                 ,help = "Select the number of forcecasted days")

option = st.selectbox("Select data to view"
                      , ("Temperature", "Sky"))

st.subheader(f"{option} for next {days} days in {place}")