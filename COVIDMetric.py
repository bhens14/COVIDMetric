import pandas as pd
import matplotlib.pyplot as plt
import requests
import json

#datasources
COwaterdata = 'https://opendata.arcgis.com/datasets/c6566d454edb47c680afe839a0b4fc26_0.geojson'
COcoviddata = 'https://opendata.arcgis.com/datasets/efd7f5f77efa4122a70a0c5c405ce8be_0.geojson'

#pull the COVID wastewater data
resp = requests.get(url=COwaterdata)
waterdatajson = resp.json()
waterdata = json.load(waterdatajson)

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

#COcoviddata = https://opendata.arcgis.com/datasets/efd7f5f77efa4122a70a0c5c405ce8be_0.geojson

#pull just the dates for processing
#rawdates = pd.DataFrame(data, columns= ['Person Name','Country'])
