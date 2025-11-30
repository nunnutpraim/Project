n = int(input())

count_overweight = 0

max_weight = -1
fattest_name = ""

for _ in range(n):
    name, weight_str = input().split()
    weight = int(weight_str)

    if weight > 15:  
        count_overweight += 1

    if weight > max_weight:
        max_weight = weight
        fattest_name = name

print(count_overweight)
print(fattest_name, max_weight)