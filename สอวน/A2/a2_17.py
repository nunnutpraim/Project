size,type = input().split()
topping = input().split()
p = 0
if size == 'S':
    if type == 'R':
        p = 60
    else:
        p =80
elif size == 'M':
    if type == 'R':
        p = 80
    else:
        p =100
else:
    if type == 'R':
        p = 100
    else:
        p =120
if topping[0] == 'P':
    p += int(topping[1])*15
elif topping[0] == 'E':
    p += int(topping[1])*10
elif topping[0] == 'N':
    p += 0
print(p)