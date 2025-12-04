import random
import time
import os

text = "I GUZ PEN GAY"
glitch_chars = "!@#$%^&*()_-+=<>?/\\|[]{}"

for _ in range(20):
    glitched = ""
    for ch in text:
        if random.random() < 0.2:
            glitched += random.choice(glitch_chars)
        else:
            glitched += ch
    os.system('cls' if os.name == 'nt' else 'clear')
    print(glitched)
    time.sleep(0.05)

os.system('cls' if os.name == 'nt' else 'clear')
print(text)