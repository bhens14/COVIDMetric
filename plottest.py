import pandas as pd
import matplotlib.pyplot as plt

date_time = ["2021-01-01", "2021-01-02", "2021-01-03"]
date_time = pd.to_datetime(date_time)
data = [1, 2, 3]

DF = pd.DataFrame()
DF['value'] = data
DF = DF.set_index(date_time)
plt.plot(DF)
plt.gcf().autofmt_xdate()
plt.show()
