import pandas as pd
import matplotlib.pyplot as plt
from plotnine import *
from plotnine.data import diamonds

df = diamonds

p = (
    ggplot(df)
    + aes(x="price")
    + geom_histogram()
)

p.draw()
plt.show()
