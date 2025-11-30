dic = {}
for i in range(5):
    a = input("")
    dic.setdefault(i+1,a)
    dic.update({1:'mon',2:'tue',3:'wed',4:'thu',5:'fri'})
    print(dic)
    