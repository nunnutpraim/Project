import string
import time
import random
import os

text = "Hello World"
chars = string.ascii_letters + string.digits + string.punctuation + " "
result = ""

for ch in text:
    for _ in range(8):  # จำนวนครั้งที่สุ่มต่อ 1 ตัว
        rand = random.choice(chars)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(result + rand)
        time.sleep(0.03)

    result += ch  # ล็อกตัวจริง

os.system('cls' if os.name == 'nt' else 'clear')
print(result)