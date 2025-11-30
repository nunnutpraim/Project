while True:
    a = input()
    if len(a) == 5 and a.isalpha() and a.isupper():
        break 
r = "" 
c = 1
for i in range(1,5):
    if a [i] == a[i-1]:
        c += 1
    else:
        r += str(c) + a[i-1]
        c = 1
r += str(c) + a[i]
print(r)

