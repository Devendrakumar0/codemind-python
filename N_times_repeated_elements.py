n=int(input())
l=list(map(int,input().split()))
k=int(input())
a=[]
for i in range(n):
    if((l[i] not in a)and(k==l.count(l[i]))):
        a.append(l[i])
if(len(a)==0):
    print(-1)
else:
    print(*a)