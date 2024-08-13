import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from backend import get_data

# Add UI stuff
st.title('Weather Forecast of Next Days')
place = st.text_input("Place : ")
days = st.slider("Forecast Days", min_value = 1, max_value=5 
                 ,help = "Select the number of forcecasted days")

option = st.selectbox("Select data to view"
                      , ("Temperature", "Sky"))
st.subheader(f"{option} for next {days} days in {place}")

# get temperature/ sky data
if place :
    try : 
        filtered_data = get_data(place,days)
        
        if option =='Temperature':
            temperatures = [dict['main']['temp'] /10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
                
            figure = px.line(x=dates,y = temperatures , labels = {"x" : "Date" , "y":"Temperatures (C)"} )
            st.plotly_chart(figure)

        if option =='Sky':
            sky_conditions = [dict['weather'][0]['main'] for dict in filtered_data]
            images = {"Clear": 'images/clear.png',
                    'Clouds':'images/cloud.png',
                    'Rain' :'images/rain.png',
                    'Snow':'images/snow.png'
                    }
            
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths,width= 115)
    except KeyError:
        st.warning(f"{place} doesn't exist in our database..try with some other city name")