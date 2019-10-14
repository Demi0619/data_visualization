import matplotlib.pyplot as plt
import tkinter
input_value=range(1,101)
sqaures=[x**2 for x in input_value]
plt.style.use('seaborn-dark')
fig,ax=plt.subplots()
ax.scatter(input_value,sqaures,c=sqaures,cmap=plt.cm.Blues,s=10)
ax.set_title('sqaure numbers',fontsize=24)
ax.set_xlabel('value',fontsize=14)
ax.set_ylabel('sqaure of value',fontsize=14)
ax.tick_params(axis='both',labelsize=10)

plt.savefig('square.png',bbox_inches='tight')
