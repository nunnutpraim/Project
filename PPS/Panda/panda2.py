#intro to DataFrame
import pandas as pd

print("=== Pandas DataFrame ===")
#data represent as dictionary with key:value 
data = {
    "Name": ["Jeff", "Lisa", "Jenny", "Jisoo", "Bambam", "Jackson"],
    "Score": [85, 90, 78, 92, 88, 75],
    "Age": [16, 17, 16, 17, 16, 15],
    "Room": ["M.3", "M.5", "M.5", "M.5", "M.4", "M.6"]
}

df = pd.DataFrame(data)
#print(df)    #print as table with rows index and columns
#print("+++++++++ Head & Describe ++++++++")
print(df.head())
print(df.describe())
print("+++++++++++++++++++++++++++++++++++")

print(df.loc[0])  # ตาม label index
print()
print(df.iloc[2]) # ตามตำแหน่ง

#Filter
print("+++++ Filter Age>16 +++++ ")
print(df[df["Age"]>16])
print("+++++ Filter Room == 'M.5' +++++ ")
print(df[df["Room"]=='M.5'])