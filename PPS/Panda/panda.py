import pandas as pd
import numpy as np
scores= pd.Series([85,90,78,92,88], index=["ann","bob","cat","dan","eve"])
print(scores["cat"])
print(scores.iloc[1])

data_list = ["10.1",True,30.5,40,50.7]
data01 = pd.Series(data_list)
print(data01)

data_array = np.array([1.414, 1.732, 2.236, 2.718])
data02 = pd.Series(data_array)
print(data02)

midterm_score = [85, 90, 78, 92, 88]
students = ["ann","bob","cat","dan","eve"]
series_data = pd.Series(midterm_score,index = students)
print(series_data)

print(series_data[1])
print(series_data["cat"])


data = pd.DataFrame({"name" : ["jeft", "lisa", "jenny", "bambam", "jackson"],
                    "score" : [85,90,78,92,88,75],
                    "age" : [16,17,16,17,16,15],
                    "room" :["m3","m5","m5","m5","m4","m6"]})
print(data)


df = pd.DataFrame(data)
print(df.head())
print(df.describe())  #
print(df.loc[0])  #ตาม label index
print(df[df["age"]>16])

'''
data3 = pd.DataFrame(name)  #มีแถว colum 
print(data3)

data2 = pd.Series(name)  #ไม่มีแถว colum
print(data2)
'''