import pandas as pd
import streamlit as st
import numpy as np
import yfinance as yf
import plotly.express as px
#import pandas_ta as ta 

st.title('Stock Dashboard')

ticker_options = ["AAPL", "GOOGL", "MSFT", "TSLA", "AMZN"]
ticker = st.sidebar.selectbox("Select Ticker:", ticker_options)
start_date = st.sidebar.date_input('Start Date')
end_date = st.sidebar.date_input('End Date')


if ticker_options:
    # Convert dates to string format
    start_date = start_date.strftime('%Y-%m-%d')
    end_date = end_date.strftime('%Y-%m-%d')

    # Fetch data
    data = yf.download(ticker, start=start_date, end=end_date, progress=False)
    #st.write("Data Preview:", data.head())
    #st.write("Data Shape:", data.shape)


    # Check if data is empty
    if data.empty:
        st.warning("No data found for the selected ticker and date range. Please try again.")
    else:
        fig = px.line(data, x=data.index, y=data['Close'].squeeze(), title=ticker)
        st.plotly_chart(fig)
    import numpy as np

arr = np.array([0, 1, 2])

if arr.any():  # True because at least one element is nonzero
    print("At least one element is True")


pricing_data,fundamental_data,news=st.tabs(["Pricing Data","Fundamentl Data","Top 10 News"])

with pricing_data:
    st.header('Price Movements')
    st.write(data)