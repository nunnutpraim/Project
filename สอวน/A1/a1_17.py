y1 = int(input())
m1 = int(input())
d1 = int(input())
y2 = int(input())
m2 = int(input())
d2 = int(input())
p1 = [y1,m1,d1]
p2 = [y2,m2,d2]
if p1 > p2:
    print("2")
elif p2 > p1:
    print("1")
else:
    print(0)


