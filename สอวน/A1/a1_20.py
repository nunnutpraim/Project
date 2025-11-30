a = int(input())
b = int(input())
c= int(input())
if a>b and b>c:
    print("decreasing")
elif c>b and b>a:
    print("incresing")
else:
    print("neither")