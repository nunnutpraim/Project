mycar = dict(brand='Honda',cc=2500,gear='auto')
print(mycar)
print(mycar['gear'])

for i in mycar:
    if mycar[i] =='auto':
        mycar = i
print(i)