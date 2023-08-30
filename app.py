# importing Libraries and Confiugaration
import pandas as pd
import numpy as np
import streamlit as st
import yfinance as yf
import datetime
import pandas_datareader as web
import matplotlib.pyplot as plt

st.set_page_config(page_title="CAPM",
page_icon="chart_with_upward_trend",
layout='wide')

st.title("Capital Asset Pricing Model")

# Taking Input from User 

col1,col2 = st.columns([1,1])
try:
        
    with col1:
        stocks_list = st.multiselect("Choose 4 Stocks",('TSLA','NFLX','MSFT','AMZN','NVDA','GOOGL'),
        ['AMZN','TSLA','NFLX','MSFT'])
    with col2:
        year = st.number_input("Enter No of Years",1,10)
        
    # Downloading Data for sp500
    end = datetime.date.today()
    start = datetime.date(datetime.date.today().year-year,datetime.date.today().month,datetime.date.today().day)
    SP500 = web.DataReader(['sp500'],'fred',start,end)
    #print(SP500.tail())

    stocks_df = pd.DataFrame()

    for stock in stocks_list:
        data = yf.download(stock,period=f'{year}y')
        stocks_df[f'{stock}'] = data['Close']
        
    st.write(stocks_df.head())
except:
    st.write('Please wait..while fetching data from server.....')









  