work = int(input())
test = int(input())
final = int(input())
workpass = work >= 5
testpass = test>=20
finalpass = final>=25
if workpass and testpass and finalpass:
    print("pass")
else:
    print("fail")