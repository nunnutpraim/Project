import numpy as np
a = np.array([10,20,30,40])
b = np.array([1,2,3,4])
c = np.array([1,1.4,7,14])
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)

zeros = np.zeros(5)
print(zeros)

arr=np.arange(0,11,2)
print(arr)

arr=np.linspace(10,20,5)
print(arr)

print(a+b)
print(a*b)
print(a**2)
print(np.sqrt(a))   #หารากที่2
print(np.sum(a))
print(np.mean(a))
print(np.max(a))
print(np.min(a))

area = np.pi*(c**2)    #หาพื้นที่วงกลม
print(area)

arr = np.array([10,20,30,40])
print(arr[-1])   #-1แสดงค่าตัวสุดท้าย ไม่ต้องไปนั่งนับ
print(arr[0:3])
print(arr[arr>25])

arr2d = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])
print(arr2d[0])
print(arr2d[:, 0])
print(arr2d[0,2])

print(np.sum(arr2d,axis=0))   #หาค่าแกน x,y


arr = np.array([1,2,3,4,5,6,7,8,9])
print(arr)
a3x3 = arr.reshape(3,3)
print(a3x3)

arr=np.array([[1,2,3],[4,5,6]])
arr = arr.reshape(1,6)
print(arr)