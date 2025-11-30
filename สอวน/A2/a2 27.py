n = int(input())

scores = []
for _ in range(n):
    score = int(input())
    scores.append(score)

max_score = max(scores)

top_count = scores.count(max_score)

print(max_score)
print(top_count)