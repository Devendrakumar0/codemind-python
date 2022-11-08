a,b=map(int,input().split())
l=[]
for i in range(a):
    d=list(map(int,input().split()))
    l.append(d)
c=0
for i in range(a):
    for j in range(b):
        if(i!=0 and j!=0 and i!=a-1 and j!=b-1):
            c+=l[i][j]
print(c)