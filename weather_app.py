import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title('Weather Forecast of Next Days')
place = st.text_input("Place : ")
days = st.slider("Forecast Days", min_value = 1, max_value=5 
                 ,help = "Select the number of forcecasted days")

option = st.selectbox("Select data to view"
                      , ("Temperature", "Sky"))

def get_data(days):    
    dates =['2021-25-10', '2022-25-10','2023-25-10','2024-25-10']
    temperatures =[10,11,14,10] 
    temperatures = [days * i for  i in temperatures]
    return dates, temperatures
d,t = get_data(days)


st.subheader(f"{option} for next {days} days in {place}")
figure = px.line(x=d,y = t , labels = {"x" : "Date" , "y":"Temperatures (C)"} )
st.plotly_chart(figure)