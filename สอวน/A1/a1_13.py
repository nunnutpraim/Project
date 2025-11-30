a = input()
n = input()
if a == "H" and n == "4567":
    print('"safe unlocked"')
elif a == "H" and n!="4567":
    print("safe locked - change digit")
elif a != "H" and n == "4567":
    print("safe locked - change char" )
else:
    print("safe locked")
