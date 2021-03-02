import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

st.header("Home Value Estimator")
st.subheader('''
    Directions for the page here:
        1. We have a dashboard for our PowerBI info
        2. Data preprocessing and predictions for home values
    ''')

options = st.selectbox('Please Select',['PowerBI Dashboard', 'Preprocessing & Predictions'])