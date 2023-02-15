import math
import datetime as dt

import numpy as np
import yfinance as yf

from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.layouts import row, column
from bokeh.models import TextInput, Button, DatePicker, MultiChoice


def load_data(ticker1, ticker2, start, end):
    df1 = yf.download(ticker1, start, end)
    df2 = yf.download(ticker2, start, end)
    return df1, df2


def plot_data(data, indicators, sync_axis=None):
    pass


def on_button_click(ticker1, ticker2, start, end, indicators):
    pass


stock1_text = TextInput(title="Stock 1")
stock2_text = TextInput(title="Stock 2")
date_picker_from = DatePicker(tite="Start Date", value="2020-01-01", min_date="2000-01-01",
                              max_date=dt.datetime.now().strftime("%Y-%m-%d"))

