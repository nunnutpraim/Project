numbers = input().split()
numbers = [int(num) for num in numbers]
seen = set()
unique_numbers = []
for num in numbers:
    if num not in seen:
        seen.add(num)
        unique_numbers.append(num)
print(*(map(str, unique_numbers)))