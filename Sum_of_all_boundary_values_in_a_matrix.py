a,b=map(int,input().split())
l=[]
for i in range(a):
    d=list(map(int,input().split()))
    l.append(d)
c=0
for i in range(a):
    for j in range(b):
        if(i==0 or j==0 or i==a-1 or j==b-1):
            c+=l[i][j]
print(c)