import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
from thetadata import ThetaClient, OptionReqType, OptionRight, DateRange


def create_signals(ticker, exp_date, client):
    transactions = {
        "transaction_date": [],
        "ticker": [],
        "strike": [],
        "ex_date": [],
        "transaction_type": []
    }

    strikes = client.get_strikes(ticker, exp_date)
    for strike in strikes:
        try:
            data = client.get_hist_option(
                req=OptionReqType.EOD,
                root=ticker,
                exp=exp_date,
                strike=strike,
                right=OptionRight.CALL,
                date_range=DateRange(exp_date - dt.timedelta(90),  exp_date)

            )
            print(data)
        except:
            continue


client = ThetaClient()

with client.connect():
    ticker = "BMY"
    exp_dates = client.get_expirations(ticker)

    for exp_date in exp_dates[390:400]:
        try:
            create_signals(ticker, exp_date, client)
        except:
            continue
