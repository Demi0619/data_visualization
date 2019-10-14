import csv
from plotly.graph_objs import Layout,Scattergeo
from plotly import offline
import json

filepath='data/data/world_fires_1_day.csv'
with open(filepath) as f1:
    reader=csv.reader(f1)
    header_row=next(reader)
    for index,value in enumerate(header_row):
         print(index,value)
    lons=[]
    lats=[]
    bris=[]
    for row in reader:
        lons.append(row[1])
        lats.append(row[0])
        bris.append(float(row[2]))
data=[{
    'type':'scattergeo',
    'lon':lons,
    'lat':lats,
    'marker':{
        'size':[float(bri)/40 for bri in bris],
        'color':bris,
        'colorscale':'Rainbow',
        'reversescale':False,
        'colorbar':{'title':'Brightness'},
    }
}]
my_layout=Layout(title='fires spread world')
fig={'data':data,'layout':my_layout}
offline.plot(fig,'fire_spread.html')