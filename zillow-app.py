import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from ml_model import df_updated, county_dict, data
from ml_midwest import df_updated_mw, county_dict_mw, data_mw


st.header("Home Value Estimator")
st.subheader('''
    Directions for the page here:
        ** Join us at: https://project3-groupj.herokuapp.com **
        1. We have a dashboard for our Tableau info
        2. Data preprocessing and predictions for home values in Indiana
        3. Data preprocessing and predictions for home values for the Midwest
    ''')

options = st.selectbox('Please Select',['Tableau Dashboard', 'Preprocessing & Predictions: Indiana', 'Preprocessing & Predictions: Midwest'])
# @st.cache
if options == 'Tableau Dashboard':
    
    # def main():
        html_temp = """ <div class='tableauPlaceholder' id='viz1614995758021' style='position: automatic'><noscript><a href='#'><img alt=' ' height=600 src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;HV&#47;HV_Dashboard_16149955310770&#47;Sheet1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='HV_Dashboard_16149955310770&#47;Sheet1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;HV&#47;HV_Dashboard_16149955310770&#47;Sheet1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1614995758021');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script> """ 
        components.html(html_temp, width= 800, height=550)
    # if __name__ == "__main__":
    #     main()
    

elif options == 'Preprocessing & Predictions: Indiana':
    df = df_updated
    st.write(df.head())
    def user_input_features():
        # county_input = st.sidebar.selectbox("CountyName", county_dict['CountyCode'])
        county_input = st.sidebar.selectbox("CountyName", data)
        dates_input = st.sidebar.text_input("Date - YYYYMM (ex. 201410)")
        zip_input = st.sidebar.text_input("Zip")
        df = {'county_input': county_input, "dates": dates_input, "zip": zip_input}
        features = pd.DataFrame(df)
        return df, [[county_input[-1], dates_input, zip_input]]
    
    st.sidebar.subheader("User Input Parameters")
    df_params, params = user_input_features()

    st.subheader("Home Value Data")
    st.write(df.describe())

    st.subheader("Prediction")
    
    load_zillowml = pickle.load(open('zillow-ml.pkl','rb'))
    load_Xscaler_in = pickle.load(open('Xscaler-in.pkl','rb'))
    load_yscaler_in = pickle.load(open('yscaler-in.pkl','rb'))
    try:
        scaled_X = load_Xscaler_in.transform(params)
        scaled_pred = load_zillowml.predict(scaled_X)
        unscaled_pred = load_yscaler_in.inverse_transform(scaled_pred)
        df_params['predictions'] = unscaled_pred.ravel().tolist()

        st.write(df_params)
    except:
        st.write("Enter Parameters")

    

elif options == 'Preprocessing & Predictions: Midwest':
    df_mw = df_updated_mw
    st.write(df_mw.head())
    def user_input_features():
        # county_input = st.sidebar.selectbox("CountyName", county_dict['CountyCode'])
        county_input = st.sidebar.selectbox("CountyName", data_mw)
        dates_input = st.sidebar.text_input("Date - YYYYMM (ex. 201410)")
        zip_input = st.sidebar.text_input("Zip")
        dfmw = {'county_input': county_input, 'dates': dates_input, 'zip': zip_input}
        features_mw = pd.DataFrame(dfmw)
        return dfmw, [[county_input[-1], dates_input, zip_input]]
    
    st.sidebar.subheader("User Input Parameters")
    df_params_mw, params_mw = user_input_features()

    st.subheader("Home Value Data")
    # st.write(df_updated_mw.info())
    st.write(df_mw.describe())

    st.subheader("Prediction")

    load_mwzillow = pickle.load(open('zillowmw-ml.pkl','rb'))
    load_Xscaler_mw = pickle.load(open('Xscaler-mw.pkl','rb'))
    load_yscaler_mw = pickle.load(open('yscaler-mw.pkl','rb'))
    try:
        scaled_X_mw = load_Xscaler_mw.transform(params_mw)
        scaled_pred_mw = load_mwzillow.predict(scaled_X_mw)
        unscaled_pred_mw = load_yscaler_mw.inverse_transform(scaled_pred_mw)
        df_params_mw['predictions'] = unscaled_pred_mw.ravel().tolist()
        st.write(df_params_mw)
    except:
        st.write("Enter Paramaters")