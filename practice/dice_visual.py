from roll_dice import RollDice
from plotly.graph_objs import Bar,Layout
from plotly import offline

rd1=RollDice()
rd2=RollDice(5)

results=[]
for i in range(500):
    result=rd1.roll_dice()+rd2.roll_dice()
    results.append(result)

frequencies=[]
for value in range(2,rd1.dice_sides+rd2.dice_sides+1):
    frequency=results.count(value)
    frequencies.append(frequency)

x_vaule=list(range(2,rd1.dice_sides+rd2.dice_sides+1))
data=[Bar(x=x_vaule,y=frequencies)]
x_layout={'title':'dice sides','dtick':1}
y_layout={'title':'frequencies'}
layout=Layout(title='Result of rolling 2 dice',xaxis=x_layout,yaxis=y_layout)
offline.plot({'data':data,'layout':layout},filename='d6.html')

