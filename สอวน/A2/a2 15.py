width, length, layers = map(int, input().split())
price_per_meter = int(input())

perimeter = 2 * (width + length)

total_length = perimeter * layers

total_price = total_length * price_per_meter

print(total_length)
print(total_price)