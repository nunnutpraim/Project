start, count = input().split()
count = int(count)

colors = ['Red', 'Green', 'Blue']

start_index = {'R': 0, 'G': 1, 'B': 2}[start]

result = []
for i in range(count):
    color_index = (start_index + i) % 3
    result.append(colors[color_index])

print(' '.join(result))
print(*result)