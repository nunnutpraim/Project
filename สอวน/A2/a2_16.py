d_let,d_num = input().split()
t_let,t_num = input().split()
if d_let == t_let and d_num == t_num:
    r = 1000000
elif d_num == t_num:
    r = 100000
elif d_let == t_let and d_num[-3:] == t_num[-3:]:
    r = 2000
elif d_let == t_let and d_num[-2:] == t_num[-2:]:
    r = 1000
elif d_num[-3:] == t_num[-3:]:
    r = 200
elif d_num[-2:] == t_num[-2:]:
    r =100
elif d_let == t_let:
    r = 20
else:
    r = 0
print(r)