weekdays = {1: 'mon', 2:'tus', 3:'wed', 4:'thu', 5:'fri',6:'sat',7:'sun'}
print(weekdays.keys())
print(weekdays.items())
print(weekdays.get(2))   # print key no.2 
print(weekdays[2])

for i in weekdays:
    if weekdays[i]=='mon':
        key = i
print(key)
#ถ้าต้องการ value from key ที่กำหนดมาให้ = print(weekdays[2])
#ถ้าบอกvalue want key = for loopด้านบน
