import csv
import tkinter
import matplotlib.pyplot as plt
from datetime import datetime

filepath='data/sitka_weather_2018_simple.csv'
with open(filepath)as f:
    reader=csv.reader(f)
    header=next(reader)

    Tmax=[]
    Tmin=[]
    Date=[]
    for rows in reader:
        date = datetime.strptime(rows[2], '%Y-%m-%d')
        try:
           max=int(rows[5])
           min=int(rows[6])
        except ValueError:
            print('data error for date:',date)
        else:
            Tmin.append(min)
            Tmax.append(max)
            Date.append(date)

    print(Tmax)

fig,ax=plt.subplots()
ax.plot(Date,Tmax,'r',alpha=0.5)
ax.plot(Date,Tmin,'b',alpha=0.5)
plt.fill_between(Date,Tmin,Tmax,facecolor='green',alpha=0.1)
plt.xlabel('date',fontsize=16)
fig.autofmt_xdate()
plt.ylabel('temperature',fontsize=16)
plt.title('highest and lowest temperature change')
plt.tick_params(axis='both',labelsize=10)
plt.show()

