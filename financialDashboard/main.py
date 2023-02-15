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
date_picker_to = DatePicker(tite="End Date", value="2020-02-01", min_date="2000-01-01",
                            max_date=dt.datetime.now().strftime("%Y-%m-%d"))
indicator_choice = MultiChoice(options=["100 Day SMA", "30 Day SMA", "Linear Regression Line"])

load_button = Button(label="Load Data", button_type="success")
load_button.on_click(lambda: on_button_click(stock1_text.value, stock2_text.value,
                                             date_picker_from.value, date_picker_to.value,
                                             indicator_choice.value))

layout = column(stock1_text, stock2_text, date_picker_from, date_picker_to, indicator_choice, load_button)

curdoc().clear()
curdoc().add_root(layout)

