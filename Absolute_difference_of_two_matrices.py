n=int(input())
a=[]
b=[]
d=[]
for i in range(n):
    a.append(list(map(int,input().split())))
for i in range(n):
    b.append(list(map(int,input().split())))
for i in range(n):
    c=[]
    for j in range(n):
        c.append(abs(b[i][j]-a[i][j]))
    d.append(c)
for i in d:
    print(*i)