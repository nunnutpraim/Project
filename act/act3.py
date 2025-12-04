import time
import sys

text = "Hello World..."

for ch in text:
    print(ch, end="", flush=True)
    time.sleep(0.3)

print()