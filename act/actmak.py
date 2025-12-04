import random
import os
import time

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%^&*()"
width = 80
drops = [0] * width

while True:
    print("\033[0;32m", end="")  # green
    for i in range(width):
        char = random.choice(chars)
        if drops[i] == 0:
            if random.random() > 0.975:
                drops[i] = 1
        if drops[i] > 0:
            print(char, end="")
            drops[i] += 1
            if drops[i] > 20:
                drops[i] = 0
        else:
            print(" ", end="")
    print()
    time.sleep(0.03)        