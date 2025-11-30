N = int(input())
board = [input().strip() for _ in range(N)]


can_reach = [[False] * N for _ in range(N)]


if board[N-1][N-1] == '.':
    can_reach[N-1][N-1] = True


for i in reversed(range(N)):
    for j in reversed(range(N)):
        if board[i][j] == 'X':
            continue

        if i == N-1 and j == N-1:
            can_reach[i][j] = True

        elif (i + 1 < N and can_reach[i+1][j]) or (j + 1 < N and can_reach[i][j+1]):
            can_reach[i][j] = True


count = 0
for i in range(N):
    for j in range(N):
        if board[i][j] == '.' and can_reach[i][j]:
            count += 1

print(count)
