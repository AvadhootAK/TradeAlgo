import pandas as pd 
import streamlit as st, numpy as np, yfinance as yf
import plotly.express as px 

st.title("Welcome to Streamlit")
st.header("Streamlit python")

df=pd.DataFrame({
    'first column':[1,2,3,4,5],
    'second column':[10,20,30,40,50]})

st.write(df)
x= st.sidebar.slider('x',0,10)
st.write(x*x)

chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['a','b','c'])

st.line_chart(chart_data)
