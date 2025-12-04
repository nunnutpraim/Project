import string
import time
import random
import os

text = "Hello World"
chars = string.printable  # ชุดตัวอักษรที่สุ่มได้
output = [" "] * len(text)

while True:
    done = True
    for i, ch in enumerate(text):
        if output[i] != ch:
            output[i] = random.choice(chars)
            done = False

    os.system('cls' if os.name == 'nt' else 'clear')
    print("".join(output))
    time.sleep(0.03)

    if done:
        break