import streamlit as st
import pandas as pd
import plotly.express as px 
import numpy as np

# config
st.set_page_config(
    layout="wide",
    page_title="Immigration Analysis App",
    page_icon="⚪"
)

years = list(range(1980,2014))
cols_to_drop = ['Type', 'Coverage', 'AREA','DEV','REG']
rename_dict = {'OdName':'Country','AreaName':'Continent',
                'RegName':'Region','DevName':'Status'}

@st.cache_data()
def load_data(path):
    df = pd.read_excel('Canada.xlsx', sheet_name=1, skiprows=20, skipfooter=2)
    df.drop(columns=cols_to_drop, inplace=True)
    df.rename(columns=rename_dict, inplace=True)
    df['Total'] = df[years].sum(axis=1)
    df.set_index('Country', inplace=True)
    return df

with st.spinner('processing imagination data ....'):
    df = load_data('canada.xlsx')
    
# st.image(" ",
        #  use_column_width=True)

st.title("immigration Analysis App")  

c1, c2, c3, c4, c5, c6 = st.columns(6)

total_countries = df.shape[0]
duration = "1980 - 2013"
total_immigration = df['Total'].sum()
st.metric("Total Countries", total_countries)
st.metric("years", duration)
st.metric("Total Immigration", total_immigration)
c1.metric("Total Countries", total_countries)
c2.metric("years", duration)
c3.metric("Total Immigration", total_immigration)
st.header("Immgiration analysis")
