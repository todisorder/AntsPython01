import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)
#data = np.random.randn(2, 2)

# data = [[x1,x2],[y1,y2]]
data=[[1,2],
      [3,4]]
data2=[[5,2],
      [1,7]]
data=np.array(data)

fig = plt.figure()
#fig.show()
ax = plt.subplot(111)
ax.set_xlim(0, 10)
ax.set_ylim(0, 10),
#ax.set_xlim(0, 1), ax.set_xticks([])
#ax.set_ylim(0, 1), ax.set_yticks([])

pa = [1,2,4,2,3,4,5,3,4]
pb = [4,6,6,2,5,8,5,6,8]
pc = [7,3,2,4,6,4,4,4,6]
pd = [4,6,6,6,8,9,3,1,4]
ax.plot(pc,pd,'ro')
ax.plot(pa,pb)

#ax = plt.subplot(111)
#im = ax.imshow(np.arange(100).reshape((10, 10)))



plt.show()



