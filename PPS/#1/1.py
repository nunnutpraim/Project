weekdays = {1: 'mon', 2:'tus', 3:'wed', 4:'thu', 5:'fri'}
print("weekdays =",weekdays)
weekdays.setdefault(6,'sat')    #เพิ่มสมาชิกของ dic
print("weekdays =",weekdays)
weekdays.update({6:'sun',7:'sat'})   #แก้ 6 เพิ่ม 7 แก้เฉพาะ value
print("weekdays =",weekdays)
weekdays.pop(3)  #pop key 3
weekdays.popitem() #popตัวสุดท้าย
weekdays.clear()
print("weekdays clear() =",weekdays)
