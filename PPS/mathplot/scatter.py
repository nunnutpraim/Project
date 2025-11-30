import matplotlib.pyplot as plt
import numpy as np

studdie_hours = np.array([1,2,3,4,5,6,7,8,9,10])
exam_score = np.array([55,58,67,68,77,78,87,88,92,100])

plt.scatter(studdie_hours,exam_score,color='skyblue',marker='o')
plt.title('study hours vs exam score')
plt.xlabel('study hours')
plt.ylabel('study scores')
plt.grid(True)
plt.show()