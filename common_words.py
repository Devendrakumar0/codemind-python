n1=input()
n2=input()
l1=list(n1.split())
l2=list(n2.split())
a=[]
l1=[i.upper() for i in l1]
for i in l2:
    if i.upper() in l1:
        a.append(i)
print(*a)