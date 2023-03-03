import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

from adtk.data import validate_series
from adtk.visualization import plot
from adtk.detector import *

data = pd.read_csv("monthly_csv.csv")
data["Date"] = pd.to_datetime(data["Date"])
data = data.set_index("Date")
data = data["Mean"]


quantile_detector = QuantileAD(low=0.01, high=0.99)
anomalies = quantile_detector.fit_detect(data)
plot(data, anomaly=anomalies, anomaly_color="red", anomaly_tag="marker")
plt.show()
