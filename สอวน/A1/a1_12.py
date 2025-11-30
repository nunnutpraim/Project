n = int(input())
o = input()

t = n // 10 
on = n % 10
s = on*10 + t
if o == "+":
    r = n + s
else:
    r=n*s
print(f"{n} {o} {s} = {r}")
