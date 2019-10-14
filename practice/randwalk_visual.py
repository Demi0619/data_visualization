from matplotlib import pyplot as plt
from randomwalk import Randomwalk

randomwalk=Randomwalk()
randomwalk.fill_walk()
fig,ax=plt.subplots()
point_number=range(randomwalk.total_walk)
ax.plot(randomwalk.x_place,randomwalk.y_place,c='red')
ax.scatter(0,0,c='blue',s=10)
ax.scatter(randomwalk.x_place[-1],randomwalk.y_place[-1],c='blue',s=10)
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()