n = int(input())
rn = {
    1:"I",
    2:"II",
    3:"III",
    4:"IV",
    5:"v",
    6:"VI",
    7:"VII",
    8:"VIII",
    9:"IX"
}
if n < 0:
    print("Error : Please input positive number")
elif n > 9:
    print("Error : Out of range")
else:
    print(rn[n])