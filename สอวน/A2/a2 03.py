N = int(input("Input N: "))
H_input = list(map(int, input(f"Input {N} values for H: ").split()))

if len(H_input) != N:
    print(f"Error: You must enter exactly {N} values.")
else:
    count = 0  

    for i in range(N):
        left = H_input[i - 1] if i > 0 else float('-inf')  
        right = H_input[i + 1] if i < N - 1 else float('-inf') 

        if H_input[i] > left and H_input[i] > right:
            count += 1

    print("Number of trees birds like:", count)
