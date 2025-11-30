import numpy as npy
book_list = ["math","sci","thai"]
idol_list = ["Lisa","Jenny","Rose"]
idol_list.append("Jisoo")
idol_list.sort()
print(idol_list)

book_list.insert(1,"social")
book_list.pop()
print(book_list)


m4 = ["dragon","noon","oscar"]
m5 = ["guz","praim","atom"]
student_list = m4+m5
print(student_list)
if "atom" in student_list:
    print("Found! atom")
else:
    print("not found atom")

A = npy.array([0,1.141,1.732])
B = npy.array([[-1],[0],[1]])
C = npy.array([[1,0,0],[0,1,0],[0,0,1]])
print(A)
print(B)
print(C)