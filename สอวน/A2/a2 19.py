text = input()
text_lower = text.lower()
n = len(text)

max_u = 0
found = False

for i in range(n):
    if text_lower[i] == 'b':
        count_u = 0
        j = i + 1
        while j < n and text_lower[j] == 'u':
            count_u += 1
            j += 1
        if count_u >= 2:
            found = True
            max_u = max(max_u, count_u)

if found:
    print(f"Yes {max_u}")

else:
    if 'b' in text_lower:
        idx = text_lower.index('b')
        result = text[:idx+1] + 'U' * (n - idx - 1)
        print(result)

    else:
        pattern = "BUU"
        result = ""
        for i in range(n):
            result += pattern[i % 3]
        print(result)
