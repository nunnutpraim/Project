n = int(input())

id1 = input().strip()
id2 = input().strip()

wrong_count = 0

for i in range(n):
    digit1 = int(id1[i])
    digit2 = int(id2[i])
    if digit1 + digit2 != 9:
        wrong_count += 1

if wrong_count == 0:
    print("YES")
else:
    print("NO", wrong_count)