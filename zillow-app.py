import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from ml_model import df_updated, county_dict
from ml_midwest import df_updated_mw, county_dict_mw


st.header("Home Value Estimator")
st.subheader('''
    Directions for the page here:
        ** Join us at: https://project3-groupj.herokuapp.com **
        1. We have a dashboard for our PowerBI info
        2. Data preprocessing and predictions for home values in Indiana
        3. Data preprocessing and predictions for home values for the Midwest
    ''')

options = st.selectbox('Please Select',['PowerBI Dashboard', 'Preprocessing & Predictions: Indiana', 'Preprocessing & Prediction: Midwest'])

if options == 'PowerBI Dashboard':
    st.markdown("""
        <iframe width="600" height="606" src="https://public.tableau.com/views/CitiBike_Data/Story1?:language=en&:display_count=y&:origin=viz_share_link" frameborder="0" style="border:0" allowfullscreen></iframe>
        """, unsafe_allow_html=True)
    
    # st.markdown("""
    #     <iframe width="600" height="606" src="https://app.powerbi.com/reportEmbed?reportId=098732ca-c993-4eda-a158-ffa14d2d7b55&autoAuth=true&ctid=8dacabf7-f04d-4b21-b6e9-4a866700c6fd&config=eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly93YWJpLXVzLWNlbnRyYWwtYS1wcmltYXJ5LXJlZGlyZWN0LmFuYWx5c2lzLndpbmRvd3MubmV0LyJ9" frameborder="0" style="border:0" allowfullscreen></iframe>
    #     """, unsafe_allow_html=True)

elif options == 'Preprocessing & Predictions: Indiana':
    df = df_updated
    st.write(df.head())
    def user_input_features():
        # county_input = st.sidebar.selectbox("CountyName", county_dict['CountyCode'])
        county_input = st.sidebar.selectbox("CountyName", [county_dict["CountyCode"]])

    st.sidebar.subheader("User Input Parameters")
    df_params = user_input_features()

    st.write(df_updated.info())
    st.write(df.describe())

    st.subheader("User Input Parameters")
    st.write(df_params)

else:
    df_mw = df_updated_mw
    st.write(df_mw.head())
    def user_input_features():
        # county_input = st.sidebar.selectbox("CountyName", county_dict['CountyCode'])
        county_input = st.sidebar.selectbox("CountyName", [county_dict_mw])

    st.sidebar.subheader("User Input Parameters")
    df_params = user_input_features()

    st.write(df_updated_mw.info())
    st.write(df_mw.describe())

    st.subheader("User Input Parameters")
    st.write(df_params)