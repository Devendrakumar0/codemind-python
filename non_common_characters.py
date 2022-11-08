s1=input()
s2=input()
s1=s1.casefold()
s2=s2.casefold()
a=[]
for i in s1:
    if(i!=" "):
        if(i not in s2)and(i not in a):
            a.append(i)
for i in s2:
    if(i!=" "):
        if(i not in s1)and(i not in a):
            a.append(i)
a=sorted(a)
if(len(a)==0):
    print(-1)
else:
    [print(i,end="")for i in a]