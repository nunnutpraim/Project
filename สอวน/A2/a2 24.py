L, P = map(int, input().split())

jump_rabbit, jump_monkey, jump_frog = map(int, input().split())

score_map = {}
for _ in range(P):
    pos, score = map(int, input().split())
    score_map[pos] = score

def calculate_score(jump):
    score = 0
    pos = 0
    while pos <= L:
        if pos in score_map:
            score += score_map[pos]
        pos += jump
    return score

score_rabbit = calculate_score(jump_rabbit)
score_monkey = calculate_score(jump_monkey)
score_frog = calculate_score(jump_frog)

max_score = max(score_rabbit, score_monkey, score_frog)

if score_rabbit == max_score:
    print("Rabbit", max_score)
if score_monkey == max_score:
    print("Monkey", max_score)
if score_frog == max_score:
    print("Frog", max_score)