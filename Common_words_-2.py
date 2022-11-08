s1=input()
s2=input()
s1=s1.casefold()
s2=s2.casefold()
l1=list(s1.split())
l2=list(s2.split())
c=0
for i in l1:
    if(i in l2):
        if(l1.count(i)==1 and l2.count(i)==1):
            c+=1
print(c)