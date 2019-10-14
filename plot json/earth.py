import json
from plotly.graph_objs import Layout,Scattergeo
from plotly import offline


filepath='data/data/eq_data_30_day_m1.json'
with open(filepath) as f:
    json_data=json.load(f)

with open('data/data/readable.json','w') as readable:
    json.dump(json_data,readable,indent=4)

features=json_data['features']
mags=[]
Long=[]
Lati=[]
Title=[]
for feature in features:
    Title.append(feature['properties']['title'])
    Long.append(feature['geometry']['coordinates'][0])
    Lati.append(feature['geometry']['coordinates'][1])
    mags.append(feature['properties']['mag'])

data=[
    {'type':'scattergeo',
     'lon':Long,
     'lat':Lati,
     'text':Title,
     'marker':{
             'size':[5*mag for mag in mags],
             'color':mags,
             'colorscale':'Rainbow',
             'reversescale':True,
             'colorbar':{'title':'magntitude'}
               },
      }]
my_layout=Layout(title=json_data['metadata']['title'])
fig={'data':data,'layout':my_layout}
offline.plot(fig,filename='earthquake_spread.html')

