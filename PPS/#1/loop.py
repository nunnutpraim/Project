x = 0
while x <= 10:
    y = 2*x+1
    print("f(%d)=%d"%(x,y))
    x = x+1
a = 8
b = 12.74
c = 3.14124
print("b =%.6f" %b)
print("a=%d b=%.3f" %(a,b))  # f = floating point
print(f"a={a} b={b}")
print("a={0} b={1:.3f}".format(a,b))  #format = %
print("c=%.2f"%c)
print("a=%d b=%d c=%d" %(a,b,c))