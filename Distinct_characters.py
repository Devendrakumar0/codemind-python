s=input()
s=s.casefold()
a=[]
b=[]
for i in s:
    if(i!=" "):
        if(i not in a):
            a.append(i)
for i in a:
    if(s.count(i)==1):
        b.append(i)
b=sorted(b)
if(len(b)==0):
    print(-1)
else:
    [print(i,end='')for i in b]