def aLine():
    print("-"*50)
    print()

def bLine(ch):  #ch = ตัวแปร
    print(ch*50)
    print()

def cLine(ch,n):  #ch = + ,n = 70
    for i in range(n+1):
        print(ch,end="")
    print()

#call aLine()
aLine()
#call bLine('x)
bLine('x')
#call cLine('+',70)
cLine('+',70)