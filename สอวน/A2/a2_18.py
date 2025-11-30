s,c = input().split()
c = int(c)
color = ['Red','Green','Blue']
st_in = {'R':0,'G':1,'B':2}[s]
r=[]
for i in range(c):
    c_in = (st_in + i)%3
    r.append(color[c_in])
print(' '.join(r))