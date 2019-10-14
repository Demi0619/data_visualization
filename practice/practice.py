import csv
import tkinter
from datetime import datetime
import matplotlib.pyplot as plt

filepath='data/sitka_weather_2018_simple.csv'
with open(filepath)as f:
    reader=csv.reader(f)
    header_row=next(reader)
    for index,value in enumerate(header_row):
        print(index,value)
    # prepare data
    Date,Prcp=[],[]
    for rows in reader:
        date=datetime.strptime(rows[2],'%Y-%m-%d')
        prcp=float(rows[3])
        Date.append(date)
        Prcp.append(prcp)

    #plot
    fig,ax=plt.subplots()
    ax.plot(Date,Prcp,color='red')
    plt.xlabel('date',fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel('rainfall rate',fontsize=16)
    plt.title('rainfall rate for sitka')
    plt.tick_params(axis='both',labelsize=10)
    plt.show()




