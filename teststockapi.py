# -*- coding: utf-8 -*-
"""TestStockAPI.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1J4_teu5sOicxmAWPio_yn1G54JKzguCL
"""

from pandas_datareader import data as pdr
import yfinance as yf
import pandas as pd
import datetime

#getting updated Google stock history
googldata = pdr.get_data_yahoo("GOOGL", start="2020-01-01", end="2021-03-16")
googldata.to_csv("googl_stock1.csv")
googldata.to_json("googl_stock1.json")

#getting updated apple stock history
aapldata = pdr.get_data_yahoo("AAPL", start="2020-01-01", end='2021-03-16')
aapldata.to_csv("aapl_stock1.csv")
aapldata.to_json("json_stock1.json")

#getting updated Carnival stock history
ccldata = pdr.get_data_yahoo("CCL", start="2020-01-01", end="2021-03-16")
ccldata.to_json("ccl_stock1.json")
ccldata.to_csv("ccl_stock1.csv")

#getting updated Tesla stock history
TSLAdata = pdr.get_data_yahoo("TSLA", start="2020-01-01", end="2021-03-16")
TSLAdata.to_csv("TSLA_stock1.csv")
TSLAdata.to_json("TSLA_stock1.json")

#getting updated Microsoft stock history
msftdata = pdr.get_data_yahoo("MSFT", start="2020-01-01", end="2021-03-16")
msftdata.to_csv("MSFT_stock1.csv")
msftdata.to_json("MSFT_stock1.json")

#getting apple recommendations
aapl = yf.Ticker("AAPL")
aapl_rec = aapl.recommendations
aapl_rec.to_csv("aapl_rec.csv")

#getting Carnival recommendations
ccl = yf.Ticker("CCL")
ccl_rec = ccl.recommendations
ccl_rec.to_csv("ccl_rec.csv")

#getting Microsoft recommendations
msft = yf.Ticker("MSFT")
msft_rec = msft.recommendations
msft_rec.to_csv("msft_rec.csv")

#getting Telsa recommendations
tsla = yf.Ticker("TSLA")
tsla_rec = tsla.recommendations
tsla_rec.to_csv("tsla_rec.csv")