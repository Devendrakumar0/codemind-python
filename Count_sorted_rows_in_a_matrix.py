a,b=map(int,input().split())
c=0
for i in range(a):
    l=list(map(int,input().split()))
    if(l==sorted(l) or sorted(l)==l[::-1]):
        c+=1
print(c)