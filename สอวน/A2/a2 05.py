W, H, M, N = map(int, input().split())
X = list(map(int, input().split()))  
Y = list(map(int, input().split()))  

X = [0] + X + [W]
Y = [0] + Y + [H]

widths = [X[i+1] - X[i] for i in range(len(X)-1)]
heights = [Y[i+1] - Y[i] for i in range(len(Y)-1)]

pieces = [w * h for h in heights for w in widths]

pieces.sort(reverse=True)

print(pieces[0], pieces[1])