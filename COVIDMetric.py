import pandas as pd
import matplotlib.pyplot as plt

#import the whole CSV file
raw = pd.read_csv (r'CDPHE_COVID19_Wastewater_Dashboard_Data (test).csv')
data = pd.DataFrame(raw, columns= ['Date','SARS_CoV_2_copies_L'])
#print(data)



#data['Date'] = pd.to_datetime(data['Date'])
#print(data)

plotdata = pd.DataFrame()
plotdata['SARS_CoV_2_copies_L'] = data['SARS_CoV_2_copies_L']
plotdata = plotdata.set_index(pd.to_datetime(data['Date']))

plotdata = plotdata.sort_values('Date')

plt.plot(plotdata)
plt.gcf().autofmt_xdate()
plt.show()

#pull just the dates for processing
#rawdates = pd.DataFrame(data, columns= ['Person Name','Country'])
