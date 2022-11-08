a,b=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
c=[]
d=[]
e=0
for i in l1:
    if((i in l2)and(i not in c)):
        e+=1
        c.append(i)
print(e)