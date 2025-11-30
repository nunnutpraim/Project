def check_pure_blood(word):
    word = word.upper()
    n = len(word)

    if all(c in 'TI' for c in word):
        return f"unknown {n}"

    max_a_streak = 0
    i = 0
    while i < n:
        c = word[i]
        if c not in 'RABIT':
            return f"no {i}"

        if c == 'R':
            i += 1
            a_count = 0
            while i < n and word[i] == 'A':
                a_count += 1
                i += 1
            if a_count == 0:
                return f"no {i}"
            max_a_streak = max(max_a_streak, a_count)

        elif c == 'A':
            # A ต้องมาหลัง R เท่านั้น
            return f"no {i}"

        elif c == 'B':
            i += 1
            if i >= n or word[i] not in 'IT':
                return f"no {i if i < n else n}"
            while i < n and word[i] in 'IT':
                i += 1

        else:  # I หรือ T
            i += 1

    return f"yes {max_a_streak}"
# ตัวอย่างการใช้งาน:
word = input().strip()
print(check_pure_blood(word))