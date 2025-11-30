N = int(input())
H = list(map(int, input().split()))

count = 0
for i in range(N):
    if (i == 0 or H[i] > H[i - 1]) and (i == N - 1 or H[i] > H[i + 1]):
        count += 1

print(count)