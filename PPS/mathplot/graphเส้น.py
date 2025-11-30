import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,2,5,7])
y = np.array([3,8,1,10])
plt.subplot(1,2,1)#rows,colum,index  เปรียบเทียบกราฟ
plt.plot(x,y)

x2 = np.array([1,3,6,8])
y2 = np.array([4,7,2,9])
plt.subplot(1,2,2)
plt.plot(x2,y2)

plt.show()