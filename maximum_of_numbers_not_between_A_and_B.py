n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
m=0
f=0
for i in l:
    if(i<a or i>b):
        if(i>m):
            f=1
            m=i
if(f==0):
    print(-1)
else:
    print(m)