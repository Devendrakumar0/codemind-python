a,b=map(int,input().split())
c=[]
d=[]
for i in range(a):
    c.append(list(map(int,input().split())))
for i in range(b):
    s=0
    for j in range(a):
        s=s+c[j][i]
    d.append(s)
print(max(d))