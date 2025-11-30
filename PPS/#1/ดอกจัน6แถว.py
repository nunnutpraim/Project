n = int(input("Enter number"))
for i in range(n):
    for j in range(40):
        if i == 0 or i == n-1:
            print("*",end="")
        else:
            if j == 0 or j == 39:
                print("*",end="")
            else:
                print(" ",end="")
    print()