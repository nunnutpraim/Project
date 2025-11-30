import numpy as npy
import random
x = npy.array([random.randint(1,6) for i in range(10)])
print(x)

y = npy.array([[random.randint(1,6) for i in range(3)]for j in range(2)])
print(y)

z = npy.array([0,1,2,3,4,5,6,7,8,9])
print(z[3:7])   #printตัวที่4-6
print(z[7:])