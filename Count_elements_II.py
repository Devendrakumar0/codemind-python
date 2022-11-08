a,b=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
c=[]
d=[]
e=0
for i in l1:
    if((i not in l2)and(i not in c)):
        e+=1
        c.append(i)
for i in l2:
    if((i not in l1)and(i not in d)):
        e+=1
        d.append(i)
print(e)