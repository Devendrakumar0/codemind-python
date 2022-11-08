a,b=map(int,input().split())
c=[]
s=0
d=0
for i in range(a):
    l=list(map(int,input().split()))
    s=s+l[d]+l[-(d+1)]
    d+=1
    if(a%2!=0 and a//2==i):
        s=s-l[b//2]
print(s)