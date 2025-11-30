arr = []
for _ in range(5):
    row = list(map(int, input().split()))
    arr.append(row)

bad_row = -1
bad_col = -1

for i in range(5):
    if sum(arr[i]) % 2 != 0:
        bad_row = i
        break

for j in range(5):
    col_sum = sum(arr[i][j] for i in range(5))
    if col_sum % 2 != 0:
        bad_col = j
        break

print(bad_row, bad_col)