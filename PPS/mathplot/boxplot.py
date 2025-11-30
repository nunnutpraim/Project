import matplotlib.pyplot as plt
import numpy as np

data = np.array([20,30,40,50,60,70,80,90,30,80,70,75,82,45,68,72,84,88,52,25])
plt.boxplot(data,vert=False) #Trueจะเป็นแนวตั้ง
plt.show()