n=int(input())
l=list(map(int,input().split()))
d={}
for i in l:
    if(i not in d):
        d[i]=1
    else:
        d[i]+=1
m=1
for k,v in d.items():
    if(v>m):
        a=k
        m=v
print(a)