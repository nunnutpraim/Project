L, P = map(int, input().split())

# รับระยะกระโดดของสัตว์แต่ละตัว
jump_rabbit, jump_monkey, jump_frog = map(int, input().split())

# เก็บจุดเก็บแต้มไว้ใน dict
score_map = {}
for _ in range(P):
    pos, score = map(int, input().split())
    score_map[pos] = score

# ฟังก์ชันคำนวณคะแนนสำหรับแต่ละตัว
def calculate_score(jump):
    score = 0
    pos = 0
    while pos <= L:
        if pos in score_map:
            score += score_map[pos]
        pos += jump
    return score

# คำนวณคะแนน
score_rabbit = calculate_score(jump_rabbit)
score_monkey = calculate_score(jump_monkey)
score_frog = calculate_score(jump_frog)

# หา max score
max_score = max(score_rabbit, score_monkey, score_frog)

# แสดงผู้ชนะเรียงตามลำดับ Rabbit → Monkey → Frog
if score_rabbit == max_score:
    print("Rabbit", max_score)
if score_monkey == max_score:
    print("Monkey", max_score)
if score_frog == max_score:
    print("Frog", max_score)