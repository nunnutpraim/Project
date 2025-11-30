month = int(input())
day = int(input())
if (month % 3 == 0 and day >= 21) or month in (1,2) or (month == 3 and day < 21):
  print("Winter")
elif  (month % 3 == 0 and day >= 21) or month in (4,5) or (month == 6 and day < 21):
  print("Spring")
elif  (month % 3 == 0 and day >= 21) or month in (7,8) or (month == 9 and day < 21):
  print("Summer")
elif  (month % 3 == 0 and day >= 21) or month in (10,11) or (month == 12 and day < 21):
  print("fall")