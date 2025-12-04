import time
import os

text = "POWER LOADING"

for i in range(30):
    os.system('cls' if os.name == 'nt' else 'clear')
    if i % 2 == 0:
        print("\033[1;31m" + text)    # bright red
    else:
        print("\033[0;31m" + text)    # dim red
    time.sleep(0.15)

print("\033[1;37m" + text)