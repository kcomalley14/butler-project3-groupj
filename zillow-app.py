import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

st.header("Home Value Estimator")
st.subheader('''
    Directions for the page here:
        ** Join us at: https://project3-groupj.herokuapp.com **
        1. We have a dashboard for our PowerBI info
        2. Data preprocessing and predictions for home values
    ''')

options = st.selectbox('Please Select',['PowerBI Dashboard', 'Preprocessing & Predictions'])

if options == 'PowerBI Dashboard':
    st.markdown("https://app.powerbi.com/reportEmbed?reportId=098732ca-c993-4eda-a158-ffa14d2d7b55&autoAuth=true&ctid=8dacabf7-f04d-4b21-b6e9-4a866700c6fd&config=eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly93YWJpLXVzLWNlbnRyYWwtYS1wcmltYXJ5LXJlZGlyZWN0LmFuYWx5c2lzLndpbmRvd3MubmV0LyJ9", unsafe_allow_html=True)
    
