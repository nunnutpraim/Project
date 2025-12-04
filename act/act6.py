import string
import time

text = 'I am Gay'
temp = ''

for ch in text:
    for i in string.printable:
        time.sleep(0.02)
        print(temp + i)

        if i == ch:
            temp += ch
            break